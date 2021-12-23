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

    def select_all_query(self, query) -> list:
        """returns list of query results"""
        cursor = self.db_connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
        except Error as err:
            print(f"Error selecting many: {err}")
        cursor.close()
        return results

    def select_one_query(self, query) -> list:
        """Returns single list of query results"""
        cursor = self.db_connection.cursor(buffered=True)
        try:
            cursor.execute(query)
            results = cursor.fetchone()
        except Error as err:
            print(f"Error selecting one: {err}")
        cursor.close()
        return results

    def insert_query(self, query) -> int:
        """Insert Query"""
        cursor = self.db_connection.cursor()
        try:
            cursor.execute(query)
            self.db_connection.commit()
            results = cursor.rowcount
        except Error as err:
            print(f"Error inserting: {err}")
        cursor.close()
        return results

    def delete_query(self, query) -> int:
        """Delete Query"""
        cursor = self.db_connection.cursor()
        try:
            cursor.execute(query)
            self.db_connection.commit()
            results = cursor.rowcount
        except Error as err:
            print(f"Error deleting: {err}")
        cursor.close()
        return results

    def update_query(self, query) -> int:
        """Update Query"""
        cursor = self.db_connection.cursor()
        try:
            cursor.execute(query)
            self.db_connection.commit()
        except Error as err:
            print(f"Error updating: {err}")
        cursor.close()
        return cursor.rowcount
