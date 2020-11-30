from app.root import *

class Enemy(Root):
    def __init__(self, hp = 0, dmg = 0):
        super(Enemy, self).__init__(hp, dmg)

    # def is_alive(self):
    #     super(Root, self).is_alive()
        
class PartialExam(Enemy):
    def __init__(self, hp = 25, dmg = 9):
        super(PartialExam, self).__init__(hp, dmg)

    # def is_alive(self):
    #     super(PartialExam, self).is_alive()
        
# class FinalExam(Enemy):
#     def __init__(self, hp = 40, dmg = 12):
#         super(Enemy, self).__init__(hp, dmg)
    
# class TheoreticalClass(Enemy):
#     def __init__(self, hp = 8, dmg = 4):
#         super(Enemy, self).__init__(hp, dmg)

# class Teacher(Enemy):
#     def __init__(self, hp = 15, dmg = 7):
#         super(Enemy, self).__init__(hp, dmg)

