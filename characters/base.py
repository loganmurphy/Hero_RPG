from random import *

class Base_Stats:
    def __init__(self, health, power, char_class):
        self.health = health
        self.power = power
        self.char_class = char_class
    def special(self, enemy):
        pass
    def attack(self, enemy):
        self.special(enemy)
        die1 = randrange(1,7)
        die2 = randrange(1,7)
        if enemy.char_class == "zombie" and self.char_class in ["warrior", "medic", "shadow", "mage"]:
            print("Your attack has no effect!")
        elif die1 == die2 and self.char_class in ["warrior", "medic", "shadow", "mage"]:
            self.power = self.power * 2
            enemy.health -= self.power
        else:
            enemy.health -= self.power
            who = ' '
            if self.char_class in ["warrior", "medic", "shadow", "mage"]:
                print("You do {} damage to the {}.".format(self.power, enemy.char_class))
            else:
                print("The {} does {} damage to the {}.".format(self.char_class, self.power, enemy.char_class))
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
