import kivy
kivy.require("1.11.1")
from kivy.app import App
from kivy.uix.button import Button, Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image


class GUI(App):
    def build(self):
        self.title = "R\u00b2-Analysis"
        self.icon = "../Images/Logo.png"

        layout = GridLayout(cols=2)
        layout.add_widget(Button(text="First"))
        layout.add_widget(Button(text="Second"))
        layout.add_widget(Button(text="Third"))
        layout.add_widget(Button(text="Forth"))
        return layout

gui = GUI()
gui.run()
