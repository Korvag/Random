from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class userPass(App):

    def getPass(self,event):
        passwd = self.password.text
        if passwd == 'password':
            self.passRequest.text = "Correct!"

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6,0.7)
        self.window.pos_hint = {"center_x":0.5,"center_y":0.5}
        self.window.add_widget(Image(source = "fire.jpg"))

        self.passRequest = Label(
            text = "Enter your password:  ",
            font_size = 30,
            color = "#ffffff",
            bold = True
        )
        self.window.add_widget(self.passRequest)

        self.password = TextInput(
            multiline = False,
            padding_y=(30,30),
            size_hint=(1,0.7),
            font_size = (12)
            
        )
        self.window.add_widget(self.password)

        self.button = Button(
            text = "Enter password",
            size_hint = (0.5,0.5),
            bold = True,
            font_size = 20
        )
        self.button.bind(on_press = self.getPass)
        self.window.add_widget(self.button)
        return self.window
    
if __name__ == "__main__":
    userPass().run()