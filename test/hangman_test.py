import unittest
from model.digit_lib import Digit

class TestRover(unittest.TestCase):
    def test_oneNumber(self):
        digit = Digit()
        resultado = digit.validate('1')
        assert resultado=='*'
