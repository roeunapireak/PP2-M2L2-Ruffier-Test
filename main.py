from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
# from kivy.core.window import Window
# from kivy.uix.scrollview import ScrollView
from instr import txt_instruction #, txt_test1, txt_test2, txt_test3, txt_sits
# from ruffier import test


class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instruction = Label(text=txt_instruction)

        lbl1 = Label(text='Enter the name:', halign='right')
        lbl2 = Label(text='Enter the age:', halign='right')

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')

        line1.add_widget(lbl1)
        self.in_name = TextInput(multiline=False) # create in_name property to keyword argument
        line1.add_widget(self.in_name) 
        
        line2.add_widget(lbl2)
        self.in_age = TextInput(text='7', multiline=False) # create in_age property to keyword argument
        line2.add_widget(self.in_age) 

        self.btn = Button(text='Start', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.press_next

        layout = BoxLayout(orientation='vertical', padding=8, spacing=8)
        layout.add_widget(instruction)
        layout.add_widget(line1)
        layout.add_widget(line2)

        layout.add_widget(self.btn)

        self.add_widget(layout)

    def press_next(self):
        print('next is pressed!')


class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='instr'))

        return sm


app = HeartCheck()
app.run()
