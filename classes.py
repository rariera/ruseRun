
#!/usr/bin/env python3


class Character(object):
    def __init__(self, level, pc, state, inventory, alphanum):
        self.level = level
        self.pc = pc
        self.state = state
        self.inventory = inventory
        self.alphanum = alphanum

class LevelItems(object):
    def __init__(self, lvl1, lvl2):
        self.lvl1 = lvl1
        self.lvl2 = lvl2

class LevelMonsters(object):
    def __init__(self, lvl1, lvl2):
        self.lvl1 = lvl1
        self.lvl2 = lvl2
