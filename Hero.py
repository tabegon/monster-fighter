class Hero:
    def __init__(self, nom, attaque, esquive, vie, regeneration):
        self.nom = nom
        self.attaque = attaque
        self.esquive = esquive
        self.vie_initiel = vie
        self.vie = vie
        self.regeneration = regeneration
        self.argent = 0

    def qui_es_tu(self):
        print(f"Je suis {self.nom} . J'ai un attaque de {self.attaque}, une esquive de {self.esquive} et je me regenere de {self.regeneration} points")

    def reinitialiser_vie(self):
        self.vie = self.vie_initiel