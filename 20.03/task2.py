from kivy.app import App
from kivy.uix.button import Button

class Myapp(App):
    def buld(self):
        btn = Button(text='This is BUTTON!!!')
        return btn
    


Myapp().run()