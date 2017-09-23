from characters.heroes import *
from characters.base import Base_Stats
from items import *

def go_shopping(self):
    while True:
        print("Shop keeper: What do you want to do?")
        print("1. buy a health_potion for 5 gold")
        print("2. buy a potion_of_mana for 5 gold")
        print("3. buy a bomb for 8 gold")
        print("4. buy a swap for 8 gold")
        print("5. buy an evade for 10 gold")
        print("6. buy armor for 10 gold")
        print("7. leave")
        print("> ", end=' ')
        raw_input = input()
        if raw_input not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid input {}".format(raw_input))
        elif raw_input == "1":
            if self.gold >= 5:
                print("Here you are.")
                self.gold -= 5
                self.health_potion += 1
            else:
                print("You don't have enough gold!")
        elif raw_input == "2":
            if self.gold >= 5:
                print("Here you are.")
                self.gold -= 5
                self.potion_of_mana += 1
            else:
                print("You don't have enough gold!")
        elif raw_input == "3":
            if self.gold >= 8:
                print("Here you are.")
                self.gold -= 8
                self.bomb += 1
            else:
                print("You don't have enough gold!")
        elif raw_input == "4":
            if self.gold >= 8:
                print("Here you are.")
                self.gold -= 8
                self.swap += 1
            else:
                print("You don't have enough gold!")
        elif raw_input == "5":
            if self.gold >= 10:
                print("Here you are.")
                self.gold -= 10
                self.evade += 1
            else:
                print("You don't have enough gold!")
        elif raw_input == "6":
            if self.gold >= 10:
                print("Here you are.")
                self.gold -= 10
                self.armor += 2
            else:
                print("You don't have enough gold!")
        else:
          print("Come again!")
          break
