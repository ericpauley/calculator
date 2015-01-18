import code
import sys
from astworker import compile_calc
from sympy.parsing.sympy_parser import *
from sympy.parsing.sympy_parser import _token_splittable
import decimal
import elements
from sympy.physics import units
from sympy import *
import re
class Calculator:

    #Create initial variables for calculator
    def __init__(self):
        self.builtins = {}
        #Python builtins
        self.builtins.update(__builtins__)
        #units
        self.builtins.update(units.__dict__)
        #Chemical elements
        self.builtins.update(elements.element_dict)
        #Extra functions
        self.builtins['Mol'] = elements.Molecule
        #Unit override
        self.builtins['u'] = units

    '''
    This fuction checks if a variable is elligible for splitting in sympy
    '''
    def can_split(self, symbol):
        if re.match(r'(([A-Z][a-z]?[a-z]?)([0-9]*))+', symbol):
            return False
        elif symbol in self.builtins:
            return False
        else:
            return _token_splittable(symbol)

    '''
    Accepts a command string and parses it in the current evironment
    '''
    def run_cmd(self, cmd):
        #Parsees for assignment operator (ex: a=2)
        m = re.match(r'(?:(\w+) *=)([^=].*)', cmd.strip())
        if(m):
            var = m.group(1)
            text = m.group(2)
        else:
            var = None
        text = cmd
        try:
            #Parse and evaluate expression
            ans = parse_expr(text, local_dict=self.builtins, transformations=standard_transformations+(split_symbols_custom(self.can_split), implicit_multiplication, implicit_application, function_exponentiation, ))
        except Exception as e:
            return str(e)
        if var is not None:
            #save ans variable for future calculations
            self.builtins[var] = ans
            self.builtins['ans'] = ans
            return ans
