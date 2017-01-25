import unittest
from model.hangman_lib import HangMan

class TestHangman(unittest.TestCase):

    def test_one_word_success(self):
        hangman = HangMan()
        body,partial = hangman.validate("a")
        self.assertEquals(partial,"_a_a__a")
        self.assertEquals(body, "OOOOOO")
 
    def test_one_word_success_other(self):
        hangman = HangMan()
        body,partial = hangman.validate("p")
        self.assertEquals(partial,"p______")
        self.assertEquals( body, "OOOOOO")
        body,partial = hangman.validate("a")
        self.assertEquals(partial,"pa_a__a")
        self.assertEquals( body, "OOOOOO")

    def test_one_word_success_fail(self):
        hangman = HangMan()
        body,partial = hangman.validate("i")
        self.assertEquals( partial,"_______")
        self.assertEquals( body, "XOOOOO")
        body,partial = hangman.validate("i")
        self.assertEquals( partial,"_______")
        self.assertEquals( body , "XXOOOO")




