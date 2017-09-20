from characters.base import Base_Stats
from random import *

class Warrior(Base_Stats):
    def attack(self, enemy):
        # make the hero generate double damage
        # points during an attack with a probability of 20%
        super().attack(enemy)
        die1 = randrange(1,7)
        die2 = randrange(1,7)
        if die1 == die2:
            self.power * 2
