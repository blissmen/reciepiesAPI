"""
Sample test
"""
from app.calc import add
from app.calc import raise_power
from django.test import SimpleTestCase

class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        self.assertEqual(add(1, 2), 3)  


    def test_raise_power(self):
        self.assertEqual(raise_power(2, 3), 8)