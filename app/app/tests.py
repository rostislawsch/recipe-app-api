from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):
    
    """ Test that two numbersare added together """
    def test_add_numbers(self):
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """ Test that values are subtracted and returned"""
        self.assertEqual(subtract(4, 5), -1)
