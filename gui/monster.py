from random import *
class Monster:
    def __init__(self):
        self.attaque = randint(10, 30)
        self.regeneration = randint(10, 30)
        self.vie = randint(50, 250)
        self.MaxVie = self.vie
