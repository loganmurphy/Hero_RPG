class Base_Stats:
    def __init__(self, health, power, char_class):
        self.health = health
        self.power = power
        self.char_class = char_class
    def attack(self, enemy):
        enemy.health -= self.power
        print("You do {} damage to the {}.".format(self.power, enemy.char_class))
    def alive(self):
        if self.health > 0:
            # print("I'm alive!")
            return True
    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))
