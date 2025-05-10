import unittest
from main import NormalMode
import random

class TestYahtzeeRoll(unittest.TestCase):
    def setUp(self):
        self.yahtzee = YahtzeeRoll()

    def test_ones(self):
        self.yahtzee.roll = [1, 6, 2, 1, 1]
        self.assertEqual(self.yahtzee.upperscore("All-Ones"), 3)

    def test_fives(self):
        self.yahtzee.roll = [6, 5, 1, 6, 1]
        self.assertEqual(self.yahtzee.upperscore("All-Fives"), 5)
        
    def test_sixes(self):
        self.yahtzee.roll = [3, 6, 1, 6, 4]
        self.assertEqual(self.yahtzee.upperscore("All-Sixes"), 12)

    def test_full_house(self):
        self.yahtzee.roll = [1, 1, 1, 2, 2]
        self.assertEqual(self.yahtzee.lowerscore("Full_House"), 25)

    def test_four_kind(self):
        self.yahtzee.roll = [4, 4, 4, 4, 5]
        self.assertEqual(self.yahtzee.lowerscore("Four_Kind"), 21)

    def test_score_yahtzee(self):
        self.yahtzee.roll = [1, 1, 1, 1, 1]
        scores = self.yahtzee.roll()
        self.assertEqual(scores["YAHTZEE!!"], 50)

    def test_chance(self):
        self.yahtzee.roll = [5, 5, 4, 6, 4]
        self.assertEqual(self.yahtzee.lowerscore("Chance_Time"), 24)
        
    def test_outlimit_reroll(self): #I decided to make a test that deals with assertRaises similiar to the bank test example.
         with self.assertRaises(ValueError):
            self.yahtzee.reroll([7,8,9,111,1222222332327464])

if __name__ == '__main__':
    unittest.main()
