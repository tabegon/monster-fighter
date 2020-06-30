# Les importations

import pygame
from pygame.locals import *
from Hero import *
import time 
from random import *
from monster import *

pygame.init()

# Les variables

red = (255, 0, 0)
white = (255, 255, 255)
yellow = (255, 209, 0)
green = (36, 217, 0)
blue = (0, 35, 255)
monstre = Monster(20, 5, 50, 70)
sleep = 4.0
hero = False
attack_speciale = 2
tour = 1

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

def Choix_hero(position, guerrier, mage, archer):
	x, y = position
	global personnage
	if guerrier.get_rect(x = 1450, y = 0).collidepoint(x, y):
		efface_texte()
		personnage = Hero('Guerrier', 20, 10, 30, 30, 5)
		texte(personnage.qui_es_tu(), (800, 50), 30, red)
		hero = True

	if mage.get_rect(x = 1300, y = 0).collidepoint(x, y):
		efface_texte()
		personnage = Hero('Mage', 10, 5, 30, 30, 20)
		texte(personnage.qui_es_tu(), (800, 50), 30, red)
		hero = True


	if archer.get_rect(x = 1150, y = 0).collidepoint(x, y):
		efface_texte()
		personnage = Hero('Archer', 5, 20, 30, 30, 10)
		texte(personnage.qui_es_tu(), (800, 50), 30, red)
		hero = True

def Choix_boutons():
	global sleep, attack_speciale
	if attaque.get_rect(x = 750, y = 700).collidepoint(x, y):
		efface_texte()
		attack = randint(0, personnage.attaque)
		coup_critique = randint(0, 1)
		if coup_critique == 1:
			attack += 20
			sleep += 4.0
			texte("Vous avez donner un coup critique", (500, 50), 30, yellow)
		texte(f'Vous avez attaquer de {attack}', (500, 100), 30, blue)
		monstre.vie -= attack
		if monstre.vie > 0:
			time.sleep(sleep)
			sleep = 4
			efface_texte()
			texte(f"Le monstre lui reste {monstre.vie} vies", (500, 50), 30, red)
			Attaque_monstre()
		else:
			efface_texte()
			texte("Vous avez gagnez", (700, 500), 100, green)

	if gagné_vie.get_rect(x = 925, y = 700).collidepoint(x, y):
		efface_texte()
		vie_regagner = randint(personnage.regeneration, personnage.regeneration + 20)
		texte(f'Vous avez regagné {vie_regagner} de vies', (500, 50), 30, green)
		time.sleep(sleep)
		personnage.vie = personnage.vie + vie_regagner
		efface_texte()
		texte(f"Vous avez {personnage.vie} de vies", (500, 50), 30, white)
		Attaque_monstre()

	if esquive.get_rect(x = 1100, y = 700).collidepoint(x, y):
		efface_texte()
		texte("esquive marche", (550, 150), 50, red)

	if attaque_spéciale.get_rect(x = 1275, y = 700).collidepoint(x, y):
		efface_texte()
		if attack_speciale == 0:
			texte("Vous ne pouvez pas utilisez votre attaque spéciale plus de deux fois", (700, 50), 30, red)
			texte("Vous n'avez pas attaqué", (500, 100), 30, red)
		if attack_speciale > 0:
			attack_speciale = attack_speciale - 1
			coup_spécial = randint(personnage.attaque, 200)
			efface_texte
			texte(f"vous avez attaquer de {coup_spécial}", (500, 50), 30, green)
			monstre.vie -= coup_spécial
			time.sleep(4.0)

		if monstre.vie > 0:
			efface_texte()
			texte(f"Le monstre lui reste {monstre.vie} vies", (500, 50), 30, red)
			Attaque_monstre()
		else:
			efface_texte()
			texte("Vous avez gagnez", (700, 500), 100, green)

	if shop.get_rect(x = 1450, y = 700).collidepoint(x, y):
		efface_texte()
		texte("shop marche", (550, 150), 50, white)

def Attaque_monstre():
	time.sleep(5.0)
	efface_texte()
	action_boss = randint(0, 1)
	if action_boss == 0:
			attack_b = randint(0, monstre.attaque)
			efface_texte()
			texte(f'Le monstre vous a attaqué de {attack_b}', (550, 50), 30, red)
			personnage.vie -= attack_b
			time.sleep(4.0)
			efface_texte()
			texte(f"Vous avez {personnage.vie} vies", (550, 50), 30, red)
	if action_boss == 1:
		vies_b = randint(0, monstre.regeneration)
		efface_texte()
		texte(f'Le monstre à regagné {vies_b} de vies', (550, 50), 30, white)
		monstre.vie += vies_b
		time.sleep(4.0)
		efface_texte()
		texte(f'Le monstre lui reste {monstre.vie} vies', (550, 50), 30, white)

def fin_de_vie():
	global tour
	if monstre.vie <= 0:
		monstre.vie = monstre.MaxVie
		personnage.vie = personnage.maxVie
		tour += 1
		texte(f"Vous êtes maintenant à l'étage {tour}", (500, 50), 50, yellow)
	if personnage.vie <= 0:
		monstre.vie = monstre.MaxVie
		personnage.vie = personnage.maxVie
		tour -= 1
		texte(f"Vous avez desendu d'un étage maintenant vous êtes à l'étage n°{tour}", (700, 50), 50, red)
		



#________________________________________________________________________________________________________

#Ouverture de la fenêtre Pygame
pygame.display.set_caption("Monster fihgter - Jeu Méga cool")
fenetre = pygame.display.set_mode((1600, 900), RESIZABLE)

#________________________________________________________________________________________________________

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

#________________________________________________________________________________________________________ 

texte("Quel métier choisis tu? ", (950, 40), 40, blue)
#Rafraîchissement de l'écran
pygame.display.flip()

#________________________________________________________________________________________________________ 

#________________________________________________________________________________________________________

#BOUCLE INFINIE
continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		if event.type == MOUSEBUTTONDOWN:
			x,y = event.pos
			if hero == False:
				Choix_hero(event.pos, Guerrier, Mage, archer)		
			Choix_boutons()
			fin_de_vie()


		if event.type == QUIT:
			continuer = 0
	#Rafraichissement
	pygame.display.flip()