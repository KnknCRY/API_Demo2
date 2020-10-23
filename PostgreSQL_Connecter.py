import psycopg2
import os

import datetime
from dotenv import load_dotenv


class Connector:

    def __init__(self):
        load_dotenv()
        self.__db = psycopg2.connect(
            database=os.getenv("DATABASE_NAME"),
            user=os.getenv("SERVER_USER"),
            password=os.getenv("ADMIN_PASSWORD"),
            host=os.getenv("SERVER_IP"),
            port="5432"
        )
        self.__cur = self.__db.cursor()
        self.successExecute = False
        self.errMsg = ""

    def getStationData(self):
        add_5sec = (datetime.datetime.now() + datetime.timedelta(seconds=5)).strftime("%Y-%m-%d %H:%M:%S")
        sub_5sec = (datetime.datetime.now() - datetime.timedelta(seconds=5)).strftime("%Y-%m-%d %H:%M:%S")
        self.__cur.execute(
            f"""
                SELECT 
                    *
                FROM 
                    bottom_layer 
                WHERE 
                    end_time < '{add_5sec}'
                AND end_time > '{sub_5sec}'
                LIMIT 1;
            """
        )
        print(sub_5sec, add_5sec)
        result = self.__cur.fetchall()
        return result
