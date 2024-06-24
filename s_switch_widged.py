import kivy
from kivy.app import App
from kivy.uix.switch import Switch
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class SimpleSwitch(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text='Switch'))

        self.settings_sample = Switch(active= False)
        self.add_widget(self.settings_sample)

class SwitchApp(App):
    def build(self):
        return SimpleSwitch()

if __name__ == '__main__':
    SwitchApp().run()