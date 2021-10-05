import pandas as pd
import mysql.connector as sql



def add_server(msg,time,group):

    connection = sql.connect(
    host = "127.0.0.1",
    user="root",
    password='add your code',
    auth_plugin = "mysql_native_password"
    
    )
    cursor = connection.cursor("SELECT * FROM my_schema.table")
    text = "INSERT INTO `my_schema`.`table` (`message`, `time`, `group`) VALUES ('{}', '{}', '{}');".format(msg,time,group)
    cursor.execute(text)
    connection.commit()
    table = pd.read_sql_query("SELECT * FROM my_schema.table",connection)
    cursor.close()
    connection.close()
    return table
