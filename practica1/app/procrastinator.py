
from app.root import Root
from app.character import Character

class Procrastinator(Character):

    def __init__(self):
        super().__init__(30, 6)
        
    def hurt(self):
        value = super.hurt() + (self.round - 1)
        return value

