
from app.root import Root

class Character(Root):

    def __init__(self, hp, dmg):
        super().__init__(hp, dmg)
        self.victory = False
        self.rounds_accumulated = 0

    def nextRound(self):
        self.rounds_accumulated = self.rounds_accumulated + 1
        
    def is_alive(self):
        if self.hp > 0:
            return True

