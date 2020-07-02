import pygame
from pygame.locals import *
from monster import *
from Hero import *

pygame.init()

monstre2 = Monster()
perssonage = Hero("test", 0, 0, 30, 30, 30, "ok")

monster_image = pygame.image.load("./gui/monster.png")
monster_image = pygame.transform.scale(monster_image, (150, 150))

fond = pygame.image.load("./gui/Fond/entree.png")
fond = pygame.transform.scale(fond, (1600, 900))

red = (255, 0, 0)
white = (255, 255, 255)
yellow = (255, 209, 0)
green = (36, 217, 0)
blue = (0, 35, 255)
orange = (255, 120, 0)

#________________________________________________________________________________________

#Ouverture de la fenêtre Pygame

pygame.display.set_caption("► ► ► Monster fighter - Jeu Méga cool ◄ ◄ ◄")
fenetre = pygame.display.set_mode((1600, 900), RESIZABLE)

#___________________________________________________________________________________________

def creaTexteObj(texte, police, couleur) :
	texteSurface = police.render(texte,True,couleur)
	return texteSurface, texteSurface.get_rect()

# FAIT

def texte(texte, coordonée, police, couleur):
	GOTexte = pygame.font.Font('./gui/Skate_Brand.otf', police)
	GOTexteSurf, GOTexteRect = creaTexteObj(texte, GOTexte, couleur)
	GOTexteRect.center = (coordonée)
	fenetre.blit(GOTexteSurf, GOTexteRect)
	pygame.display.flip()

# FAIT


def efface_texte():
	fenetre.blit(monster_image, (1450, 0))
	fenetre.blit(fond, (0, 0))


def health_bar(surface):
		texte(f"{monstre2.vie}/{monstre2.MaxVie}", (1300, 40), 30, red)
		# definir notre couleur (vert clair)
		color_bar = (111, 210, 46)
		# définir notre couleur de l'arrière plan de la jauge (gris foncée)
		back_color_bar = (60, 63, 60)
		# definir position ainsi que la largeur et de l'epesseur
		bar_position2 = [1425, 70, (monstre2.vie - (monstre2.vie * 2)), 20]
		# definir la position de la jauge ainsi que la largeur et de l'epesseur
		back_bar_position2 = [1425, 70, (monstre2.MaxVie - (monstre2.MaxVie * 2)), 20]
		pygame.draw.rect(surface, back_color_bar, back_bar_position2)
		pygame.draw.rect(surface, color_bar, bar_position2)
		if monstre2.vie <= 100:
			pygame.draw.rect(surface, orange, bar_position2)

		if monstre2.vie <= 50:
			pygame.draw.rect(surface, red, bar_position2)

def attaque_monstre2():
		global apres
		efface_texte()
		action_boss = randint(0, 1)
		if action_boss == 0:
				attack_b = randint(0, monstre2.attaque)
				efface_texte()
				texte(f'Le monstre vous a attaqué de {attack_b}', (550, 50), 30, red)
				personnage.vie -= attack_b
				if apres == 1:
					esquive = randint(0, (25 // personnage.esquive))
					if esquive == 0:
						personnage.vie += attack_b
						efface_texte()
						texte("Vous avez esquivez le coup", (600, 100), 30, green)
						time.sleep(3.0)
						apres = 0
				time.sleep(3.0)
				efface_texte()
		if action_boss == 1:
			vies_b = randint(0, monstre2.regeneration)
			efface_texte()
			texte(f'Le monstre à regagné {vies_b} de vies', (550, 50), 30, white)
			monstre2.vie += vies_b
			if monstre2.vie < monstre2.MaxVie:
				time.sleep(3.0)
			if monstre2.vie > monstre2.MaxVie:
				monstre2.vie = monstre2.MaxVie

#______________________________________________________

fenetre.blit(fond, (0, 0))
fenetre.blit(monster_image, (1450, 0))
#______________________________________________________

#BOUCLE INFINIE
continuer = 1
while continuer:
	
	for event in pygame.event.get():	#Attente des événements
		health_bar(fenetre)	
		if event.type == MOUSEBUTTONDOWN:
			x,y = event.pos
			print(event)

			health_bar(fenetre)

		if event.type == QUIT:
			continuer = 0
	#Rafraichissement
	pygame.display.flip()