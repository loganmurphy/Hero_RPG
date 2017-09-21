# Take the code for printing the health status of the hero and move it into a method
# called print_status of Hero. Do the same for the goblin.
from PIL import Image

from characters import *

im = Image.open("you-are-dead-screen.jpg")
# player = Warrior(10, 5, "warrior")
# player = Medic(10, 3, "medic")
player = Mage(8, 2, 10, "mage")
# monster = Goblin(6, 2, "goblin")
monster = Zombie(10, 2, "zombie")
# monster = Zombie(0, 2, "zombie")

while monster.alive() and player.alive():
    player.print_status()
    monster.print_status()
    print("What do you want to do?")
    print("1. fight ", monster.char_class)
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')
    raw_input = input()
    if raw_input == "1":
        player.attack(monster)
        if monster.health <= 0: # and monster.char_class not in ["zombie"]:
            print("The ", monster.char_class, " is dead.")
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
