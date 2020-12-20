
from app.root import Root
from app.character import Character

class Whatsapper(Character):

    def __init__(self, hp, dmg):
        super().__init__(20, 6)
        self.victory = False
        
    def treatment(self, player):
        value = 2 * self.dmg
        if ((self.turn / 3) == 0):
            player.hp = player.hp + value
        return player.hp
