# Take the code for printing the health status of the hero and move it into a method
# called print_status of Hero. Do the same for the goblin.
from PIL import Image
from characters import *

im = Image.open("you-are-dead-screen.jpg")
# print('hello')
player = Warrior(10, 5, "warrior")
monster = Goblin(6, 2, "bandit")


while monster.alive() and player.alive():
    # These lines replace the lines below them.
    player.print_status()
    monster.print_status()
    # print("You have {} health and {} power.".format(hero.health, hero.power))
    # print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')
    raw_input = input()
    if raw_input == "1":
        player.attack(monster)
        if monster.health <= 0:
            print("The goblin is dead.")
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input {}".format(raw_input))
    if monster.alive():
        monster.attack(player)
        if player.health <= 0:
            im.show()
            print("You are dead.")
