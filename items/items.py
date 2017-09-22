from items.base import Base_Item

class Health_Potion(Base_Item):
    pass
class Mana_Potion(Base_Item):
    pass
class Armor(Base_Item):
    pass

# add an Evade item to the store. Buying an "evade" will add 2 evade points
# to the hero - another new attribute on the Hero object. The more evade he has,
# the more probable that he will evade an enemy attack unscathed. For example:
# 2 evade points: 10% probably of avoiding attack, 4 evade points: 15% probability
# of avoiding attack. It should never be possible to reach 100% evasion though.
class Evade(Base_Item):
    pass

healing_potion = Health_Potion(5)
potion_of_mana = Mana_Potion(5)
armor = Armor(2)
