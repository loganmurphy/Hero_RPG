from random import *
from items.weapons import *

class Base_Stats:
    def __init__(self, health, power, char_class, gold, weapon, armor, evade, health_potion):
        self.health = health
        self.power = power
        self.char_class = char_class
        self.gold = gold
        self.weapon = weapon
        self.armor = armor
        self.evade = evade
        self.health_potion = health_potion
    def drink_potion(self, potion):
        if potion == "healing potion" and self.health_potion > 0:
            self.health += 5
            self.health_potion -= 1
        elif potion == "potion of mana" and self.potion_of_mana > 0:
            self.mana += 5
            self.potion_of_mana -= 1
        else:
            print("You have none!")
    def special(self, enemy):
        pass
    def attack(self, enemy):
        self.special(enemy)
        die1 = randrange(1,7)
        die2 = randrange(1,7)
        if enemy.char_class == "zombie" and self.char_class in ["warrior", "medic", "shadow", "mage"]:
            print("Your attack has no effect!")
        elif die1 == die2 and self.char_class in ["warrior", "medic", "shadow", "mage"]:
            print("Critical hit!")
            self.power = self.power * 2
            enemy.health -= self.power
        else:
            adjusted_damage = self.power - enemy.armor
            enemy.health -= adjusted_damage
            who = ' '
        if self.char_class in ["warrior", "medic", "shadow", "mage"]:
            print("You do {} damage to the {}.".format(self.power, enemy.char_class))
        if die1 == die2 and self.char_class in ["warrior", "medic", "shadow", "mage"]:
            self.power = int(self.power / 2)
    def alive(self):
        if self.health > 0:
            return True
    def print_status(self):
        who = ' '
        if self.char_class in ["warrior", "medic", "shadow"]:
            who = 'You have'
        else:
            who = "The " + self.char_class + " has"
        print("{} {} health and {} power.".format(who, self.health, self.power))
    def display_inventory(self):
        print("You have: {} and {}".format(self.weapon, self.potion))
