from datetime import datetime
import  mysql.connector

db_connect=mysql.connector.connect(user="root", password="root", database="count", host="localhost")
db_cursor=db_connect.cursor()
now = datetime.now()
def insert(table, pk,Imię,hasło):
    db_cursor.execute(f"INSERT INTO {table} (pk,FullName,Password)"
    "VALUES ({pk},{Imię},{hasło})")
class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        #select
        self.users = {}

        for line in self.file:
            email, password, name, created = line.strip().split(";")
            self.users[email] = (password, name, created)

        self.file.close()

    def get_user(self, name):
        if email in self.users:
            return self.users[name]
        else:
            return -1

    def add_user(self, password, name):
        a=0
        if name.strip() not in self.users:
            self.users[name.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            
            a+=1
            insert(a,name,password)
            return 1
        else:
            print("Email exists already")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]


