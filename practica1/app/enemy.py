from app.root import *

class Enemy(Root):
    def __init__(self, hp = 0, dmg = 0):
        super(Enemy, self).__init__(hp, dmg)
        
class PartialExam(Enemy):
    def __init__(self):
        super(PartialExam, self).__init__(hp = 25, dmg = 9)
        
class FinalExam(Enemy):
    def __init__(self):
        super(Enemy, self).__init__(hp = 40, dmg = 12)

    def hurt(self):
        if (super.hurt() == 7):
            value = 14
        else:
            value = super.hurt()
        return value
    
        
class TheoreticalClass(Enemy):
    def __init__(self):
        super(Enemy, self).__init__(hp = 40, dmg = 12)

    def hurt(self):
        value = super.hurt() + self.level
        return value
        
class Teacher(Enemy):
    def __init__(self):
        super(Enemy, self).__init__(hp = 15, dmg = 7)

