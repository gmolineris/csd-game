import unittest
from model.hangman_lib import HangMan

class TestHangman(unittest.TestCase):
    def test_oneletter_success(self):
        hangman = HangMan()
        result = hangman.validate("i")
        self.assertTrue(result)

    def test_oneletter_fail(self):
        hangman = HangMan()
        result = hangman.validate("x")
        self.assertFalse(result)
