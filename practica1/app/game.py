import random
from app.enemy import *

class Game(object):

    def __init__(self):
        self.turn = 0
        self.level = 0
        self.list_enemies = []
        self.list_characters = []

    def generate_enemy(self):
        l = [0, 1, 2, 3]
        for x in range(4):
            n = random.randint(1,4)
            if (n == 1):
                enemy = PartialExam()
            elif (n == 2):            
                enemy = FinalExam()                
            elif (n == 3):
                enemy = TheoreticalClass()
            elif (n == 4):
                enemy = Teacher()
        return enemy
    
    def initialize_enemies(self):
        enemy1 = self.generate_enemy()
        self.list_enemies.append(enemy1)
        enemy2 = self.generate_enemy()
        self.list_enemies.append(enemy2)        
        enemy3 = self.generate_enemy()
        self.list_enemies.append(enemy3)        
        enemy4 = self.generate_enemy()
        self.list_enemies.append(enemy4)
        return self.list_enemies

    def next_level(self):
        self.level = self.level + 1
        return self.level

    def attack(self, from1, to1):
        damage = from1.hurt()
        to1.hp = to1.hp - damage
        return to1.hp
    
