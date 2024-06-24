import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.base import runTouchApp
from kivy.lang import Builder

Builder.load_string(
'''
#Define the scroll view
<ScrollableLabel>:
    text:'You are leaning kivy' * 500
    Label:
        text: root.text
        font_size=50
        text_size:self.width, None
        size_hint_y = None
        height: self.texture_size[1]
   ''' )

class ScrolLabel(ScrollView):
    text= StringProperty('')

runTouchApp(ScrolLabel())