from contextlib import closing

import snowflake.connector

from tinybird_cdk import (cloud, config, connector, errors, export, formats,
                          logger, utils)


# The `snowql` CLI for Snowflake understands a good deal of environment
# variables:
#
#     https://docs.snowflake.com/en/user-guide/snowsql-start.html
#
# However, the Python library does not. I have created an issue for this:
#
#     https://github.com/snowflakedb/snowflake-connector-python/issues/1085
#
# Meanwhile, we support a subset of variables with the standard names.
class Connector(connector.SQLConnector):
    # The default value for MAX_FILE_SIZE in COPY INTO is 16 MB. Exports may be
    # way larger, though, like 20 GB. Better set a larger value (1 GB).
    MAX_FILE_SIZE = 1024**3
    TIMESTAMP_FORMAT_TZ = 'YYYY-MM-DD HH24:MI:SS.FF3 TZHTZM'
    TIMESTAMP_FORMAT_NTZ = 'YYYY-MM-DD HH24:MI:SS.FF3'

    # https://docs.snowflake.com/en/sql-reference/sql/copy-into-location.html#type-csv
    FILE_FORMAT_FOR_CSV = "TYPE=CSV COMPRESSION=NONE FIELD_DELIMITER=',' RECORD_DELIMITER='\\n' ESCAPE_UNENCLOSED_FIELD=NONE FIELD_OPTIONALLY_ENCLOSED_BY='\"' BINARY_FORMAT=HEX NULL_IF=()"

    def __init__(self):
        super().__init__()
        self.sf_stage = config.get('SF_STAGE')

    def get_scopes(self):
        return (
            connector.Scope(name='Databases', value='database'),
            connector.Scope(name='Schemas', value='schema'),
            connector.Scope(name='Tables', value='table')
        )

    def list_scope(self, parents={}):
        if 'database' in parents:
            if 'schema' in parents:
                return self._list_tables(parents['database'], parents['schema'])
            return self._list_schemas(parents['database'])
        return self._list_databases()

    def _list_databases(self):
        databases = []
        # The 'show databases' sentece includes also default databases SNOWFLAKE and SNOWFLAKE_SAMPLE_DATA.
        # Apparently, there's no way to filter out those databases from the result set. So we'll just query the information_schema.
        for database in list(self._query('select distinct database_name from information_schema.databases where database_name not in (\'SNOWFLAKE\',\'SNOWFLAKE_SAMPLE_DATA\')')):
            databases.append(connector.Scope(name=database['DATABASE_NAME'], value=database['DATABASE_NAME']))
        databases.sort(key=lambda database: database.name)
        return databases

    def _list_schemas(self, database):
        schemas = []
        for schema in list(self._query(f'show schemas in database {database}')):
            schemas.append(connector.Scope(name=schema['name'], value=f'{schema["database_name"]}.{schema["name"]}'))
        schemas.sort(key=lambda schema: schema.name)
        return schemas

    def _list_tables(self, database, schema):
        tables = []
        for table in list(self._query(f'show tables in {database}.{schema}')):
            tables.append(connector.Table(
                name=table['name'], value=f'{table["database_name"]}.{table["schema_name"]}.{table["name"]}',
                num_rows=table['rows'], size=table['bytes']
            ))
        tables.sort(key=lambda table: table.name)
        return tables

    def suggest_schema(self, _scopes):
        raise Exception('Not implemented')

    def _query(self, sql):
        with closing(self._connection()) as connection:
            with closing(connection.cursor(snowflake.connector.DictCursor)) as cursor:
                cursor.execute(sql)
                return cursor.fetchall()

    def _export(self, query, fmt, row_limit):
        if fmt != formats.CSV:
            raise errors.UnsupportedFormatError(fmt)

        with closing(self._connection()) as connection:
            logger.info('Connected to Snowflake')
            with closing(connection.cursor()) as cursor:
                # We want to make sure timestamps reflect the data and can be imported.
                # See https://docs.snowflake.com/en/sql-reference/parameters.html.
                cursor.execute('''
                  ALTER SESSION SET
                    TIMESTAMP_OUTPUT_FORMAT     = 'YYYY-MM-DD HH24:MI:SS.FF3 TZHTZM',
                    TIMESTAMP_NTZ_OUTPUT_FORMAT = 'YYYY-MM-DD HH24:MI:SS.FF3',
                    TIMESTAMP_LTZ_OUTPUT_FORMAT = NULL,
                    TIMESTAMP_TZ_OUTPUT_FORMAT  = NULL
                ''')
                cursor.execute('SELECT GET_STAGE_LOCATION(%s)', (f'@{self.sf_stage}',))
                location = cursor.fetchone()[0].rstrip('/')
                directory = f'tinybird/{utils.random_dirname()}'
                logger.info(f'Unloading to {location}/{directory}/')

                # Trailing "/part" to get file names like ".../part_1_2_0.csv".
                external_stage = f'@{self.sf_stage}/{directory}/part'

                # https://docs.snowflake.com/en/sql-reference/sql/copy-into-location.html
                sql = f'''
                    COPY INTO {external_stage} FROM ({query})
                      FILE_FORMAT = ({self.FILE_FORMAT_FOR_CSV})
                      MAX_FILE_SIZE = {self.MAX_FILE_SIZE}'''
                logger.debug(f'Executing SQL statement\n{sql}')
                cursor.execute(sql)

        parsed_url = cloud.parse_url(location)
        client = cloud.client_for(parsed_url.service)
        if parsed_url.key:
            directory = f'{parsed_url.key}/{directory}'
        return export.CloudDir(client, parsed_url.bucket, directory)

    def _connection(self):
        return snowflake.connector.connect(
            account=config.get('SF_ACCOUNT'),
            user=config.get('SF_USER'),
            password=config.get('SF_PWD'),
            role=config.get('SF_ROLE'),
            warehouse=config.get('SF_WAREHOUSE'),
            database=config.get('SF_DATABASE'),
            schema=config.get('SF_SCHEMA')
        )
