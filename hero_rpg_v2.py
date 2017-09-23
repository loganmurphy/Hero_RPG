from PIL import Image

from characters import *
from instances import *
from items import *

im = Image.open("you-are-dead-screen.jpg")
player_char = ' '

print("You may choose a warrior, medic, shadow or mage as your character.")
while True:
    player_select = input("Choose your player. ").lower()
    if player_select not in ["warrior", "medic", "shadow", "mage"]:
        print("You must choose either a warrior, medic, shadow or a mage.")
    else:
        break
if player_select == "warrior":
    player_char = warrior
elif player_select == "medic":
    player_char = medic
elif player_select == "shadow":
    player_char = shadow
else:
    player_char = mage

battle(player_char, goblin)
go_shopping(player_char)
battle(player_char, orc)
go_shopping(player_char)
battle(player_char, zombie)
go_shopping(player_char)
battle(player_char, orc)
go_shopping(player_char)
battle(player_char, orc)
go_shopping(player_char)
battle(player_char, goblin)
if player_char.alive() == True:
    print("Congratulations, you have vanquished all of your foes. You are a true hero!")
else:
    pass
