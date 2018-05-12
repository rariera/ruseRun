
#!/usr/bin/env python3


class Character(object):
    def __init__(self, setting, level, cleared, pc, state, inventory, alphanum, equipment, HP):
        self.setting = setting
        self.level = level
        self.cleared = cleared
        self.pc = pc
        self.state = state
        self.inventory = inventory
        self.alphanum = alphanum
        self.equipment = equipment
        self.HP = HP

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
