# Take the code for printing the health status of the hero and move it into a method
# called print_status of Hero. Do the same for the goblin.
from PIL import Image

from characters import *

im = Image.open("you-are-dead-screen.jpg")
# Give each enemy a bounty.
# player = Warrior(10, 5, "warrior", 0)
# player = Medic(10, 3, "medic", 0)
# player = Shadow(1, 3, "shadow", 0)
player = Mage(8, 2, 10, "mage", 0)
# monster = Goblin(6, 2, "goblin", 2)
monster = Zombie(10, 2, "zombie", 7)
# monster = Orc(10, 3, "orc", 4)

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
        if monster.health <= 0:
            player.gold += monster.gold
            print("The ", monster.char_class, " is dead.")
            print("You looted {} gold pieces".format(monster.gold))
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
