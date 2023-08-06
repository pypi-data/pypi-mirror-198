import textwrap

import pandas as pd
from entities.const import ConnectorType
from snowflake.connector.pandas_tools import write_pandas


class Reader():
    """
    this is a first version of a generic data reader

    TODO: error catching
    TODO: separate init and termination of connection from query execution, so that
    we can execute multiple queries separately without renewing the connection
    """
    def __init__(
        self,
        connector: ConnectorType,
        user_id: str
    ):
        self.connection = connector(user_id)
        self.cp_connection = self.connection.initiate()

    def query_snowflake(self, query, file=False, variable=None):
        # TODO: !!! this class is going to be modified on 13/09 currently in use borrowed from sys sustainbility repo !!!
        '''Query against snowflake - can be to return data (both single and multiple queries) or update statements'''
        if file is True:
            fd = open(query, 'r')
            query = fd.read()
            fd.close()
            if query[-1] != ';':
                query = query + ';'
            else:
                pass
            if '?' in query and variable is not None:
                query = query.replace('?', "'" + variable + "'")
            else:
                pass
            query = query.replace(';', ';--,')
            query = query.split('--,')
            query.pop()
            for command in query:
                textwrap.dedent(command)
                cur = self.cp_connection.cursor()
                cur.execute(command)
            df = cur.fetch_pandas_all()
            cur.close()
            return df
        else:
            if query[-1] != ';':
                query = query + ';'
            else:
                pass
            query = query.replace(';', ';--,')
            query = query.split('--,')
            query.pop()
            for command in query:
                print('Snowflake: Querying')
                # print(command)
                textwrap.dedent(command)
                cur = self.cp_connection.cursor()
                cur.execute(command)
                if "set " not in command.lower() and "select" in command.lower():
                    df = cur.fetch_pandas_all()
                    print('Snowflake: Data Extracted')
                    return df
                else:
                    print('Snowflake: Queries Run')
                    pass
            cur.close()

    def get_dict_data(
        self,
        query: str
    ):

        """
        TODO: discuss with @Daniel if we want to have here an output as dict
        so use the dict/zip option and then have a separate function for df
        else we can do pd.read here and not have get_df
        imo this depends on what we should be working with dfs or dicts
        i prefer dicts for data validation, but dfs are faster
        """
        # OPTION 2: work with dicts

        cursor = self.cp_connection.cursor()
        res = cursor.execute(query)
        desc = [x[0] for x in cursor.description]
        data = [dict(zip(desc, x)) for x in res]
        return data

    def get_df_data(self, query: str):
        # OPTION 1: pd read, no need for get_df()
        data = self.get_dict_data(query)
        return pd.DataFrame(data)

    def write_df(
        self, df: pd.DataFrame,
        table: str, schema: str, db: str
    ):
        # Write the data from the DataFrame to the table named <name specified>.
        success, nchunks, nrows, _ = write_pandas(
            self.cp_connection,
            df,
            table_name=table,
            schema=schema,
            database=db
        )
        return success, nchunks, nrows

    def terminate(self):
        self.connection.terminate()
        print("Connection terminated.")
