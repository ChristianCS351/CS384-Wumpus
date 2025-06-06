import unittest
from main import NormalMode
import random

class TestNormalMode(unittest.TestCase):

    def setUp(self):
        self.caves_num = 25
        self.game = NormalMode(self.caves_num)
        
    def test_arrow(self):
        arrow_count = sum(1)
        self.assertEqual(arrow_count, 1)

    def test_pit(self):
        pit_count = sum(1)
        self.assertEqual(pit_count, 1)
        
    def test_bat(self):
        bat_count = sum(1)
        self.assertEqual(bat_count, 1)
        

    def test_wumpus(self):
        wumpus_count = sum(1)
        self.assertEqual(wumpus_count, 1)

    def test_player_safe(self):
        player_spawn = self.game.player_spawn(self.caves.num)
        cave = self.game.cave[player_spawn]
        self.assertFalse(cave[index_wumpus])
        self.assertFalse(cave[index_pit])
        self.assertFalse(cave[index_bat])
        self.assertFalse(cave[index_arrow])


if __name__ == '__main__':
    unittest.main()
