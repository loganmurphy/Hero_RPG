from PIL import Image

from characters import *
from instances import *
from items import *

im = Image.open("you-are-dead-screen.jpg")
player_char = ' '
# play_inventory = []
warrior = Warrior(10, 3, "warrior", 0, sword, 1)
medic = Medic(10, 2, "medic", 0, mace, 1)
shadow = Shadow(1, 2, "shadow", 0, dagger, 1)
mage = Mage(8, 1, 10, "mage", 0, wooden_staff, 1, 1)
goblin = Goblin(6, 2, "goblin", 2, None, None)
zombie = Zombie(10, 2, "zombie", 7, None, None)
orc = Orc(10, 3, "orc", 4, None, None)
print("You may choose a warrior, medic, shadow or mage as your character.")
player_select = input("Choose your player. ")
if player_select == "warrior":
    player_char = warrior
elif player_select == "medic":
    player_char = medic
elif player_select == "shadow":
    player_char = shadow
else:
    player_char = mage

battle(player_char, goblin)
