
#!/usr/bin/env python3


class Character(object):
    def __init__(self, level, pc, inventory):
        self.level = level
        self.pc = pc
        self.inventory = inventory

class LevelItems(object):
    def __init__(self, lvl1):
        self.lvl1 = lvl1
