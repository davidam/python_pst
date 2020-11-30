

class Root(object):

    def __init__(self, hp, dmg):
        self.hp = hp
        self.dmg = dmg

    def is_alive(self):
        if self.hp > 0:
            return True

