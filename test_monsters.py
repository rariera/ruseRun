#!/usr/bin/python3

import unittest
from monsters import monsterChoose

class TestMonsterChoose(unittest.TestCase):
    '''tests for monsters.monsterChoose'''

    def test_monster_choose(self):
        floorlist = [(1,2),(1,3),(1,4),(2,2),(2,3),(2,4)]
        level_monsters = monsterChoose(floorlist, 1, density=3)
        # run tests
        self.assertTrue(level_monsters)
        self.assertTrue(level_monsters.lvl1)
#       self.assertTrue(level_monsters.lvl2)

if __name__ == '__main__':
    unittest.main()

