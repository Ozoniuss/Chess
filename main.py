from kivy.app import App
from kivy.uix.button import Button

class Gui(App):
    def build(self):
        return Button(text='Muie.')

if __name__=='__main__':
    Gui().run()