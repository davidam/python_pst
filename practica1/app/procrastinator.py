
from app.root import Root
from app.character import Character

class Procrastinator:

    def __init__(self, hp, dmg):
        super().__init__(30, 6)
        self.victory = False
        
    def is_alive(self):
        if self.hp > 0:
            return True

