import datetime as dt
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

class SQLHelper():

    def __init__(self):
        self.connection_string = "sqlite:///Resources/hawaii.sqlite"
        self.engine = create_engine(self.connection_string)

    def getPrecipitation(self):
        qry = f"""
            SELECT
                date,
                prcp
            FROM
                Measurement
            WHERE
                date > '2016-08-23'
            """

        conn = self.engine.connect()
        df = pd.read_sql(qry, conn)
        conn.close()

        return df

    def getStation(self):
        qry = f"""
            SELECT 
                station
            FROM
                Measurement
            GROUP BY
                station
            """

        conn = self.engine.connect()
        df = pd.read_sql(qry, conn)
        conn.close()

        return df

    def getActive(self):
        qry = f"""
            SELECT
                date,
                tobs
            FROM
                Measurement
            WHERE
                date > '2016-08-23'
            AND
                station = 'USC00519397'
            """

        conn = self.engine.connect()
        df = pd.read_sql(qry, conn)
        conn.close()

        return df

    def getVacation(self):
        qry = f"""
            SELECT
                date,
                min(tobs) as min_temp,
                max(tobs) as max_temp,
                avg(tobs) as avg_temp
            FROM
                Measurement
            WHERE
                date > '2017-04-01'
            AND
                date < '2017-04-15'
            """

        conn = self.engine.connect()
        df = pd.read_sql(qry, conn)
        conn.close()

        return df