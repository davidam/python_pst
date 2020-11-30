
from app.root import Root

class Character2(Root):

    def __init__(self, hp, dmg):
        super().__init__(hp, dmg)

    def is_alive(self):
        if self.hp > 0:
            return True

