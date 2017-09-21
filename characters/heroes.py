from characters.base import Base_Stats
from random import *

class Warrior(Base_Stats):
    # def special(self, enemy):
    pass

class Medic(Base_Stats):
    def special(self, enemy):
        die1 = randrange(1,7)
        die2 = randrange(1,7)
        if die1 == die2 and self.health < 8:
            self.health += 2
            print("The medic regenerated 2 health")

# make a character called Shadow who has only 1 starting health but will only
# take damage about once out of every ten times he is attacked.
class Shadow(Base_Stats):
    pass

# come up with at least two other characters with their individual
# characteristics, and implement them.
# Here's one.

class Mage(Base_Stats):
    def __init__(self, health, power, mana, char_class):
        self.health = health
        self.power = power
        self.char_class = char_class
        self.mana = mana
    def special(self, enemy):
        die3 = randrange(2, 13)
        if self.mana > 0:
            print("The mage casts a lightning spell and does {} damage".format(die3))
            enemy.health -= die3
            self.mana -= 2
        elif enemy.char_class == "zombie":
            pass
        # else enemy.char_class != "zombie":
        #     enemy.health - self.power
        #     print("You do 2 damage to the {}.".format(enemy.char_class))
    def print_status(self):
        print("The mage has {} health, {} power and {} mana.".format(self.health, self.power, self.mana))
