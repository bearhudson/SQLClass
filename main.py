from dataclasses import dataclass
import mysql.connector
from mysql.connector import Error
from src.environs import *


@dataclass
class SQLClass:
    mysql_db: str
    mysql_host: str
    mysql_username: str
    mysql_password: str
    try:
        db_connection = mysql.connector.connect(database=mysql_db,
                                                host=mysql_host,
                                                user=mysql_username,
                                                password=mysql_password)
    except Error as error:
        print(f"Error connecting: {error}")

    def __str__(self):
        return f"{self.mysql_db} {self.mysql_host} {self.mysql_username}"

    def select_all_query(self, query):
        cursor = self.db_connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
        except Error as err:
            print(f"Error: '{err}'")
        cursor.close()
        return results

    def select_one_query(self, query):
        cursor = self.db_connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchone()
        except Error as err:
            print(f"Error: '{err}'")
        cursor.close()
        return results

    def insert_query(self, query):
        cursor = self.db_connection.cursor()
        try:
            cursor.execute(query)
            self.db_connection.commit()
        except Error as err:
            print(f"Error: {err}")
        cursor.close()

    def delete_query(self, query):
        cursor = self.db_connection.cursor()
        try:
            cursor.execute(query)
            self.db_connection.commit()
        except Error as err:
            print(f"Error: {err}")
        cursor.close()

    def update_query(self, query):
        cursor = self.db_connection.cursor()
        try:
            cursor.execute(query)
            self.db_connection.commit()
        except Error as err:
            print(f"Error: {err}")
        cursor.close()
        return cursor.rowcount


sql_object = SQLClass(mysql_db=mysql_db,
                      mysql_host=mysql_host,
                      mysql_username=mysql_username,
                      mysql_password=mysql_password
                      )
print(sql_object)
print(sql_object.select_all_query(query='SELECT * from table1;'))
