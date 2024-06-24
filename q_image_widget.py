import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.image import Image

class MyApp(App):
    def build(self):
        return Image(source='baixados.jpeg')

MyApp().run()