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
    
    def __init__(self):
        self.builtins = {}
        self.builtins.update(__builtins__)
        self.builtins.update({"Decimal":decimal.Decimal})
        self.builtins.update(units.__dict__)
        self.builtins.update(elements.element_dict)
        self.builtins['Mol'] = elements.Molecule
        self.builtins['chemeq'] = elements.chemeq

    def can_split(self, symbol):
        if re.match(r'(([A-Z][a-z]?[a-z]?)([0-9]*))+', symbol):
            return False
        elif symbol in self.builtins:
            return False
        else:
            return _token_splittable(symbol)

    def run_cmd(self, cmd):
        m = re.match(r'(?:(\w+) *=)([^=].*)', cmd.strip())
        if(m):
            var = m.group(1)
            text = m.group(2)
        else:
            var = None
            text = cmd
        ans = parse_expr(text, local_dict=self.builtins, transformations=standard_transformations+(split_symbols_custom(self.can_split), implicit_multiplication, implicit_application, function_exponentiation, ))
        if var is not None:
            self.builtins[var] = ans
        self.builtins['ans'] = ans
        return ans
