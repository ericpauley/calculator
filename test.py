import unittest
import random
import calculator
from math import *

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calc = calculator.Calculator()

    def run_cmd(self, cmd):
        return self.calc.run_cmd(cmd)

    def test_sin(self):
        for i in range(100):
            n = random.random()*2*pi
            self.assertEqual(int(self.run_cmd("sin(%s)" % n)*100000), int(sin(n)*100000))

    def test_cos(self):
        for i in range(100):
            n = random.random()
            self.assertEqual(int(self.run_cmd("cos(%s)" % n)*100000), int(cos(n)*100000))

    def test_symbol_simplify(self):
        self.assertEqual(self.run_cmd("2x"), self.run_cmd("x+x"))

    def test_solve(self):
        self.assertEqual(self.run_cmd("solve(2x-1==5)"), [3])

    def test_solve_quad(self):
        self.assertEqual(self.run_cmd("solve(2x^2-1==17)"), [-3, 3])

    def test_diff(self):
        self.assertEqual(self.run_cmd("diff(x^2+2x+10)"), self.run_cmd("2x+2"))

    def test_integral(self):
        self.assertEqual(self.run_cmd("integrate(x^2+6)"), self.run_cmd("x^3/3+6x"))

if __name__ == '__main__':
    unittest.main()
