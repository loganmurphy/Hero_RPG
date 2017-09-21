from items.base import Base_Item



class Health_Potion(Base_Item):
    pass
class Mana_Potion(Base_Item):
    pass
# add an Armor item to the store. Buying an armor will add 2
# armor points to the hero - you will add "armor" as a new attribute
# to hero. Every time the hero is attacked, the amount of hit points
# dealt to him will be reduced by the value of the armor attribute.
class Armor(Base_Item):
    pass
healing_potion = Health_Potion(5)
potion_of_mana = Mana_Potion(5)
armor =Armor(2)
