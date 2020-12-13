
from app.root import Root
from app.character import Character

class Whatsapper(Character):

    def __init__(self, hp, dmg):
        super().__init__(20, 6)
        self.victory = False
        


