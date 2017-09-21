from characters.base import Base_Stats
from random import *

class Goblin(Base_Stats):
    def attack(self, enemy):
        # self.power = 2
        self.special(enemy)
        die1 = randrange(1,7)
        die2 = randrange(1,7)
        if die1 + die2 > 3 and enemy.char_class == "shadow":
            self.power = 0
            print("The {} missed!".format(self.char_class))
        else:
            enemy.health -= self.power
            print("The {} did {} damage to the {}.".format(self.char_class, self.power, enemy.char_class))
        self.power = 2
# make a Zombie character that doesn't die even if his health is below zero
class Zombie(Goblin):
    def alive(self):
        if self.health > 0:
            return True

# come up with at least two other characters with their individual
# characteristics, and implement them.
# Here's another.

class Orc(Goblin):
    def special(self, enemy):
        if self.health < 5:
            self.power = self.power * 1.5
