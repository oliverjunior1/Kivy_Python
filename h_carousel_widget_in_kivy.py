import kivy
from kivy.app import App
from kivy.uix.image import AsyncImage
from kivy.uix.carousel import Carousel

class CasouselApp(App):
    def build(self):

        casousel = Carousel(direction='right')

        for i in range(10):
            src = 'http://placehold.it/480x270.png&text = slide-%d&.png' %i

            image = AsyncImage(source = src, alow_stretch = True)
            casousel.add_widget(image)
        return casousel

CasouselApp().run()