from random import *
from items.weapons import *
# sword = (randrange(2,4))
# dagger = (randrange(1,2))
# mace = (randrange(2,3))
# wooden_staff = (1)

class Base_Stats:
    def __init__(self, health, power, char_class, gold, weapon, armor, health_potion):
        self.health = health
        self.power = power
        self.char_class = char_class
        self.gold = gold
        self.weapon = weapon
        self.armor = armor
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
        if self.weapon in [sword, "dagger", "mace", "wooden_staff"]:
            self.power = self.power + self.weapon
        self.special(enemy)
        die1 = randrange(1,7)
        die2 = randrange(1,7)
        if enemy.char_class == "zombie" and self.char_class in ["warrior", "medic", "shadow", "mage"]:
            print("Your attack has no effect!")
        elif die1 == die2 and self.char_class in ["warrior", "medic", "shadow", "mage"]:
            self.power = self.power * 2
            enemy.health -= self.power
        else:
            adjusted_damage = self.power - enemy.armor
            enemy.health = (enemy.health - adjusted_damage)
            who = ' '
            if self.char_class in ["warrior", "medic", "shadow", "mage"]:
                print("You do {} damage to the {}.".format(self.power + self.weapon, enemy.char_class))
            else:
                print("The {} does {} damage to the {}.".format(self.char_class, adjusted_damage, enemy.char_class))
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
