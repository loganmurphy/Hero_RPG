from characters.base import Base_Stats
from items import *
from random import *



class Warrior(Base_Stats):
    pass

class Medic(Base_Stats):
    def special(self, enemy):
        die1 = randrange(1,7)
        die2 = randrange(1,7)
        if die1 == die2 and self.health < 8:
            self.health += 2
            print("The medic regenerated 2 health")

class Shadow(Base_Stats):
    pass

class Mage(Base_Stats):
    def __init__(self, health, power, mana, char_class, gold, weapon, armor, health_potion, potion_of_mana):
        self.health = health
        self.power = power
        self.char_class = char_class
        self.mana = mana
        self.gold = gold
        self.weapon = weapon
        self.armor = armor
        self.health_potion = health_potion
        self.potion_of_mana = potion_of_mana
    def special(self, enemy):
        die3 = randrange(2, 13)
        if self.mana > 0:
            print("The mage casts a lightning spell and does {} damage".format(die3))
            enemy.health -= die3
            self.mana -= 2
    def print_status(self):
        print("You have {} health, {} power and {} mana.".format(self.health, self.power, self.mana))
