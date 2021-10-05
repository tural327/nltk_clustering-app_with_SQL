from flask import Flask,render_template,request
import pandas as pd
import mysql.connector as sql
from main import my_group
import datetime
from server import add_server

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])


def calculate():
    sheet = ""
    if request.method == "POST" and "msg" in request.form:
        my_text = str(request.form.get("msg"))
        result = len(my_text)
        if result >0:
            my_gr = str(my_group(my_text)[0])
            my_time = str(datetime.datetime.now())[:19]
            data = add_server(my_text,my_time,my_gr)
            data.to_csv("data.csv")
            sheet = data.to_html()
        else:
            connection = sql.connect(
            host = "127.0.0.1",
            user="root",
            password='tural123',
            auth_plugin = "mysql_native_password"
            
            )
            cursor = connection.cursor("SELECT * FROM my_schema.table")
            table = pd.read_sql_query("SELECT * FROM my_schema.table",connection)
            connection.close()
            sheet = table.to_html()

    return render_template("index.html",sheet=sheet)



if __name__=="__main__":
  app.run()