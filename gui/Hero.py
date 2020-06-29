class Hero:
    def __init__(self, nom, attaque, esquive, vie, maxVie, regeneration):
        self.nom = input("Quel est ton nom? ")
        self.attaque = attaque
        self.esquive = esquive
        self.vie_initiel = vie
        self.vie = vie
        self.maxVie = maxVie
        self.regeneration = regeneration
        self.argent = 0

    def qui_es_tu(self):
        print(f"Je suis {self.nom}. J'ai une attaque de {self.attaque}, une esquive de {self.esquive} et je me regenere de {self.regeneration} points")

    def reinitialiser_vie(self):
        self.vie = self.vie_initiel