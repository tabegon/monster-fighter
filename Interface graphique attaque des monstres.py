
import pygame
from pygame.locals import *

pygame.init()

def creaTexteObj(texte, Police):
	texteSurface = Police.render(texte, True)
	return texteSurface, texteSurface.get_rect()

def message (texte):
	GOTexte = pygame.font.Font('Skate Brand.otf', 30)
	GOTexteSurf, GOTexteRect = creaTexteObj(texte, GOTexte)
	GOTexteRect.center = ((0, 0)-50)
	fenetre.blit(GOTexteSurf, GOTexteRect)
	pygame.display.flip()


#Ouverture de la fenêtre Pygame
pygame.display.set_caption("Monster fighter")
fenetre = pygame.display.set_mode((1600, 900), FULLSCREEN)

#Chargement et collage du fond
fond = pygame.image.load("./entrée.png").convert()
fond = pygame.transform.scale(fond, (1600, 900))
fenetre.blit(fond, (0,0))
#Chargement et collage des boutons
bouton = pygame.image.load("./boutique.png").convert()
bouton = pygame.transform.scale(bouton, (150, 150))
fenetre.blit(bouton, (1450, 750))
attaque_spéciale = pygame.image.load("./attaque spéciale.png")
attaque_spéciale = pygame.transform.scale(attaque_spéciale, (150, 150))
fenetre.blit(attaque_spéciale, (1275, 750))
esquive = pygame.image.load("./esquive.png")
esquive = pygame.transform.scale(esquive, (150, 150))
fenetre.blit(esquive, (1100,750))
gagné_vie = pygame.image.load("./re-gagner de la vie.png")
gagné_vie = pygame.transform.scale(gagné_vie, (150, 150))
fenetre.blit(gagné_vie, (925, 750))
attaque = pygame.image.load("./Attaque.png")
attaque = pygame.transform.scale(attaque, (150, 150))
fenetre.blit(attaque, (750, 750))
message("Test")

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		if event.type == QUIT:
			continuer = 0
	#Rafraichissement
	pygame.display.flip()