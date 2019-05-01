from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.core.window import Window

from src import load_data
from src import style_selector

global_user = ""
curr_layer = ""

skin_color = (0.0, 0.0, 0.0, 1.0)
mouth_style = 0
hair_style = 0
hair_color = (0.0, 0.0, 0.0, 1.0)
back_color = (0.0, 0.0, 0.0, 1.0)
beard_style = 0
beard_color = (0.0, 0.0, 0.0, 1.0)
eyes_style = 0
eyes_color = (0.0, 0.0, 0.0, 1.0)



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

    gallery = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MainWindow,self).__init__(**kwargs)

        '''
        file_read = open("DB/User_Image.txt", "r")
        strr = file_read.readlines()
        file_read.close();
        collention = list()
        for curr_str in strr:
            strList = curr_str.split()
            if(strList[0] == global_user):
                collention.add(strList[1])
        '''

        for i in range(5):
            self.gallery.add_widget(Button(background_normal = "temp.png"))

        '''for curr_str in collention:
            dir = "Collections/" + curr_str + ".csv"

            #create temp.png from data

            self.gallery.add_widget(AsyncImage(source="temp.png"))'''

    def createNew(self):
        #implement create window
        return 0

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

class WorkshopWindow(Screen):

    hair = ObjectProperty(None)
    skin = ObjectProperty(None)
    mouth = ObjectProperty(None)
    beard = ObjectProperty(None)
    back = ObjectProperty(None)
    eyes = ObjectProperty(None)
    style = ObjectProperty(None)
    preview = ObjectProperty(None)
    img_name = ObjectProperty(None)
    colorPicker = ObjectProperty(None)
    colorPickerLabel = ObjectProperty(None)
    colorSelectorButton = ObjectProperty(None)
    colorPickerBox = ObjectProperty(None)
    colorLabel = ObjectProperty(None)
    styleLabel = ObjectProperty(None)
    styleBox = ObjectProperty(None)
    box1 = ObjectProperty(None)
    box2 = ObjectProperty(None)
    box3 = ObjectProperty(None)
    box4 = ObjectProperty(None)
    box5 = ObjectProperty(None)
    box6 = ObjectProperty(None)

    layerList = list()
    layerList.append(hair)
    layerList.append(skin)
    layerList.append(mouth)
    layerList.append(beard)
    layerList.append(back)
    layerList.append(eyes)

    def __init__(self, **kwargs):
        super(WorkshopWindow,self).__init__(**kwargs)
        self.hair.color = (0.8, 0.8, 0.0, 1.0)
        self.skin.color = (0.8, 0.8, 0.0, 1.0)
        self.mouth.color = (0.8, 0.8, 0.0, 1.0)
        self.beard.color = (0.8, 0.8, 0.0, 1.0)
        self.back.color = (0.8, 0.8, 0.0, 1.0)
        self.eyes.color = (0.8, 0.8, 0.0, 1.0)



        #implement initial state

    #implement buttons

    def Shair(self, instance):
        self.box1.background_normal = ""
        self.box1.background_color = (1.0, 0, 0.0, 1.0)

        self.box2.background_normal = ""
        self.box2.background_color = (0.0, 1.0, 0.0, 1.0)

        self.box3.background_normal = ""
        self.box3.background_color = (0.0, 0.0, 1.0, 1.0)

        self.box4.background_normal = ""
        self.box4.background_color = (1.0, 1.0, 0.0, 1.0)

        self.box5.background_normal = ""
        self.box5.background_color = (1.0, 0.0, 1.0, 1.0)

        self.box6.background_normal = ""
        self.box6.background_color = (0.0, 1.0, 1.0, 1.0)

        self.colorPicker.opacity = 1
        self.colorPickerLabel.opacity = 1
        self.colorSelectorButton.opacity = 1
        self.colorPickerBox.opacity = 1
        self.colorLabel.opacity = 1
        self.styleLabel.opacity = 1
        self.styleBox.opacity = 1

        curr_layer = "hair"
        self.hair.background_normal = ""
        self.hair.background_color = (0.8, 0.8, 0.0, 1.0)
        self.hair.color = (0.3412, 0.2392, 0.3451, 1)

        self.skin.background_normal = ""
        self.skin.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.skin.color = (0.8, 0.8, 0.0, 1.0)

        self.mouth.background_normal = ""
        self.mouth.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.mouth.color = (0.8, 0.8, 0.0, 1.0)

        self.beard.background_normal = ""
        self.beard.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.beard.color = (0.8, 0.8, 0.0, 1.0)

        self.back.background_normal = ""
        self.back.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.back.color = (0.8, 0.8, 0.0, 1.0)

        self.eyes.background_normal = ""
        self.eyes.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.eyes.color = (0.8, 0.8, 0.0, 1.0)

        for i in range(3):
            bubutton = Button(background_normal="temp.png", id = str(i), on_press = self.find_style)
            self.style.add_widget(bubutton)

    def Sskin(self, instance):
        self.box1.background_normal = ""
        self.box1.background_color = (1.0, 0, 0.0, 1.0)

        self.box2.background_normal = ""
        self.box2.background_color = (0.0, 1.0, 0.0, 1.0)

        self.box3.background_normal = ""
        self.box3.background_color = (0.0, 0.0, 1.0, 1.0)

        self.box4.background_normal = ""
        self.box4.background_color = (1.0, 1.0, 0.0, 1.0)

        self.box5.background_normal = ""
        self.box5.background_color = (1.0, 0.0, 1.0, 1.0)

        self.box6.background_normal = ""
        self.box6.background_color = (0.0, 1.0, 1.0, 1.0)

        self.colorPicker.opacity = 1
        self.colorPickerLabel.opacity = 1
        self.colorSelectorButton.opacity = 1
        self.colorPickerBox.opacity = 1
        self.colorLabel.opacity = 1
        self.styleLabel.opacity = 1
        self.styleBox.opacity = 1

        curr_layer = "skin"

        self.hair.background_normal = ""
        self.hair.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.hair.color = (0.8, 0.8, 0.0, 1.0)

        self.skin.background_normal = ""
        self.skin.background_color = (0.8, 0.8, 0.0, 1.0)
        self.skin.color = (0.3412, 0.2392, 0.3451, 1)

        self.mouth.background_normal = ""
        self.mouth.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.mouth.color = (0.8, 0.8, 0.0, 1.0)

        self.beard.background_normal = ""
        self.beard.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.beard.color = (0.8, 0.8, 0.0, 1.0)

        self.back.background_normal = ""
        self.back.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.back.color = (0.8, 0.8, 0.0, 1.0)

        self.eyes.background_normal = ""
        self.eyes.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.eyes.color = (0.8, 0.8, 0.0, 1.0)

        self.styleLabel.opacity = 0
        self.styleBox.opacity = 0
        self.colorPicker.opacity = 0
        self.colorPickerLabel.opacity = 0
        self.colorSelectorButton.opacity = 0

        self.box1.background_normal = ""
        self.box1.background_color = (0.9686, 0.851, 0.8196, 1.0)

        self.box2.background_normal = ""
        self.box2.background_color = (0.9, 0.8, 0.76, 1.0)

        self.box3.background_normal = ""
        self.box3.background_color = (0.83, 0.73, 0.69, 1.0)

        self.box4.background_normal = ""
        self.box4.background_color = (0.76, 0.66, 0.62, 1.0)

        self.box5.background_normal = ""
        self.box5.background_color = (0.69, 0.59, 0.55, 1.0)

        self.box6.background_normal = ""
        self.box6.background_color = (0.62, 0.52, 0.48, 1.0)


    def Smouth(self, instance):
        self.box1.background_normal = ""
        self.box1.background_color = (1.0, 0, 0.0, 1.0)

        self.box2.background_normal = ""
        self.box2.background_color = (0.0, 1.0, 0.0, 1.0)

        self.box3.background_normal = ""
        self.box3.background_color = (0.0, 0.0, 1.0, 1.0)

        self.box4.background_normal = ""
        self.box4.background_color = (1.0, 1.0, 0.0, 1.0)

        self.box5.background_normal = ""
        self.box5.background_color = (1.0, 0.0, 1.0, 1.0)

        self.box6.background_normal = ""
        self.box6.background_color = (0.0, 1.0, 1.0, 1.0)

        self.colorPicker.opacity = 1
        self.colorPickerLabel.opacity = 1
        self.colorSelectorButton.opacity = 1
        self.colorPickerBox.opacity = 1
        self.colorLabel.opacity = 1
        self.styleLabel.opacity = 1
        self.styleBox.opacity = 1

        curr_layer = "mouth"
        self.hair.background_normal = ""
        self.hair.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.hair.color = (0.8, 0.8, 0.0, 1.0)

        self.skin.background_normal = ""
        self.skin.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.skin.color = (0.8, 0.8, 0.0, 1.0)

        self.mouth.background_normal = ""
        self.mouth.background_color = (0.8, 0.8, 0.0, 1.0)
        self.mouth.color = (0.3412, 0.2392, 0.3451, 1)

        self.beard.background_normal = ""
        self.beard.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.beard.color = (0.8, 0.8, 0.0, 1.0)

        self.back.background_normal = ""
        self.back.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.back.color = (0.8, 0.8, 0.0, 1.0)

        self.eyes.background_normal = ""
        self.eyes.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.eyes.color = (0.8, 0.8, 0.0, 1.0)

        self.colorPicker.opacity = 0
        self.colorPickerLabel.opacity = 0
        self.colorSelectorButton.opacity = 0
        self.colorPickerBox.opacity = 0
        self.colorLabel.opacity = 0

        for i in range(3):
            bubutton = Button(background_normal="temp.png", id = str(i), on_press = self.find_style)
            self.style.add_widget(bubutton)

    def Sbeard(self, instance):
        self.box1.background_normal = ""
        self.box1.background_color = (1.0, 0, 0.0, 1.0)

        self.box2.background_normal = ""
        self.box2.background_color = (0.0, 1.0, 0.0, 1.0)

        self.box3.background_normal = ""
        self.box3.background_color = (0.0, 0.0, 1.0, 1.0)

        self.box4.background_normal = ""
        self.box4.background_color = (1.0, 1.0, 0.0, 1.0)

        self.box5.background_normal = ""
        self.box5.background_color = (1.0, 0.0, 1.0, 1.0)

        self.box6.background_normal = ""
        self.box6.background_color = (0.0, 1.0, 1.0, 1.0)

        self.colorPicker.opacity = 1
        self.colorPickerLabel.opacity = 1
        self.colorSelectorButton.opacity = 1
        self.colorPickerBox.opacity = 1
        self.colorLabel.opacity = 1
        self.styleLabel.opacity = 1
        self.styleBox.opacity = 1

        curr_layer = "beard"

        self.hair.background_normal = ""
        self.hair.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.hair.color = (0.8, 0.8, 0.0, 1.0)

        self.skin.background_normal = ""
        self.skin.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.skin.color = (0.8, 0.8, 0.0, 1.0)

        self.mouth.background_normal = ""
        self.mouth.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.mouth.color = (0.8, 0.8, 0.0, 1.0)

        self.beard.background_normal = ""
        self.beard.background_color = (0.8, 0.8, 0.0, 1.0)
        self.beard.color = (0.3412, 0.2392, 0.3451, 1)

        self.back.background_normal = ""
        self.back.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.back.color = (0.8, 0.8, 0.0, 1.0)

        self.eyes.background_normal = ""
        self.eyes.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.eyes.color = (0.8, 0.8, 0.0, 1.0)

        for i in range(3):
            bubutton = Button(background_normal="temp.png", id = str(i), on_press = self.find_style)
            self.style.add_widget(bubutton)

    def Sback(self, instance):
        self.box1.background_normal = ""
        self.box1.background_color = (1.0, 0, 0.0, 1.0)

        self.box2.background_normal = ""
        self.box2.background_color = (0.0, 1.0, 0.0, 1.0)

        self.box3.background_normal = ""
        self.box3.background_color = (0.0, 0.0, 1.0, 1.0)

        self.box4.background_normal = ""
        self.box4.background_color = (1.0, 1.0, 0.0, 1.0)

        self.box5.background_normal = ""
        self.box5.background_color = (1.0, 0.0, 1.0, 1.0)

        self.box6.background_normal = ""
        self.box6.background_color = (0.0, 1.0, 1.0, 1.0)

        self.colorPicker.opacity = 1
        self.colorPickerLabel.opacity = 1
        self.colorSelectorButton.opacity = 1
        self.colorPickerBox.opacity = 1
        self.colorLabel.opacity = 1
        self.styleLabel.opacity = 1
        self.styleBox.opacity = 1

        curr_layer = "back"

        self.hair.background_normal = ""
        self.hair.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.hair.color = (0.8, 0.8, 0.0, 1.0)

        self.skin.background_normal = ""
        self.skin.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.skin.color = (0.8, 0.8, 0.0, 1.0)

        self.mouth.background_normal = ""
        self.mouth.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.mouth.color = (0.8, 0.8, 0.0, 1.0)

        self.beard.background_normal = ""
        self.beard.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.beard.color = (0.8, 0.8, 0.0, 1.0)

        self.back.background_normal = ""
        self.back.background_color = (0.8, 0.8, 0.0, 1.0)
        self.back.color = (0.3412, 0.2392, 0.3451, 1)

        self.eyes.background_normal = ""
        self.eyes.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.eyes.color = (0.8, 0.8, 0.0, 1.0)

        self.styleLabel.opacity = 0
        self.styleBox.opacity = 0

    def Seyes(self, instance):
        self.box1.background_normal = ""
        self.box1.background_color = (1.0, 0, 0.0, 1.0)

        self.box2.background_normal = ""
        self.box2.background_color = (0.0, 1.0, 0.0, 1.0)

        self.box3.background_normal = ""
        self.box3.background_color = (0.0, 0.0, 1.0, 1.0)

        self.box4.background_normal = ""
        self.box4.background_color = (1.0, 1.0, 0.0, 1.0)

        self.box5.background_normal = ""
        self.box5.background_color = (1.0, 0.0, 1.0, 1.0)

        self.box6.background_normal = ""
        self.box6.background_color = (0.0, 1.0, 1.0, 1.0)

        self.colorPicker.opacity = 1
        self.colorPickerLabel.opacity = 1
        self.colorSelectorButton.opacity = 1
        self.colorPickerBox.opacity = 1
        self.colorLabel.opacity = 1
        self.styleLabel.opacity = 1
        self.styleBox.opacity = 1

        curr_layer = "eyes"

        self.hair.background_normal = ""
        self.hair.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.hair.color = (0.8, 0.8, 0.0, 1.0)

        self.skin.background_normal = ""
        self.skin.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.skin.color = (0.8, 0.8, 0.0, 1.0)

        self.mouth.background_normal = ""
        self.mouth.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.mouth.color = (0.8, 0.8, 0.0, 1.0)

        self.beard.background_normal = ""
        self.beard.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.beard.color = (0.8, 0.8, 0.0, 1.0)

        self.back.background_normal = ""
        self.back.background_color = (0.3412, 0.2392, 0.3451, 1)
        self.back.color = (0.8, 0.8, 0.0, 1.0)

        self.eyes.background_normal = ""
        self.eyes.background_color = (0.8, 0.8, 0.0, 1.0)
        self.eyes.color = (0.3412, 0.2392, 0.3451, 1)

        for i in range(3):
            bubutton = Button(background_normal="temp.png", id = str(i), on_press = self.find_style)
            self.style.add_widget(bubutton)

    def colorBox1(self, instance):
        mod_color = instance.background_color
        upd_color(mod_color)

        img_reload()

    def colorBox2(self, instance):
        mod_color = instance.background_color
        upd_color(mod_color)
        img_reload()

    def colorBox3(self, instance):
        mod_color = instance.background_color
        upd_color(mod_color)
        img_reload()

    def colorBox4(self, instance):
        mod_color = instance.background_color
        upd_color(mod_color)
        img_reload()

    def colorBox5(self, instance):
        mod_color = instance.background_color
        upd_color(mod_color)
        img_reload()

    def colorBox6(self, instance):
        mod_color = instance.background_color
        upd_color(mod_color)
        img_reload()

    def colorSelected(self):
        pass

    def find_style(self, instance):
        if curr_layer == "hair":
            hair_style = instance.id

        if curr_layer == "mouth":
            mouth_style = instance.id

        if curr_layer == "beard":
            beard_style = instance.id

        if curr_layer == "eyes":
            eyes_style = instance.id

    def upd_color(self, cocolor):

        if curr_layer == "hair":
            hair_color = cocolor
        if curr_layer == "beard":
            beard_color = cocolor
        if curr_layer == "eyes":
            eyes_color = cocolor
        if curr_layer == "back":
            back_color = cocolor

class SaveWindow(Screen):

    def __init__(self, **kwargs):
        super(SaveWindow,self).__init__(**kwargs)

        #implement initial state

    #implement buttons

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

def img_reload():
    blueprint_data = load_data.get_data()
    style_selector.generate(blueprint_data, skin_color, mouth_style, hair_style, hair_color, back_color, beard_style, beard_color, eyes_color, eyes_style)


kv = Builder.load_file("wew.kv")

sm = WindowManager()

screens = [SaveWindow(name="save"), WorkshopWindow(name="work"),InitWindow(name="init"),LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "work"


class MyMainApp(App):
    def build(self):
        return sm