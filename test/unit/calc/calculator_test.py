import unittest

from app.code.calc.calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(5, result)
