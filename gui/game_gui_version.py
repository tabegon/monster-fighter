
import pygame
from pygame.locals import *

pygame.init()

def creaTexteObj(texte, police) :
	white = (255, 255, 255)
	texteSurface = police.render(texte,True,white)
	return texteSurface, texteSurface.get_rect()

def message (texte, coordonée, police):
	GOTexte = pygame.font.Font('./gui/Skate_Brand.otf', police)
	GOTexteSurf, GOTexteRect = creaTexteObj(texte, GOTexte)
	GOTexteRect.center = (coordonée)
	fenetre.blit(GOTexteSurf, GOTexteRect)
	pygame.display.flip()



#Ouverture de la fenêtre Pygame
pygame.display.set_caption("Monster fihgter - Jeu Méga cool")
fenetre = pygame.display.set_mode((1600, 900), RESIZABLE)

#Chargement et collage du fond
fond = pygame.image.load("./gui/Fond/entrée.png").convert()
fond = pygame.transform.scale(fond, (1600, 900))
fenetre.blit(fond, (0,0))
#Chargement et collage des boutons
bouton = pygame.image.load("./gui/Boutons/boutique.png").convert()
bouton = pygame.transform.scale(bouton, (150, 150))
fenetre.blit(bouton, (1450, 700))
attaque_spéciale = pygame.image.load("./gui/Boutons/attaque spéciale.png")
attaque_spéciale = pygame.transform.scale(attaque_spéciale, (150, 150))
fenetre.blit(attaque_spéciale, (1275, 700))
esquive = pygame.image.load("./gui/Boutons/esquive.png")
esquive = pygame.transform.scale(esquive, (150, 150))
fenetre.blit(esquive, (1100,700))
gagné_vie = pygame.image.load("./gui/Boutons/re-gagner de la vie.png")
gagné_vie = pygame.transform.scale(gagné_vie, (150, 150))
fenetre.blit(gagné_vie, (925, 700))
attaque = pygame.image.load("./gui/Boutons/Attaque.png")
attaque = pygame.transform.scale(attaque, (150, 150))
fenetre.blit(attaque, (750, 700))


#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		print(event)

		if event.type == MOUSEBUTTONDOWN:
			message("", (550, 150), 50 )
		if event.type == QUIT:
			continuer = 0
	#Rafraichissement
	pygame.display.flip()


