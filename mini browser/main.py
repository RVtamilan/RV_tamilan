from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.popup import Popup
from wikipedia import *
from pyttsx3 import *
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

from kivy.uix.screenmanager import *
Config.set('graphics', 'resizable', True)
Config.write()

Window.size =(500,550)


Builder.load_string("""
<page1>
     txt:txt
     FloatLayout:
          canvas.before:
               Color :
                    rgba :(1,1,1,1)
               Rectangle :
                    source : "i2.jpg"
                    size : root.width,root.height
                    pos : self.pos
     
          Label:
               text:"Search Answers For Your Questions Here:"
               color:0,1,1,1
               font_size : '18sp'
               pos : 120,400
          TextInput:
               id : txt
               pos : 80,390
               size_hint : 3,.4
          Button:
               text:"Search"
               size_hint : .8,.3
               pos : 300,350
               on_press:
                    root.press()
                    root.press1()
                    
""")


                    
class page1 (Widget):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
     txt = ObjectProperty(None)
     def press(self):
          global result
          layout = GridLayout(cols = 1, padding = 10)
          text = self.txt.text
          result = summary(text,sentences = 2)
          l2 = Label(text = result,halign ="justify",valign = "center",
                     text_size=(self.width-210,self.height))
          bt = Button(text = "Close",size_hint_y =None,height = 80)
          layout.add_widget(l2)
          layout.add_widget(bt)
          popup = Popup(title = "output",
                        content = layout,
                        size_hint=(None,None),size = (400,500))
          popup.open()
          bt.bind(on_press = popup.dismiss)
     def press1(self):
          engine = init()
          engine.setProperty('rate',150)
          voices = engine.getProperty('voices')
          engine.setProperty('voice',voices[11].id)
          engine.say(result)
          engine.runAndWait()
          engine.stop()
class main(App):
    def build(self):
         return page1()

main().run()