from characters.base import Base_Stats
from random import *

class Goblin(Base_Stats):
    def attack(self, enemy):
        self.special(enemy)
        die1 = randrange(1,7)
        die2 = randrange(1,7)
        if die1 + die2 > 3 and enemy.char_class == "shadow":
            self.power = 0
            print("The {} missed!".format(self.char_class))
        elif enemy.evade == 2 and die1 + die2 > 11:
            self.power = 0
            print("You dodged the attack!")
        elif enemy.evade == 4 and die1 + die2 > 10:
            self.power = 0
            print("You dodged the attack!")
        elif enemy.evade == 6 and die1 + die2 > 9:
            self.power = 0
            print("You dodged the attack!")
        elif enemy.evade == 8 and die1 + die2 > 8:
            self.power = 0
            print("You dodged the attack!")
        elif enemy.evade == 10 and die1 + die2 > 7:
            self.power = 0
            print("You dodged the attack!")
        else:
            adjusted_damage = self.power - enemy.armor
            enemy.health = (enemy.health - adjusted_damage)
            print("The {} does {} damage to the {}.".format(self.char_class, adjusted_damage, enemy.char_class))
        self.power = 2

class Zombie(Goblin):
    def alive(self):
        if self.health > 0:
            return True

class Orc(Goblin):
    def special(self, enemy):
        if self.health < 5:
            self.power = self.power * 1.5
goblin = Goblin(6000, 2, "goblin", 2, None, 0, None, None)
zombie = Zombie(10, 2, "zombie", 7, None, 0, None, None)
orc = Orc(10, 3, "orc", 4, None, 0, None, None)
