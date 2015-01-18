import json
import decimal
import sympy.physics.units as u
from sympy.core import AtomicExpr
import re
from sympy.core import Symbol
import sys

try:
    base = sys._MEIPASS+"\\"
except Exception:
    base = ''
raw = json.load(open(base+"elements.json"), parse_float=decimal.Decimal)

class Molecule(u.Unit):
    
    def __new__(cls, name):
        if isinstance(name, Symbol):
            name = name.name
        obj = AtomicExpr.__new__(cls)
        obj.name = name
        obj.abbrev = name
        contents = {}
        for match in re.finditer(r'([A-Z][a-z]?[a-z]?)([0-9]*)', name):
            contents[element_dict[match.group(1)]] = int(match.group(2)) if match.group(2) else 1
        obj.contents = contents
        return obj
    
    def __init__(self, name):
        if isinstance(name, Symbol):
            name = name.name
        contents = {}
        for match in re.finditer(r'([A-Z][a-z]?[a-z]?)([0-9]*)', name):
            contents[element_dict[match.group(1)]] = int(match.group(2)) if match.group(2) else 1
        self.contents = contents
        
def chemeq(side1, side2):
    elements = set()
    side1 = list(side1.atoms(Molecule))
    side2 = list(side2.atoms(Molecule))
    for item in side1 + side2:
        elements += item.keys()
    elements = list(elements)
    for item in elements:
        pass
    
    

class Element(u.Unit):

    def __new__(cls, name, info, **assumptions):
        obj = AtomicExpr.__new__(cls, **assumptions)
        obj.name = name
        obj.abbrev = info['symbol']
        obj.info = info
        return obj

    @property
    def mass(self):
        mass = self.info["atomic_weight"]
        if isinstance(mass, decimal.Decimal):
            return mass*u.g/u.mol
        else:
            return None
            
    @property
    def id(self):
        return self.info["symbol"]
        
    '''def __add__(self, other):
        return Molecule(self, other)'''
        
    def __string__(self):
        return self.id
        
    def __repr__(self):
        return self.__string__()

element_dict={}
for name, value in raw.items():
    element = Element(name, value)
    element_dict[value['symbol']] = element
