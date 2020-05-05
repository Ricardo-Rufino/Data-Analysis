import kivy
kivy.require("1.11.1")
from kivy.app import App
from kivy.uix.button import Button, Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image


class HomePage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "R\u00b2-Analysis"
        self.icon = "../Images/Logo.png"
        self.cols = 2

        self.add_widget(Button(text="Data Analysis"))
        self.add_widget(Button(text="Second"))
        self.add_widget(Button(text="Third"))
        self.add_widget(Button(text="Website"))


class App(App):
    def build(self):
        return HomePage()


if __name__ == "__main__":
    App().run()

