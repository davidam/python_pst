
from app.root import Root
from app.character import Character

class Worker(Character):

    def __init__(self):
        super().__init__(40, 10)
        self.victory = False
        
    def is_alive(self):
        if self.hp > 0:
            return True

    def hurt(self):
        if (self.rounds_accumulated == 3):
            value = (10 + super.hurt()) * 1.5
        else:
            value = super.hurt()
        return value

