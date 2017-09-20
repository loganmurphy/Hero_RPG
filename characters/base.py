from random import *

class Base_Stats:
    def __init__(self, health, power, char_class):
        self.health = health
        self.power = power
        self.char_class = char_class
    def attack(self, enemy):
        # make the hero generate double damage
        # points during an attack with a probability of 20%
        die1 = randrange(1,7)
        die2 = randrange(1,7)
        if die1 != die2:
            enemy.health -= self.power
            # self.power = int(self.power / 2)
        elif die1 == die2 and self.char_class in ["warrior"]:
            self.power = self.power * 2
        who = ' '
        if self.char_class in ["warrior"]:
            who = 'You do'
        else:
            who = "The " + self.char_class + " does"
        print("{} {} damage to the {}.".format(who, self.power, enemy.char_class))
        if die1 == die2:
            self.power = int(self.power / 2)

    def alive(self):
        if self.health > 0:
            # print("I'm alive!")
            return True
    def print_status(self):
        who = ' '
        print("{} {} health and {} power.".format(who, self.health, self.power))
