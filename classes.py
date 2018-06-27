
#!/usr/bin/env python3


class Character(object):
    def __init__(self, name, difficulty, setting, level, pc, state, inventory, alphanum, equipment, HP, cheats, token, been, turns):
        self.name = name
        self.difficulty = difficulty
        self.setting = setting
        self.level = level
        self.pc = pc
        self.state = state
        self.inventory = inventory
        self.alphanum = alphanum
        self.equipment = equipment
        self.HP = HP
        self.cheats = cheats
        self.token = token
        self.been = been
        self.turns = turns

class LevelItems(object):
    def __init__(self, lvl1_1, lvl1_2, lvl2_1, lvl2_2, lvl2_3, lvl2_4, lvl3_1, lvl3_2, lvl3_3):
        self.lvl1_1 = lvl1_1
        self.lvl1_2 = lvl1_2
        self.lvl2_1 = lvl2_1
        self.lvl2_2 = lvl2_2
        self.lvl2_3 = lvl2_3
        self.lvl2_4 = lvl2_4
        self.lvl3_1 = lvl3_1
        self.lvl3_2 = lvl3_2
        self.lvl3_3 = lvl3_3


class LevelMonsters(object):
    def __init__(self, lvl1_1, lvl1_2, lvl2_1, lvl2_2, lvl2_3, lvl2_4, lvl3_1, lvl3_2, lvl3_3):
        self.lvl1_1 = lvl1_1
        self.lvl1_2 = lvl1_2
        self.lvl2_1 = lvl2_1
        self.lvl2_2 = lvl2_2
        self.lvl2_3 = lvl2_3
        self.lvl2_4 = lvl2_4
        self.lvl3_1 = lvl3_1
        self.lvl3_2 = lvl3_2
        self.lvl3_3 = lvl3_3
