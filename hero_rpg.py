# Do you see a lot of duplicated or similar code between Hero and Goblin? What if you can share
# the duplicated code between them? You can by using inheritance! Create a new class called
# Character and make both Hero and Goblin inherit from it.

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

class Hero (Character):
    # This is now inherited from Character:
    # def __init__(self, health, power):
    #     self.health = health
    #     self.power = power
    def attack(self, goblin):
        goblin.health -= hero.power
        print("You do {} damage to the goblin.".format(hero.power))
    def alive(self):
        if self.health > 0:
            return True
    def print_status(self):
        print("You have {} health and {} power.".format(hero.health, hero.power))

class Goblin (Character):
    # This is now inherited from Character:
    # def __init__(self, health, power):
    #     self.health = health
    #     self.power = power
    def attack(self, hero):
        hero.health -= goblin.power
        print("The goblin does {} damage to you.".format(goblin.power))
    def alive(self):
        if self.health > 0:
            return True
    def print_status(self):
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))

hero = Hero(10, 5)
goblin = Goblin(6, 2)
print(hero.health)
while goblin.alive() and hero.alive():
    hero.print_status()
    goblin.print_status()
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
    if goblin.alive():
        goblin.attack(hero)
        if hero.health <= 0:
            print("You are dead.")
