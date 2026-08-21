from kivy.app import App
from kivy.uix.label import Label

class GreenBook(App):
    def build(self):
        return Label(text="Welcome to GreenBook")

GreenBook().run()
