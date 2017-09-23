import sys
import os
# Here is where I have stored all of the character/enemy stats
class Monster:
     def __init__(self, name, hp, ap):
         self.name = name
         self.hp = hp
         self.ap = ap
     def displayMonster(self):
         print "Name : ", self.name,  ", HP: ", self.hp, ", AP: ", self.ap
#Below is the list of enemy types in the game.
goblin = Monster("Goblin", 10, 2)
orc = Monster("Orc", 13, 4)

class Player:
    def __init__(self, Class, hp, ap, mp):
        self.Class = Class
        self.hp = hp
        self.ap = ap
        self.mp = mp
    def displayPlayer(self):
        print "Class : ", self.Class,  ", HP: ", self.hp, ", AP: ", self.ap, ", MP: ", self.mp
# warrior = Player("Warrior", 10, 5, 0)
# archer = Player("Archer", 10, 3, 0)
# mage = Player("Mage", 10, 1, 5)
# p1 = Player("", 0, 0, 0)

class Magic:
    def __init__(self, spell, mp, dmg):
        self.spell = spell
        self.mp = mp
        self.dmg = dmg
    def displayMagic(self):
        print "Spell : ", self.spell, ", MP Cost: ", self.mp, ", Damage: ", self.dmg
# Below is the list of spells available in the game.
fireBall = Magic("fire-ball", 1, "4-7")
# fireBall.displayMagic()

#This function allows the monster to attack the player.
def monsterAttack(monster, player):
    from random import randint
    rand_num = (randint(0, monster.ap))
    player.hp = player.hp - rand_num
    if (rand_num == 0):
        print "The fiend misses!"
    else:
        print "The beast did %s damage." %(rand_num)
    if (player.hp == 0):
        print "You have been defeated!"

#This function allows the player to attack the monster.
def playerAttack(player, monster):
    from random import randint
    rand_num = (randint(0, player.ap))
    monster.hp = monster.hp - rand_num
    if (rand_num == 0):
        print "You missed!"
    else:
        print "You did %s damage." %(rand_num)
    if (monster.hp == 0):
        print "You have slain the beast!"

def escapeRoll():
    from random import randint
    rand_num = (randint(0, 10))
    print rand_num
    if (rand_num >= 5):
        print "You escaped."
    else:
        print "You can't get away!"
        monsterAttack(goblin, p1)
# A function that allows the player to escape from battle. Instead of using this, I have decided to manually code the loop
# in the "battle" so that I am allowed more flexibility with the usage of my variables.

def inventoryCheck():
    print inventory
# Checks the current contents of the player's inventory.

def fire_ball(monster):
  from random import randint
  rand_num = (randint(4, 7))
  monster.hp = monster.hp - rand_num
  print "You did %s damage." %(rand_num)
# Casts fire-ball

print "You find yourself at the foot of an old abandoned mine. In front of the cavernous entrance stands an old, wizened man."
char_name = raw_input("Old man: Hello, what is your name? ")
#Choices are Dwarf, Elf and Human
while True:
    char_race = raw_input("Old man: What Race are you a member of? ")
    if char_race.lower() not in ('dwarf', 'elf', 'human'):
        print "You may choose a Dwarf, Elf or Human as your character's race."
    else:
        print "Ah, well met noble %s." %(char_race)
        break
while True:
    char_class = raw_input("Old man: What class are you? ")
    if char_class.lower() not in ("warrior", "archer", "mage"):
        print "Hmm, never heard of that before. Around here we just have warriors, archers or mages."
        print "Choose again."
    else:
        print "I thought as much, you have the bearings of a %s." %(char_class)
        break
#Choices are warrior, archer and mage

if (char_race == "dwarf" and char_class == "warrior"):
    p1 = Player("Warrior", 10, 6, 0)
    print "Here are your stats: "
    p1.displayPlayer()
elif (char_race == "elf" and char_class == "archer"):
    p1 = Player("Archer", 10, 4, 0)
    print "Here are your stats: "
    p1.displayPlayer()
elif (char_race == "human" and char_class == "mage"):
    p1 = Player("Mage", 10, 1, 6)
    print "Here are your stats: "
    p1.displayPlayer()
elif (char_race != "dwarf" and char_class == "warrior"):
    p1 = Player("Warrior", 10, 5, 0)
    print "Here are your stats: "
    p1.displayPlayer()
elif (char_race != "elf" and char_class == "archer"):
    p1 = Player("Archer", 10, 3, 0)
    print "Here are your stats: "
    p1.displayPlayer()
else:
    p1 = Player("Mage", 10, 1, 5)
    print "Here are your stats: "
    p1.displayPlayer()

char_gen = raw_input("Old man: What is your gender? ")

print "Old man: Hello, brave %s. Tell me, what brings a %s %s to our lands?" % (char_name, char_race, char_class)
reason = raw_input("Old man: Is it adventure that you seek? ")

if (reason.lower() == "no"):
    print "Old man: Oh, how disapointing. A coward. Begone from here, the sight of you sickens me."
    print "You turn and leave, shoulders slumped in defeat. The old man's loud, shrill laughter rings in your ears as you make retreat."
    print ">>>>>>>>>GAME OVER<<<<<<<<<"
    os.execl(sys.executable, sys.executable, *sys.argv)
    # This restarts the program at the beginning.
    # sys.exit()
    # This exits the program completely.
else:
    print "Old man: May the Gods look over you on your journey. Here, take this. I no longer need it."
    print "Old man: And you my friend, will need all the help you can get."
    if(char_class == "warrior"):
        print "The old man hands over a sheathed short-sword. It is well-worn, but upon inspection you find it to be deadly-sharp"
        inventory = ["short-sword"]
        print "You look up to thank the old man, only to find he has vanished."
    elif(char_class == "archer"):
        print "The old man hands over a cloth-wrapped short-bow and quiver of arrows. The draw-string is frayed, and the wooden shaft well-worn, but it will do."
        inventory = ["short-bow", "10 arrows"]
        print "You look up to thank the old man, only to find he has vanished."
    else:
        print "The old man hands over a dust-covered scroll, and a stout wooden-staff. You unravel the scroll and find that the script is in a familiar language, and you realize this is a fire-spell. With this, you can hurl fire-balls at your enemies"
        magic = ["fire-ball"]
        inventory = ["wooden-staff"]
        print "You look up to thank the old man, only to find he has vanished."
    user_choice = raw_input("The mine-shaft lies await, like a demon's maw ready to swallow you. You have come too far to turn around. What do you do? ")
    if user_choice not in ("enter", "go in", "continue"):
        print "Make another choice."
    else:
        print "You take your first steps into the mine, dreaming of the treasures you will find. As you continue down further, you come to a fork in the path. Beyond, the light of the sun no longer reaches."
        user_choice = raw_input("The pathways to the left and right are equally dark and foreboding. No telling what lies in wait down either. Which direction do you go? ")
        if user_choice not in ("left", "right", "inventory"):
            print "Make another choice."
        else: print "You make your way down the %s-hand path, stepping carefull as you secure your footing. The is much steeper than you expected." % (user_choice)
        if (user_choice == "left"):
            print "As you make your way into the depths of the mine, running your hand along the wall to steady yourself, you start to wish the old man had given you a torch instead."
            print "You stop abrubtly as you hear a faint chattering ahead."
        # elif (user_choice == "inventory"):
        #     inventoryCheck()
        else:
            print "As you are make your way down the path, you suddenly lose your footing and fall on your back, sliding several-hundred-feet down the tunnel. You come to a stop as you crash head-first into a wall."
            print "You know that the wet feeling spreading over your face is not moisture from the cave wall as you think of the family you left behind to chase fortune and fame. If only you had stayed away from this forsaken place. Everything goes black."
            print ">>>>>>>>>GAME OVER<<<<<<<<<"
            os.execl(sys.executable, sys.executable, *sys.argv)


# I need a way to pass in the information on the character based on the player's choices. OK
# print "A vicious Goblin stands before you. Before you have time to think, the beast pounces!"
# goblin.displayMonster()
# # p1.displayPlayer()
# while (goblin.hp != 0):
#     user_choice = raw_input("What do you do? ")
#     if user_choice not in ("attack", "fight", "magic", "escape", "run"):
#         print "Make another choice."
#     elif (user_choice == "attack" or user_choice == "fight"):
#         monsterAttack(goblin, p1)
#         playerAttack(p1, goblin)
#         # goblin.displayMonster()
#         # p1.displayPlayer()
#         if (p1.hp <= 0):
#             print "GAME OVER"
#             os.execl(sys.executable, sys.executable, *sys.argv)
#             break
#         elif (goblin.hp <= 0):
#             print "Having slain the vile best, you venture on."
#             p1.displayPlayer()
#             break
#     elif (user_choice == "magic" and p1.Class != "Mage"):
#             print "You don't know any spells!"
#     elif (user_choice == "magic" and p1.Class == "Mage" ):
#         user_choice = raw_input("What spell do you wish to use? ")
#         if (user_choice == "fire-ball"):
#             # fireBall.displayMagic()
#             fire_ball(goblin)
#             p1.mp = p1.mp - fireBall.mp
#             goblin.displayMonster()
#             monsterAttack(goblin, p1)
#             if (p1.hp <= 0):
#                 print "GAME OVER"
#                 break
#             elif (goblin.hp <= 0):
#                 print "Having slain the vile best, you venture on."
#                 p1.displayPlayer()
#                 break
#     else:
#         # escapeRoll()
#         #     break
#             from random import randint
#             rand_num = (randint(0, 10))
#             # print rand_num
#             if (rand_num < 5):
#                 print "You can't get away!"
#                 monsterAttack(goblin, p1)
#             else:
#                 print "You escaped."
#                 break

print "As you continue down the path, you notice the faint flicker of light in the distance."
print "A little further down the tunnel and you come to what appears to be a guard-post of sorts. Luckily, it is vacant."
while True:
    user_choice = raw_input("The ramshackle post is cramped and filthly. There is a pile of grimy blankets in one corner, and a wooden chest in another."
    " What do you do? ")
    if user_choice not in ("leave", "sleep", "open chest", "open"):
        print "Make another choice."
    elif (user_choice == "leave"):
        print "You sense danger lurking about. You decide to continue on your path, deeper into the mines."
        break
    elif (user_choice == "sleep"):
        print "As unappealing as the pile of musty rags looks, there is no denying your fatigue after encountering that Goblin. Using your pack as a pillow, you lay down and rest your eyes for a bit."
        p1.hp = 10
        p1.displayPlayer()
        print "You wake-up feeling recharged. There's no telling how long you were out, but it must not have been long, as the torch-light has yet to burn-out."
        print "You shoulder your pack and make your way deeper into the mine."
        break
    # elif (user_choice == "open chest" or user_choice == "open"):
    #     print "You set your gear on the cave-floor as you move to open the chest."
    #     print "It's locked."
    #     while True:
    #         user_choice = raw_input("What do you do? ")
    #         if user_choice not in ("leave", "break", "pick lock"):
    #             print "Make another choice."
    #         elif (user_choice == "leave"):
    #             print "Whatever the chest holds, you decide it isn't worth the risk to find out. You venture on."
    #         else:
    #             print "After a little bit of work, you manage to force the lock open."
    #             print "Just as you open the chest to inspect your loot, you hear a belowing roar from behind."
    #             print "You turn and snatch up your weapons, but the beast is already on you."
    #             monsterAttack(goblin, p1)
    #             goblin.displayMonster()
    #             while (goblin.hp != 0):
    #                 user_choice = raw_input("What do you do? ")
    #                 if user_choice not in ("attack", "fight", "magic", "escape", "run"):
    #                     print "Make another choice."
    #                 elif (user_choice == "attack" or user_choice == "fight"):
    #                     monsterAttack(goblin, p1)
    #                     playerAttack(p1, goblin)
    #                     if (p1.hp <= 0):
    #                         print "GAME OVER"
    #                         os.execl(sys.executable, sys.executable, *sys.argv)
    #                         break
    #                     elif (goblin.hp <= 0):
    #                         print "The beast is dead. You return to the open-chest to see what you have won."
    #                         p1.displayPlayer()
    #                         inventory.append("healing potion")
    #                         print "You retrieve a healing potion from the chest. This should help you in your journey."
    #                         print "Inventory: "
    #                         inventoryCheck()
    #                         break
    #                     elif (user_choice == "magic" and p1.Class != "Mage"):
    #                         print "You don't know any spells!"
    #                     elif (user_choice == "magic" and p1.Class == "Mage" ):
    #                         user_choice = raw_input("What spell do you wish to use? ")
    #                         if (user_choice == "fire-ball"):
    #                             fire_ball(goblin)
    #                             p1.mp = p1.mp - fireBall.mp
    #                             goblin.displayMonster()
    #                             monsterAttack(goblin, p1)
    #                             if (p1.hp <= 0):
    #                                 print "GAME OVER"
    #                                 break
    #                             elif (goblin.hp <= 0):
    #                                 print "The beast is dead. You return to the open-chest to see what you have won."
    #                                 p1.displayPlayer()
    #                                 inventory.append("healing potion")
    #                                 print "You retrieve a healing potion from the chest. This should help you in your journey."
    #                                 print "Inventory: "
    #                                 inventoryCheck()
    #                                 break
                        # else:
                        #     from random import randint
                        #     rand_num = (randint(0, 10))
                        #     if (rand_num < 5):
                        #         print "You can't get away!"
                        #         monsterAttack(goblin, p1)
                        #     else:
                        #         print "You escaped."
                        #         break

# --------------Notes/Problems that I have had to solve while working on my game.--------------
# I need a way to reset the game if there is a game over. OK
# I need a way for my characters to do combat with monsters and have their health change as they take damage. OK
# Work on creating a new object to store the player character and stats in(depending on race/class the player chooses). OK
# Make a way for the player to roll to escape from battle. If roll is unsuccessful, monster get's to attack. OK
# Make an inventory for the player, and put all of their starting items inside. OK
# Make a way for the mage character to cast his spells in battle. OK
# Make the players MP drain for each spell cast. OK
# Give the Mage character a wooden staff. OK
# When I finish the second battle, there is text "NONE" displayed. Where's this from??? OK
# ***Fix second battle. When I am prompted to make another choice, the program ends.***
