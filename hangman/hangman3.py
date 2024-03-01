from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput


class HangmanGame(Widget):
    def on_enter(instance,value):
        print('User pressed enter in', instance)
    textinput = TextInput(text='Hello World',multiline=False,focus=True)
    textinput.bind(on_text_validate=on_enter)

class HangmanApp(App):
    def build(self):
        return HangmanGame()
    

if __name__ == '__main__':
    HangmanApp().run()