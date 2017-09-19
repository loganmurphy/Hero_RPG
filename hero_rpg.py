# Refactor the while condition:
#
# while goblin.health > 0 and hero.health > 0:
# to
#
# while goblin.alive() and hero.alive():
# The health checks should be moved to within the alive methods of
# Hero and Goblin respectively.

class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def attack(self, goblin):
        goblin.health -= hero.power
        print("You do {} damage to the goblin.".format(hero.power))
    def alive(self):
        if self.health > 0:
            return True
class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def attack(self, hero):
        hero.health -= goblin.power
        print("The goblin does {} damage to you.".format(goblin.power))
    def alive(self):
        if self.health > 0:
            return True
hero = Hero(10, 5)
goblin = Goblin(6, 2)
# This while statement was changed.
while goblin.alive() and hero.alive():
    print("You have {} health and {} power.".format(hero.health, hero.power))
    print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')
    raw_input = input()
    if raw_input == "1":
        hero.attack(goblin)
        if goblin.health <= 0:
            print("The goblin is dead.")
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input {}".format(raw_input))
# I changed the below if statement as well.
    if goblin.alive():
        goblin.attack(hero)
        if hero.health <= 0:
            print("You are dead.")
