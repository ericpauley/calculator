import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
import re
from kivy.config import Config 
import calculator

calc = calculator.Calculator()

Config.set('graphics', 'width', '500') 
Config.set('graphics', 'height', '700')

def coloring(matchobj):
    return '[color=009999]' + matchobj.group(0) + '[/color]'

class CalcGUI(Widget):
    pass

# Opens in-program documentation
class HelpButton(Button):
    def __init__(self, **kwargs):
        Button.__init__(self, **kwargs)
        main = ObjectProperty(None)
        self.bind(on_press=self.callback)
        
    def callback(self, instance):
        popup = Popup(title='Functions:',
            content=Label(text='Display functions here\nTubkid'),
            size_hint=(.5, .5))
        popup.open()

#Allows for scrolling through previous solutions
class ScrollButton(Button):
    def __init__(self, **kwargs):
        Button.__init__(self, **kwargs)
        self.input = ObjectProperty(None)
        self.bind(on_press=self.callback)
        
    def callback(self, instance):
        if (self.direction == 'UP'):
            self.input.scroll_up()
        else:
            self.input.scroll_down()

#Displays the input and allows editing
class UserInput(TextInput):
    line1 = ObjectProperty(None)
    line2 = ObjectProperty(None)
    line3 = ObjectProperty(None)
    line4 = ObjectProperty(None)
    line5 = ObjectProperty(None)
    line6 = ObjectProperty(None)
    line7 = ObjectProperty(None)
    line8 = ObjectProperty(None)
    c = calculator.Calculator()
    
    lines = [line1, line2, line3, line4, line5, line6, line7, line8]
    input_lines = []
    output_lines = []
    before = []
    after = []
    
    def __init__(self, **kwargs):
        TextInput.__init__(self, **kwargs)
        self.focus = True
    
    def scroll_up(self):
        self.text = "scroll up"
        if len(self.before) > 0:
            self.after.append(self.output_lines.pop(3))
            self.after.append(self.input_lines.pop(3))
            self.output_lines.insert(0, self.before.pop(len(self.before)-1))
            self.input_lines.insert(0, self.before.pop(len(self.before)-1))
            self.update_screen()
            
    def scroll_down(self):
        self.text = "scroll down"
        if len(self.after) > 0:
            self.before.append(self.input_lines.pop(0))
            self.before.append(self.output_lines.pop(0))
            self.input_lines.append(self.after.pop(len(self.after)-1))
            self.output_lines.append(self.after.pop(len(self.after)-1))
            self.update_screen()
    
    # Passes lines to the calculator functions for processing
    def on_text_validate(self):
        out = str(calc.run_cmd(self.text))
        input = re.sub('[a-zA-Z]+', coloring, self.text)
        output = re.sub('[a-zA-Z]+', coloring, out)
        self.update_lists(input, output)
        self.update_screen()
        self.text = ""
        Clock.schedule_once(self.refocus)
        
    def update_lists(self, input, output):
        if len(self.input_lines) >= 4:
            self.before.append(self.input_lines.pop(0))
            self.before.append(self.output_lines.pop(0))
        self.input_lines.append(input)
        self.output_lines.append(output)
        
    #Shifts screen lines for rendering
    def update_screen(self):
        i = 0
        if len(self.input_lines) > 0:   
            self.line1.text = self.input_lines[int(i/2)]
        i += 1
        if len(self.output_lines) > 0:
            self.line2.text = self.output_lines[int(i/2)]
        i += 1
        if len(self.input_lines) > 1:
            self.line3.text = self.input_lines[int(i/2)]
        i += 1
        if len(self.output_lines) > 1:
            self.line4.text = self.output_lines[int(i/2)]
        i += 1
        if len(self.input_lines) > 2:   
            self.line5.text = self.input_lines[int(i/2)]
        i += 1
        if len(self.output_lines) > 2:
            self.line6.text = self.output_lines[int(i/2)]
        i += 1
        if len(self.input_lines) > 3:
            self.line7.text = self.input_lines[int(i/2)]
        i += 1
        if len(self.output_lines) > 3:
            self.line8.text = self.output_lines[int(i/2)]

    def refocus(self,*args):
        self.focus = True
       
class CalcApp(App):
    def build(self):
        app = CalcGUI()
        return app

if __name__ == '__main__':
    CalcApp().run()
