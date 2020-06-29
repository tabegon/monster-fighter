
import pygame
from pygame.locals import *
from Hero import *

pygame.init()

red = (255, 0, 0 )
white = (255, 255, 255)
yellow = (255, 209, 0)
green = (36, 217, 0)
blue = (0, 35, 255)

def creaTexteObj(texte, police, couleur) :
	texteSurface = police.render(texte,True,couleur)
	return texteSurface, texteSurface.get_rect()

def texte(texte, coordonée, police, couleur):
	GOTexte = pygame.font.Font('./gui/Skate_Brand.otf', police)
	GOTexteSurf, GOTexteRect = creaTexteObj(texte, GOTexte, couleur)
	GOTexteRect.center = (coordonée)
	fenetre.blit(GOTexteSurf, GOTexteRect)
	pygame.display.flip()

def efface_texte():
	fenetre.blit(fond, (0,0))
	fenetre.blit(shop, (1450, 700))
	fenetre.blit(attaque_spéciale, (1275, 700))
	fenetre.blit(esquive, (1100,700))
	fenetre.blit(gagné_vie, (925, 700))
	fenetre.blit(attaque, (750, 700))




#________________________________________________________________________________________________

#Ouverture de la fenêtre Pygame
pygame.display.set_caption("Monster fihgter - Jeu Méga cool")
fenetre = pygame.display.set_mode((1600, 900), RESIZABLE)

#_________________________________________________________________________________________________

#Chargements
fond = pygame.image.load("./gui/Fond/entrée.png").convert()
fond = pygame.transform.scale(fond, (1600, 900))

attaque = pygame.image.load("./gui/Boutons/Attaque.png")
attaque = pygame.transform.scale(attaque, (150, 150))

shop = pygame.image.load("./gui/Boutons/boutique.png").convert()
shop = pygame.transform.scale(shop, (150, 150))

attaque_spéciale = pygame.image.load("./gui/Boutons/attaque spéciale.png")
attaque_spéciale = pygame.transform.scale(attaque_spéciale, (150, 150))

esquive = pygame.image.load("./gui/Boutons/esquive.png")
esquive = pygame.transform.scale(esquive, (150, 150))

gagné_vie = pygame.image.load("./gui/Boutons/re-gagner de la vie.png")
gagné_vie = pygame.transform.scale(gagné_vie, (150, 150))

Guerrier = pygame.image.load("./gui/Boutons/guerrier.png")
Guerrier = pygame.transform.scale(Guerrier, (150, 150))

Mage = pygame.image.load("./gui/Boutons/Mage.png")
Mage = pygame.transform.scale(Mage, (150, 150))

archer = pygame.image.load("./gui/Boutons/archer.png")
archer = pygame.transform.scale(archer, (150, 150))

# Collages
fenetre.blit(fond, (0,0))						# Fond
fenetre.blit(Guerrier, (1450, 0))				# Guerrier
fenetre.blit(Mage, (1300, 0))					# Mage
fenetre.blit(archer, (1150, 0))					# Archer

#_______________________________________________________________________________________________________ 

texte("Quel métier choisi tu? ", (950, 40), 40, blue)
reponse = False
#Rafraîchissement de l'écran
pygame.display.flip()

#________________________________________________________________________________________________________ 

#_____________________________________________________________________________________________________________________

#BOUCLE INFINIE
continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		if event.type == MOUSEBUTTONDOWN:
			x, y = event.pos
		
			if attaque.get_rect(x = 750, y = 700).collidepoint(x, y):
				print("caca de la vaca")
				efface_texte()
				is_appuyer_button(3,attaque)
				texte("Attaque marche", (550, 150), 50, green)

			if Guerrier.get_rect(x = 1450, y = 0).collidepoint(x, y):
				efface_texte()
				Hero('Guerrier', 10, 20, 30, 30, 5)
				Hero.qui_es_tu()

			if Mage.get_rect(x = 1300, y = 0).collidepoint(x, y):
				efface_texte()
				Hero('Mage', 10, 5, 30, 30, 20)
			else:
				texte("il n'est pas ici le bouton, tampis", (300, 170), 30, white)
		if event.type == QUIT:
			continuer = 0
	#Rafraichissement
	pygame.display.flip()