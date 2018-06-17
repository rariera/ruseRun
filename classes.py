
#!/usr/bin/env python3


class Character(object):
    def __init__(self, name, difficulty, setting, level, pc, state, inventory, alphanum, equipment, HP, cheats, token, been):
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

class LevelItems(object):
    def __init__(self, lvl1, lvl2, lvl3):
        self.lvl1 = lvl1
        self.lvl2 = lvl2
        self.lvl3 = lvl3

class LevelMonsters(object):
    def __init__(self, lvl1, lvl2, lvl3):
        self.lvl1 = lvl1
        self.lvl2 = lvl2
        self.lvl3 = lvl3
