
import pygame
from pygame.locals import *

pygame.init()

red = (255, 0, 0 )
white = (255, 255, 255)
yellow = (255, 209, 0)
green = (36, 217, 0)

def creaTexteObj(texte, police, couleur) :
	texteSurface = police.render(texte,True,couleur)
	return texteSurface, texteSurface.get_rect()

def message (texte, coordonée, police, couleur):
	GOTexte = pygame.font.Font('./gui/Skate_Brand.otf', police)
	GOTexteSurf, GOTexteRect = creaTexteObj(texte, GOTexte, couleur)
	GOTexteRect.center = (coordonée)
	fenetre.blit(GOTexteSurf, GOTexteRect)
	pygame.display.flip()


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

#Collages
fenetre.blit(fond, (0,0))						#Fond
fenetre.blit(shop, (1450, 700))					#Shop
fenetre.blit(attaque_spéciale, (1275, 700))		#Attaque spéciale
fenetre.blit(esquive, (1100,700))				#Esquive
fenetre.blit(gagné_vie, (925, 700))				#Re-gagne de la vie
fenetre.blit(attaque, (750, 700))				#Attaque

#_______________________________________________________________________________________________________ 

test = "je test si ça marche"
#Rafraîchissement de l'écran
pygame.display.flip()

#________________________________________________________________________________________________________ 

#BOUCLE INFINIE
continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		print(event)

		if event.type == MOUSEBUTTONDOWN:
			if attaque.collipoint:
				message(f"bonjour regarde {test}", (550, 150), 300, green)
		if event.type == QUIT:
			continuer = 0
	#Rafraichissement
	pygame.display.flip()


