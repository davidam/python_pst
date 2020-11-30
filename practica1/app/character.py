

class Character(object):

    def __init__(self, hp=0, dmg=0):
        self.hp = hp
        self.dmg = dmg
        self.victory = False

    def is_alive(self):
        if self.hp > 0:
            return True

