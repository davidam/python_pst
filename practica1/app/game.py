import random
from app.enemy import *

class Game(object):

    def __init__(self):
        self.turn = 0
        self.level = 0
        self.list_enemies = []
        self.list_characters = []

    def generate_enemy(self):
        if (self.level > 3): # En la regla especial final exam dice que 
                             # solo puede aparecer a partir del 4 nivel
            l = [0, 1, 2, 3]
        else:
            l = [0, 1, 2]
        for x in range(len(l)):
            n = random.randint(1,len(l))
            if (n == 1):
                enemy = PartialExam()
            elif (n == 2):
                enemy = TheoreticalClass()
            elif (n == 3):
                enemy = Teacher()
            elif (n == 4):            
                enemy = FinalExam()                
                
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
    
    def check_with_life(self, l):
        alldies = True
        for i in l:
            if (i.is_alive()):
                death = False
            else:
                death = True
            alldies = (alldies and death)
        return alldies

    def attack_enemies_to_characters(self):
        for i in self.list_enemies:
            n = random.randint(0,len(self.list_characters))        
            self.attack(i, self.list_characters[n])
        return self.list_characters

    def attack_characters_to_enemies(self):
        for i in self.list_characters:
            n = random.randint(0,len(self.list_enemies))        
            self.attack(i, self.list_enemies[n])
        return self.list_enemies

#    def main(self):
        
