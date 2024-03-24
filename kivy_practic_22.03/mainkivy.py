from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.progressbar import ProgressBar
from kivy.uix.filechooser import FileChooserListView








class MainPage(Screen):
    def __init__(self, name="first"):
        super().__init__(name=name)
        btn1 = Button(text='Перший блок(CheckBox + TexInput) (Галочка + Введення тексту)')
        btn1.on_press = self.next1
        btn2 = Button(text='Другий блок(Label + Image)(рандом фото і текст)')
        btn2.on_press = self.next2
        btn3 = Button(text= 'Третій блок(ColorPicker +ToggleButton) (палітра кольрів + перемикач )')
        btn3.on_press = self.next3
        btn4 = Button(text='Четвертий блок(ProgressBar + FileChoose) (Смуга прогресу + обирач файлів )')
        btn4.on_press = self.next4

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        self.add_widget(layout)

    def next1(self):
        self.manager.transition.direction = "up"
        one_screen = ButtonOneScreen()
        one_screen.on_return = self.return_to_main
        self.manager.add_widget(one_screen)
        self.manager.current = "subscreen"

    def next2(self):
        self.manager.transition.direction = "up"
        two_screen = ButtonTwoScreen()
        two_screen.on_return = self.return_to_main
        self.manager.add_widget(two_screen)
        self.manager.current = "subscreen"

    def next3(self):
        self.manager.transition.direction = "up"
        third_screen = ButtonThirdScreen()
        third_screen.on_return = self.return_to_main
        self.manager.add_widget(third_screen)
        self.manager.current = "subscreen"
        
    def next4(self):
        self.manager.transition.direction = "up"
        four_screen = ButtonFourScreen()
        four_screen.on_return = self.return_to_main
        self.manager.add_widget(four_screen)
        self.manager.current = "subscreen"

    def return_to_main(self):
        self.manager.remove_widget(self.manager.current_screen)
        self.manager.current = "first"


class ButtonOneScreen(Screen):
    def __init__(self, name="subscreen"):
        super().__init__(name=name)
        btn_back = Button(text='Вернутися до вибору(головного меню)')
        btn_back.on_press = self.go_back
        cb1 = CheckBox()
        tex_input = TextInput(text = "Введіть бажаний текс:?")
        cb2 = CheckBox()
       
        

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(btn_back)
        layout.add_widget(cb1)
        layout.add_widget(tex_input)
        

        self.add_widget(layout)

    def go_back(self):
        if hasattr(self, 'on_return'):
            self.on_return()
            
class ButtonTwoScreen(Screen):
    def __init__(self, name="subscreen"):
        super().__init__(name=name)
        btn_back = Button(text= "Вернутися до вибору (головного меню)")
        btn_back.on_press = self.go_back
        label = Label(text="Рандом текст")
        self.button = Button()
        self.button.background_normal = "images/image.png"


        layout = BoxLayout(orientation="vertical")
        layout.add_widget(btn_back)
        layout.add_widget(label)
        layout.add_widget(self.button)

        self.add_widget(layout)

    def go_back(self):
        if hasattr(self, 'on_return'):
            self.on_return()



class ButtonThirdScreen(Screen):
    def __init__(self, name="subscreen"):
        super().__init__(name=name)
        btn_back = Button(text='Вернутися до вибору (головного меню)')
        btn_back.on_press = self.go_back
        
        color_picker = ColorPicker()
        toggle_button = ToggleButton(text='ToggleButton (Перемикач): Дозволяє вибирати між двома станами (увімкнено/вимкнено)')
        
        
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(btn_back)
        layout.add_widget(color_picker)
        layout.add_widget(toggle_button)
        
        

        self.add_widget(layout)

    def go_back(self):
        if hasattr(self, 'on_return'):
            self.on_return()
    
class ButtonFourScreen(Screen):
    def __init__(self, name="subscreen"):
        super().__init__(name=name)
        btn_back = Button(text='Вернутися до вибору (головного меню)')
        btn_back.on_press = self.go_back
        
        progress_bar = ProgressBar(max=100)
        progress_bar.value = 50   #смуга прогресу, тут потрібно ввести цифру від 0 до 100, щоб виміряти свій прогресс
        
        file_chooser = FileChooserListView()
        def selected(file_chooser, selection):
            print("Selected:", selection)

        file_chooser.bind(selection=selected)

    
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(btn_back)
        layout.add_widget(progress_bar)
        layout.add_widget(file_chooser)
        
        

        self.add_widget(layout)
        
    def go_back(self):
        if hasattr(self, 'on_return'):
            self.on_return()
       
    
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainPage())
        return sm


if __name__ == '__main__':
    MyApp().run()
