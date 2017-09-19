# The methods attack and print_status method in Hero and Goblin look
# almost identical, but not quite. Is it possible to move them into the
# Character class as well? Give it a try.

class Character:
    def __init__(self, name, health, power):
        self.health = health
        self.power = power
        self.name = name
    def alive(self):
        if self.health > 0:
            return True
    def print_status(self):
        if self.name is "Hero":
            who = "You have"
        else:
            who = "The goblin has"
        print("{} {} health and {} power.".format(who, self.health, self.power))
    def attack(self, enemy):
        if self.name == "Hero":
            attacker = "You do"
            attackee = "the goblin"
        else:
            attacker = "The goblin does"
            attackee = "you"
        enemy.health -= self.power
        print("{} {} damage to {}.".format(attacker, self.power, attackee))

class Hero (Character):
    pass
    # Everything is in the Character class now.
    # def attack(self, goblin):
    #     goblin.health -= hero.power
    #     print("You do {} damage to the goblin.".format(hero.power))
    # def print_status(self):
    #     print("You have {} health and {} power.".format(hero.health, hero.power))

class Goblin (Character):
    pass
    # Everything is in the Character class now.
    # def attack(self, hero):
    #     hero.health -= goblin.power
    #     print("The goblin does {} damage to you.".format(goblin.power))
    # def print_status(self):
    #     print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))

hero = Hero("Hero", 10, 5)
goblin = Goblin("Goblin", 6, 2)

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
