from dataclasses import dataclass
from src.environs import *


@dataclass
class SQLClass:
    mysql_db: str
    mysql_host: str
    mysql_username: str
    mysql_pass: str

    def return_test(self):
        return self.mysql_db, self.mysql_username, self.mysql_host

    def __str__(self):
        return_string = f"{mysql_host}, {mysql_db}"
        return return_string


sql = SQLClass(mysql_db=mysql_db, mysql_host=mysql_host, mysql_username=mysql_username, mysql_pass=mysql_pass)
print(sql.return_test())
print(sql)
