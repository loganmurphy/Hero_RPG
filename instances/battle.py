from PIL import Image
from characters.heroes import *
from characters.base import Base_Stats
from items import *

im = Image.open("you-are-dead-screen.jpg")

def battle(self, enemy):
    while enemy.alive() and self.alive():
        self.print_status()
        enemy.print_status()
        print("What do you want to do?")
        print("1. fight ", enemy.char_class)
        print("2. drink a potion")
        print("3. throw a bomb")
        print("4. swap")
        print("5. do nothing")
        print("6. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid input {}".format(raw_input))
        elif raw_input == "1":
            self.attack(enemy)
            if enemy.health <= 0:
                self.gold += enemy.gold
                print("The ", enemy.char_class, " is dead.")
                print("You looted {} gold pieces".format(enemy.gold))
        elif raw_input == "2":
            if self.char_class in ["warrior", "medic", "shadow"] and self.health_potion > 0:
                self.health += 5
                self.health_potion -= 1
            elif self.char_class == "mage":
                choice = input("What kind of potion do you want to drink? ")
                self.drink_potion(choice)
            else:
                print("You have no healing potions!")
        elif raw_input == "3":
            enemy.power, self.power = self.power, enemy.power
            if self.bomb > 0:
                print("Your bomb did {} damage.".format(bomb.effect))
                enemy.health -= bomb.effect
                self.bomb -= 1
            else:
                print("You have no bombs!")
        elif raw_input == "4":
            self.swap(enemy)
        elif raw_input == "5":
            pass
        elif raw_input == "6":
            print("You got away!")
            break
        if enemy.alive() and raw_input != "4":
            enemy.attack(self)
            if self.health <= 0:
                im.show()
                print("You are dead.")
