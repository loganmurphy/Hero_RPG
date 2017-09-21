from items.base import Base_Weapon
from random import *

sword = (randrange(3,5))
dagger = (randrange(1,3))
mace = (randrange(2,3))
wooden_staff = (1)

class Sword(Base_Weapon):
    pass

class Dagger(Base_Weapon):
    pass

class Mace(Base_Weapon):
    pass

class Wooden_Staff(Base_Weapon):
    pass
