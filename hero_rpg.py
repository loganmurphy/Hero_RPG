# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
# Step 1
#
# Make a Hero class to store the health and power of the hero, and make a Goblin class to store the health and power of the goblin.
# Use a hero object in place of the variables hero.health and hero.power and use a goblin object in place of the variables goblin.health
# and goblin.power all through out the app.

class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power
class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power
hero = Hero(10, 5)
goblin = Goblin(6, 2)

while goblin.health > 0 and hero.health > 0:
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
        # Hero attacks goblin
        goblin.health -= hero.power
        print("You do {} damage to the goblin.".format(hero.power))
        if goblin.health <= 0:
            print("The goblin is dead.")
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input {}".format(raw_input))

    if goblin.health > 0:
        # Goblin attacks hero
        hero.health -= goblin.power
        print("The goblin does {} damage to you.".format(goblin.power))
        if hero.health <= 0:
            print("You are dead.")
            