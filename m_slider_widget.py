import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.properties import NumericProperty

class WidgetContainer(GridLayout):
    def __init__(self, **kwargs):
        super(WidgetContainer, self).__init__(**kwargs)
        self.cols = 4
        self.brightnessControl = Slider(min = 0, max=100)

        self.add_widget(Label(text='brightness'))
        self.add_widget(self.brightnessControl)

        self.add_widget(Label(text='Slider Value'))
        self.brightnessValue = Label(text='0')
        self.add_widget(self.brightnessValue)

        self.brightnessControl.bind(value = self.on_value)

    def on_value(self, instance, brightness):
        self.brightnessValue.text = '% d'% brightness

class SliderExample(App):
    def build(self):
        widgetContainer = WidgetContainer()
        return widgetContainer

root = SliderExample()

root.run()

