from dataclasses import dataclass
from src.environs import *
import mysql.connector
from mysql.connector import Error


@dataclass
class SQLClass:
    mysql_db: str
    mysql_host: str
    mysql_username: str
    mysql_password: str
    db_connection = mysql.connector.connect

    def connect(self):
        try:
            self.db_connection(
                database=self.mysql_db,
                host=self.mysql_host,
                user=self.mysql_username,
                password=self.mysql_password
            )
        except Error as error:
            print(f"Error connecting: {error}")

    def __str__(self):
        return f"{self.mysql_db} {self.mysql_host} {self.mysql_username}"


sql_object = SQLClass(mysql_db=mysql_db,
                      mysql_host=mysql_host,
                      mysql_username=mysql_username,
                      mysql_password=mysql_password)
print(sql_object)
print(sql_object.connect())
