from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from datetime import datetime
import  mysql.connector

db_connect=mysql.connector.connect(user="root", password="root", database="count", host="localhost")
db_cursor=db_connect.cursor()
now = datetime.now()
def select(table):
    db_cursor.execute(f"SELECT pk,FullName,Password FROM {table}")
    
    
        
def insert(table, pk,Imię,hasło):
    db_cursor.execute(f"INSERT INTO {table} (pk,FullName,Password)"
    f"VALUES ({pk},{Imię},{hasło})")
    db_connect.commit()
class DataBase:
    def __init__(self):
        db_cursor.execute("CREATE TABLE if not exists AppUsers("
            "pk int NOT NULL AUTO_INCREMENT PRIMARY KEY,"
            "FullName varchar(255),"
            "Password varchar(255));")
        db_connect.commit()
        self.users = []
        self.load()

    def load(self):
        select("users")
        records = db_cursor.fetchall()
        print(records)
        

        

     

    def get_user(self, name):
        if name in self.users:
            return self.users[name]
        else:
            return -1

    def add_user(self, password, name):
        a=0
        if name.strip() not in self.users:
            self.users[name.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            
            a+=1
            insert("users",a,name,password)
            return 1
        else:
            print("Email exists already")
            return -1

    def validate(self, name, password):
        if self.get_user(name) != -1:
            return self.users[name][0] == password
        else:
            return False

    

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]

class CreateAccountWindow(Screen):
    name = ObjectProperty(None)
    
    password = ObjectProperty(None)

    def submit(self):
        if self.name != "":
            if self.password != "":
                db.add_user( self.password, self.name)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        
        self.password = ""
        self.name = ""


class LoginWindow(Screen):
    name = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.name, self.password):
            MainWindow.current = self.name
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.name = ""
        self.password = ""


class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.created.text = "Created On: " + created


class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Błędny Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Brak Informacji',
                  content=Label(text='Proszę wypełnić wszystkie pola formularza.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase()

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()


