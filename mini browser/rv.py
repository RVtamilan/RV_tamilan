import wikipedia 
result = wikipedia.summary("sundar pichai",sentences = 2)
print(result)
from pyttsx3 import *
engine = init()
engine.setProperty('rate',150)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[11].id)
engine.say(result)
engine.runAndWait()
engine.stop()
"""
<page1>:
    
    FloatLayout:
        canvas.before:
            Color :
                rgba :(1,1,1,1)
            Rectangle :
                source : "i2.jpg"
                size : root.width,root.height
                pos : self.pos
        Label:
            text:"Search The Answers For Your Qusetions Here:"
            size_hint : .3,.5
            pos_hint : {'x':.2,'y':.6}
            font_size : '20sp'
            color : 0,1,1,1
        TextInput:
            id : txt
            size_hint : .65,.1
            pos_hint : {'x':.2,'y': .7}
        Button :
            text : "Search"
            size_hint : .15,.05
            pos_hint :{'x':.65,'y':.62}
            border : .15,.05,.15,.05 
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'pagetwo' 
                

    
            
     """
