from app.character import Character


class Bookworm(Character):
# "Una vez cada 4 rondas puede resucitar a otro jugador que haya "
# "perdido todos los puntos de vida.\nSi se utiliza la habilidad y no "
# "hay ningún jugador sin puntos de vida no cuenta como usada."
    
    def __init__(self):
        super().__init__(25, 9)
        self.rounds_accumulated = 0
        self.skill_used = False

    def nextRound(self):
        self.rounds_accumulated = self.rounds_accumulated + 1

    def resurrection(self, player):
        if (self.rounds_accumulated > 4):
            player.hp = 1
            self.rounds_accumulated = 0
            
    def getSkill(self):
        return self.skill

    def setSkill(self, skill):
        self.skill = skill

    def isSkillUsed(self):
        return self.skill_used

    def setSkillUsed(self, used):
        self.skill_used = used

    def __str__(self):
        return "BOOKWORM\n" +"\nSkill: " + self.skill + "\nUsed: " + str(self.skill_used) + "\n"

# player = Bookworm(25, 9)

# print(player.__str__())
# print(player.hp)
# print(player.dmg)
