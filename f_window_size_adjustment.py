from kivy.config import Config
Config.set('graphics', 'resizable', True)
import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyLabelApp(App):
    def build(self):
        l2= Label(text='[color=ff3333][b]Hello !!!!!!!!!!![/b][/color]\n[color=3333ff]GFG !!:):):)[/color]', font_size='20sp', markup=True)
        return l2
label = MyLabelApp()
label.run()
