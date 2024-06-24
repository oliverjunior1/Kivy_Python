from kivy.config import Config
Config.set('graphics', 'resizable', True)
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.floatlayout import FloatLayout

class SpinnerExample(App):
    def build(self):
        layout = FloatLayout()
        self.spinnerObject = Spinner(text = 'Python', values = ('Python', 'Java', 'C++', 'C', 'C#', 'PHP'), background_color=(0.784,0.443,0.216,1))
        self.spinnerObject.size_hint=(0.3,0.2)
        self.spinnerObject.pos_hint = {'x': .35, 'y':.75}
        layout.add_widget(self.spinnerObject)
        return layout;

if __name__ == '__main__':
    SpinnerExample().run()
