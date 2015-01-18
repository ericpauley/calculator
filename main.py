import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
import re
from kivy.config import Config 
import calculator

Config.set('graphics', 'width', '500') 
Config.set('graphics', 'height', '700')

calc = calculator.Calculator()

def coloring(matchobj):
    return '[color=009999]' + matchobj.group(0) + '[/color]'

class CalcGUI(Widget):
    pass

class ScrollButton(Button):
    def __init__(self, **kwargs):
        Button.__init__(self, **kwargs)
        self.input = ObjectProperty(None)
        self.bind(on_press=self.callback)
        
    def callback(self, instance):
        if (self.text == 'UP'):
            self.input.scroll_up()
        else:
            self.input.scroll_down()
    
class UserInput(TextInput):
    line1 = ObjectProperty(None)
    line2 = ObjectProperty(None)
    line3 = ObjectProperty(None)
    line4 = ObjectProperty(None)
    line5 = ObjectProperty(None)
    line6 = ObjectProperty(None)
    line7 = ObjectProperty(None)
    line8 = ObjectProperty(None)
    
    lines = [line1, line2, line3, line4, line5, line6, line7, line8]
    input_lines = []
    output_lines =[]
    
    def __init__(self, **kwargs):
        TextInput.__init__(self, **kwargs)
        self.focus = True
    
    def scroll_up(self):
        self.text = "scroll up"
        
    def scroll_down(self):
        self.text = "scroll down"
    
    def on_text_validate(self):
        out = str(calc.run_cmd(self.text))
        input = re.sub('[a-zA-Z]+', coloring, self.text)
        output = re.sub('[a-zA-Z]+', coloring, out)
        self.update_screen(input, output)
        self.text = ""
        Clock.schedule_once(self.refocus)
        
    def update_screen(self, input, output):
        """if len(self.input_lines) >= 4:
            self.input_lines.pop(0)
            self.output_lines.pop(0)
        self.input_lines.append(self.text)
        self.output_lines.append(output)
        i = 0
        for line in self.lines:
            if i%2 == 0:            #an input line
                line.text = self.input_lines[int(i/2)]
            else:                   #an output line
                line.text = self.output_lines[int(i/2)]
            i += 1"""
            
        if len(self.input_lines) >= 4:
            self.input_lines.pop(0)
            self.output_lines.pop(0)
        self.input_lines.append(input)
        self.output_lines.append(output)
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
