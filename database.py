import  mysql.connector
from datetime import datetime

db_connect=mysql.connector.connect(user="root", password="root", database="count", host="localhost")
db_cursor=db_connect.cursor()
now = datetime.now()

print("Current time=",now)

if now.day==1:
    db_cursor.execute(f"CREATE TABLE ")
