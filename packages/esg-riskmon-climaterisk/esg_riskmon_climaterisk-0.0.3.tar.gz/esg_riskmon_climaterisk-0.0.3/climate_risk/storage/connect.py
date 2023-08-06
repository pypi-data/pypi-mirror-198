import os
import pyodbc
import snowflake.connector

from typing import Optional


class DefaultConnector():
    """
    parent class, has functions shared between its isntantiations (sql and snowflake).

    :params: db_name: this is the name of the db to get data from
    :params: user_id: this is the snowflake id that ends in "nbim.no"

    NOTE: these connectors are indpendent from database/schema. it needs to be specified in the query
    """
    def __init__(
        self,
        user_id: Optional[str] = None
    ) -> None:
        self.user_id = user_id
        self.connection = None

    def terminate(self):
        self.connection.close()
        return "Connection terminated."


class SQLConnector(DefaultConnector):
    """
    instantiation for SQL db.
    it either initiates or terminates a connection.
    """
    def __init__(
        self,
        user_id: Optional[str] = None
    ) -> None:
        super().__init__(user_id)

    def initiate(self):
        cn_str = (
            'DRIVER={SQL Server};'
            'SERVER=CAFEPROD;'
            'Trusted_Connection=yes'
        )
        self.connection = pyodbc.connect(cn_str)
        print(f"Connection initiated by {self.user_id}.")
        return self.connection


class SnowflakeConnector(DefaultConnector):
    """
    instantiation for Snowflake db.
    it either initiates or terminates a connection.
    """
    def __init__(
        self,
        user_id: str
    ) -> None:
        super().__init__(user_id)

        # Create the environement variable with the user ID
        os.environ['NBUID'] = self.user_id

        # And create variables to use it
        self.nbimid = os.getenv('NBUID')

    def initiate(self):
        # TODO: understand which of these params needs to be passed
        # probs query tag?
        self.connection = snowflake.connector.connect(
            authenticator='externalbrowser',
            user=self.nbimid,
            database='PROD',
            schema='RISKMON',
            role='GINEVRA_BERTI_MEI_NBIM_NO_ROLE_PROD',
            account='nbim-data.privatelink',
            warehouse='WH_READ_PROD',
            session_parameters={
                'QUERY_TAG': self.user_id
            }
        )
        print(f"Connection initiated by {self.user_id}.")
        return self.connection
