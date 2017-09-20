# Create a zombie character that cannot die and have it fight
# the hero instead of the goblin.
from PIL import Image
im = Image.open("you-are-dead-screen.jpg")
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
        elif self.name is "goblin":
            who = "The goblin has"
        else:
            who = "The zombie has"
        print("{} {} health and {} power.".format(who, self.health, self.power))
    def attack(self, enemy):
        # I re-wrote this code to account for the zombie being invincible.
        if enemy.name == "Zombie":
            print("Your attack has no effect!")
        elif self.name == "Zombie":
            enemy.health -= self.power
            print("The zombie does {} damage to you.".format(self.power))
        elif self.name == "Hero":
            enemy.health -= self.power
            print("You do {} damage to goblin.".format(self.power))
        else:
            enemy.health -= self.power
            print("The goblin does {} damage to you.".format(self.power))

class Hero (Character):
    pass

class Goblin (Character):
    pass

class Zombie (Character):
    pass

hero = Hero("Hero", 10, 5)
goblin = Goblin("Goblin", 6, 2)
zombie = Zombie("Zombie", 10, 2)

while zombie.alive() and hero.alive():
    hero.print_status()
    zombie.print_status()
    print()
    print("What do you want to do?")
    print("1. fight zombie")
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')
    raw_input = input()
    if raw_input == "1":
        hero.attack(zombie)
        if zombie.health <= 0:
            print("The zombie is dead.")
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input {}".format(raw_input))
    if zombie.alive():
        zombie.attack(hero)
        if hero.health <= 0:
            im.show()
            print("You are dead.")
