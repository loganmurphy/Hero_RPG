from items.base import Base_Item
from characters import *
from random import randrange

class Health_Potion(Base_Item):
    pass

class Mana_Potion(Base_Item):
    pass

# class Armor(Base_Item):
#     pass

class Bomb(Base_Item):
    pass

healing_potion = Health_Potion(5)
potion_of_mana = Mana_Potion(5)
# armor = Armor(2)
bomb = Bomb(randrange(3,8))
