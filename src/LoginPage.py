from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window

global_user = ""


class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password.text != "":
                file_append = open("DB/Users.txt", "a")
                print(self.namee.text.strip())
                new_str = self.namee.text + " " + self.email.text + " " + self.password.text + "\n"
                file_append.write(new_str)
                file_append.close();

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
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):

        print(self.password.text)

        file_read = open("DB/Users.txt", "r")
        strr = file_read.readlines()
        file_read.close();
        flag = 0
        for s_str in strr:
            strList = s_str.split()
            if(self.email.text==strList[1] and self.password.text==strList[2]):
                global_user = self.email.text
                flag = 1
                break

        if(flag == 0):
            popup = Popup(title='Oops!',
                          content=Label(text='"No such user"'),
                          size_hint=(None, None), size=(600, 400))
            popup.open()
        else:
            sm.current = "main"

    def BackBtn(self):
        sm.current = "init"


    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):

    def logOut(self):
        global_user = ""
        sm.current = "login"


class InitWindow(Screen):

    btn1 = ObjectProperty(None)
    btn2 = ObjectProperty(None)

    def actBtn1(self):

        sm.current = "login"

    def actBtn2(self):

        sm.current = "create"


class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("wew.kv")

sm = WindowManager()

screens = [InitWindow(name="init"),LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "init"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()