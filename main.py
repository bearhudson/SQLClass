from SQLClass import SQLClass
from src.environs import *

sql_object = SQLClass(mysql_db=mysql_db,
                      mysql_host=mysql_host,
                      mysql_username=mysql_username,
                      mysql_password=mysql_password
                      )

sql_object.select_all_query()
