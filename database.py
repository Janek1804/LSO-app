import  mysql.connector
from datetime import datetime

db_connect=mysql.connector.connect(user="root", password="root", database="count", host="localhost")
db_cursor=db_connect.cursor()
now = datetime.now()

print("Current time=",now)
m=now.strftime("%B")
if now.day==1:
    db_cursor.execute(f"CREATE TABLE {m}"
     "pk int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY"
     "Imię varchar(255)")
