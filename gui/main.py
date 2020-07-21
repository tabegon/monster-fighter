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
orange = (255, 120, 0)

attack_speciale = 2
tour = 1
sleep = 4.0
apres = 0

rien = pygame.image.load("./gui/rien.png")
rien = pygame.transform.scale(rien, (100, 100))

monstre = Monster()
monstre2 = Monster()
personnage = Hero("rien", 5, 5, 30, 30, 5, rien)

hero = False
is_playing = False
deuxieme_monstre = False
attaque_qui = False


battements = pygame.mixer.Sound("./gui/battements.wav")
son = pygame.mixer.Sound("./gui/fight.wav")

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
	fenetre.blit(barre, (0, 700))
	attaque_speciale_utiliser()
	esquive_utiliser()
	fenetre.blit(gagné_vie, (925, 700))
	fenetre.blit(attaque, (750, 700))
	fenetre.blit(monster_image, (0, 0))
	health_bar(fenetre)
	fenetre.blit(personnage.image, (20, 725))
	if deuxieme_monstre == 1:
		fenetre.blit(monster_image, (1450, 0))
		deux_monstre()
	fenetre.blit(case, (1275, 655))
	ta_vie()
	texte(f"{personnage.esquive}", (385, 746), 30, white)
	texte(f"{tour}", (550, 746), 30, white)
	texte(f"{personnage.attaque}", (248, 819), 30, white)
	texte(f"{personnage.regeneration}", (413, 819), 30, white)
	texte(f"{personnage.argent}", (564, 819), 30, white)
	texte(f"{attack_speciale}", (1345, 679), 30, blue)

def Choix_hero(position, guerrier, mage, archer):
	x, y = position
	global personnage
	if guerrier.get_rect(x = 1450, y = 0).collidepoint(x, y):
		efface_texte()
		personnage = Hero('guerrier', 20, 10, 30, 50, 5, guerrier_image)
		texte(personnage.qui_es_tu(), (800, 200), 30, blue)
		fenetre.blit(guerrier_image, (20, 725))
		hero = True

	if mage.get_rect(x = 1300, y = 0).collidepoint(x, y):
		efface_texte()
		personnage = Hero('mage', 10, 5, 30, 50, 20, mage_image)
		texte(personnage.qui_es_tu(), (800, 200), 30, blue)
		hero = True


	if archer.get_rect(x = 1150, y = 0).collidepoint(x, y):
		efface_texte()
		personnage = Hero('Archer', 5, 20, 30, 50, 10, archer_image)
		texte(personnage.qui_es_tu(), (800, 200), 30, blue)
		hero = True

def Choix_boutons():
	global sleep, attack_speciale, son
	if attaque.get_rect(x = 750, y = 700).collidepoint(x, y):
		attack = randint(0, personnage.attaque)
		coup_critique = randint(0, 1)
		son.play()
		if coup_critique == 1:
			attack += 20
			sleep += 4.0
			texte("Vous avez donner un coup critique", (700, 50), 30, yellow)
		texte(f'Vous avez attaquer de {attack}', (700, 100), 30, blue)
		monstre.vie -= attack

		if monstre.vie > 0:
			time.sleep(3.0)
			sleep = 4
			efface_texte()
			Attaque_monstre()
		else:
			fin_de_vie()
			if monstre2.vie > 0:
				attaque_monstre2()
			else:
				fin_de_vie()
		

	if gagné_vie.get_rect(x = 925, y = 700).collidepoint(x, y):
		efface_texte()
		vie_regagner = randint(personnage.regeneration, personnage.regeneration + 20)
		personnage.vie = personnage.vie + vie_regagner
		if personnage.vie < personnage.maxVie:
			texte(f'Vous avez regagné {vie_regagner} de vies', (700, 50), 30, green)
			time.sleep(3.0)
			efface_texte()
		if personnage.vie >= personnage.maxVie:
			texte("Vous ne pouvez plus regagnez de la vie", (700, 50), 30, red)
			time.sleep(3.0)
			personnage.vie = personnage.maxVie
			efface_texte()
		Attaque_monstre()

	if bouton_esquive.get_rect(x = 1100, y = 700).collidepoint(x, y):
		global apres
		efface_texte()
		apres = 1
		esquive_utiliser()
		Attaque_monstre()

	if attaque_spéciale.get_rect(x = 1275, y = 700).collidepoint(x, y):
		efface_texte()
		if attack_speciale == 0:
			texte("Vous ne pouvez pas utilisez votre attaque spéciale plus de deux fois", (800, 50), 30, red)
			texte("Vous n'avez pas attaqué", (700, 100), 30, red)
			time.sleep(4.0)
		if attack_speciale > 0:
			pygame.mixer.music.load("./gui/canon.mp3")
			pygame.mixer.music.play()
			attack_speciale = attack_speciale - 1
			coup_spécial = randint(personnage.attaque, personnage.attaque + 200)
			efface_texte
			texte(f"vous avez attaquer de {coup_spécial}", (700, 50), 30, green)
			if deuxieme_monstre != 1:
				monstre.vie -= coup_spécial
			else:
				monstre.vie -= coup_spécial
				monstre2.vie -= coup_spécial
			time.sleep(3.0)
			pygame.mixer.music.load("./gui/musique.mp3")
			pygame.mixer.music.play()
			pygame.mixer.music.queue("./gui/musique2.mp3")

		if monstre.vie > 0:
			efface_texte()
			Attaque_monstre()
		else:
			efface_texte()
			texte("Vous avez gagnez", (700, 500), 100, green)


def Attaque_monstre():
	global apres
	efface_texte()
	action_boss = randint(0, 1)
	if action_boss == 0:
			attack_b = randint(0, monstre.attaque)
			efface_texte()
			texte(f'Le monstre vous a attaqué de {attack_b}', (550, 50), 30, red)
			personnage.vie -= attack_b
			if apres == 1:
				esquive = randint(0, (75 // personnage.esquive))
				if esquive == 0:
					personnage.vie += attack_b
					efface_texte()
					texte("Vous avez esquivez le coup", (600, 100), 30, green)					
					apres = 0
			time.sleep(3.0)
			efface_texte()
			if deuxieme_monstre == 1:
				attaque_monstre2()
	if action_boss == 1:
		vies_b = randint(0, monstre.regeneration)
		efface_texte()
		texte(f'Le monstre à regagné {vies_b} de vies', (550, 50), 30, white)
		monstre.vie += vies_b
		if monstre.vie < monstre.MaxVie:
			time.sleep(3.0)
		if monstre.vie > monstre.MaxVie:
			monstre.vie = monstre.MaxVie
		efface_texte()
		if deuxieme_monstre == 1:
			attaque_monstre2()

def fin_de_vie():
	global tour, monstre, deuxieme_monstre, monstre2
	if deuxieme_monstre != 1:
		if monstre.vie <= 0:
			monstre.vie = 0
			efface_texte()
			monstre.vie = monstre.MaxVie
			personnage.vie = personnage.maxVie
			tour += 1
			texte(f"Vous êtes maintenant à l'étage n°{tour}", (700, 50), 50, yellow)
			monstre = Monster()
			time.sleep(3.0)
			efface_texte()
			deuxieme_monstre = randint(0, 3)
			if deuxieme_monstre == 1:
				deux_monstre()
				monstre2 = Monster()

	if deuxieme_monstre == 1:
		if monstre.vie <= 0:
			monstre.vie = 0

		if monstre2.vie <= 0:
			monstre2.vie = 0
		
		if monstre.vie and monstre2.vie <= 0:
			efface_texte()
			monstre.vie = monstre.MaxVie
			monstre2.vie = monstre2.MaxVie
			personnage.vie = personnage.maxVie
			tour += 1
			texte(f"Vous êtes maintenant à l'étage n°{tour}", (700, 50), 50, yellow)
			monstre = Monster()
			monstre2 = Monster()
			time.sleep(3.0)
			efface_texte()


			argent = randint(0, 1)
			if argent == 0:
				argent_gagne = randint(0, 50)
				texte(f"Le monstre à relaché {argent_gagne} pieces d'or en mourant", (700, 100), 30, green)
				time.sleep(3.0)
				efface_texte()
				personnage.argent += argent_gagne
			coffre = randint(0, 1)
			if coffre == 0:
				ta_le_coffre()

	if personnage.vie <= 0:
		efface_texte()
		monstre.vie = monstre.MaxVie
		personnage.reinitialiser_vie()
		tour -= 1
		texte(f"Vous avez desendu d'un étage maintenant vous êtes à l'étage n°{tour}", (900, 50), 50, red)
		time.sleep(3.0)
		monstre2.vie = 0
		monstre2.vie = monstre2.MaxVie
		if tour == 0:
			pygame.QUIT()
		if tour == 20:
			texte("Vous avez gagnez", (700, 400), 50, green)

	
def health_bar(surface):
		global bar_position
		texte(f"{monstre.vie}/{monstre.MaxVie}", (210, 40), 30, red)
		# ► ► ► ► ► ► ► ► ► ► ► ► 1er Monstre  ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄


		# definir notre couleur (vert clair)
		color_bar = (111, 210, 46)
		# définir notre couleur de l'arrière plan de la jauge (gris foncée)
		back_color_bar = (60, 63, 60)

		# definir position ainsi que la largeur et de l'epesseur
		bar_position = [160, 70, monstre.vie, 20]
		# definir la position de la jauge ainsi que la largeur et de l'epesseur
		back_bar_position = [160, 70, monstre.MaxVie, 20]

		# dessiner notre barre
		pygame.draw.rect(surface, back_color_bar, back_bar_position)
		pygame.draw.rect(surface, color_bar, bar_position)

		VieBoss()
		
def ta_vie():
	global battements
	if personnage.vie > 10:
		pygame.mixer.stop()
	if personnage.vie > 0:
		texte(f"{personnage.vie}", (230, 746), 30, white)
		if personnage.vie == personnage.maxVie:
			texte(f"{personnage.vie}", (230, 746), 30, green)
			fenetre.blit(gagné_vie2, (925, 700))

		if personnage.vie <= 20:
			texte(f"{personnage.vie}", (230, 746), 30, orange)
			fenetre.blit(gagné_vie, (925, 700))
		if personnage.vie <= 10:
			texte(f"{personnage.vie}", (230, 746), 30, red)
			battements.play()

	if personnage.vie <= 0:
		texte("Mort !", (255, 746), 30, blue)

def ta_le_coffre():
	global attack_speciale
	# qu'est ce qu'il y a dans le coffre(attaque, argent, attaque spéciale, esquive, regeneration)
	dans_coffre = randint(0, 4)
	fenetre.blit(coffre_fermee, (571, 207))
	texte("Dans le coffre il y a:", (600, 50), 30, blue)
	time.sleep(2.0)
	efface_texte()
	fenetre.blit(coffre_ouvert, (571, 207))
	if dans_coffre == 0:
		argent_gagne = randint(50, 100)
		texte(f"{argent_gagne} pièces d'or", (600, 100), 30, blue)
		attaque_gagne = randint(2, 10)
		texte(f"{attaque_gagne} d'attaque", (600, 200), 30, blue)
		personnage.argent += argent_gagne
		personnage.attaque += attaque_gagne
	if dans_coffre == 1:
		boules_speciale_gagne = randint(1, 4)
		texte(f"{boules_speciale_gagne} boules spéciales", (600, 100), 30, blue)
		argent_gagne = randint(50, 100)
		texte(f"{argent_gagne} pièces d'or", (600, 200), 30, blue)
		personnage.argent += argent_gagne
		attack_speciale += boules_speciale_gagne
	if dans_coffre == 2:
		argent_gagne = randint(50, 100)
		texte(f"{argent_gagne} pièces d'or", (600, 100), 30, blue)
		esquive_gagne = randint(10, 30)
		texte(f"{esquive_gagne} d'esquive", (600, 200), 30, blue)
		personnage.argent += argent_gagne
		personnage.esquive += esquive_gagne
	if dans_coffre == 3:
		argent_gagne = randint(50, 100)
		texte(f"{argent_gagne} pièces d'or", (600, 100), 30, blue)
		vie_gagne = randint(10, 30)
		texte(f"{vie_gagne} vies (t'enlève les unités pour combien de pomme d'or)", (600, 200), 30, blue)

		personnage.argent += argent_gagne
		personnage.maxVie += vie_gagne
	if dans_coffre == 4:
		argent_gagne = randint(50, 100)
		texte(f"{argent_gagne} pièces d'or", (600, 100), 30, blue)
		regeneration_gagner = randint(10, 20)
		texte(f"{regeneration_gagner} de régeneration", (600, 200), 30, blue)
		personnage.argent += argent_gagne
		personnage.regeneration += regeneration_gagner
	time.sleep(3.0)
	efface_texte()

def attaque_monstre2():
		global apres
		efface_texte()
		action_boss = randint(0, 1)
		if action_boss == 0:
				attack_b = randint(0, monstre2.attaque)
				efface_texte()
				texte(f'Le 2eme monstre vous a attaqué de {attack_b}', (550, 50), 30, red)
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
			texte(f'Le 2eme monstre à regagné {vies_b} de vies', (550, 50), 30, white)
			monstre2.vie += vies_b
			time.sleep(3.0)
			if monstre2.vie > monstre2.MaxVie:
				monstre2.vie = monstre2.MaxVie

def VieBoss():
	# ► ► ► ► ► ► ► ► ► ► ► ► 1er Monstre  ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄ ◄


	if monstre.vie <= 100:
		pygame.draw.rect(fenetre, orange, bar_position)

	if monstre.vie <= 50:
		pygame.draw.rect(fenetre, red, bar_position)


def esquive_utiliser():
	if apres == 1:
		fenetre.blit(esquive1, (1100,700))
	else:
		fenetre.blit(bouton_esquive, (1100,700))

def attaque_speciale_utiliser():
	if attack_speciale > 0:
		fenetre.blit(attaque_spéciale, (1275, 700))
	else:
		fenetre.blit(attaque_speciale2, (1275, 700))

def commencement():
	global is_playing
	for event in pygame.event.get():	#Attente des événements
		x,y = event.pos
		fenetre.blit(banniere, (475, 150))
		fenetre.blit(play, (520, 330))
		if play.get_rect(x = 520, y = 330).collidepoint(x, y):
			is_playing = True

def apres_play():
	texte("Quel métier choisis tu? ", (950, 40), 40, blue)
	#Rafraîchissement de l'écran
	pygame.display.flip()
	pygame.mixer.music.load("./gui/musique.mp3")
	pygame.mixer.music.queue("./gui/musique2.mp3")
	pygame.mixer.music.play()

	fenetre.blit(barre, (0, 700))
	fenetre.blit(monster_image, (0, 0))
	fenetre.blit(guerrier, (1450, 0))				# guerrier
	fenetre.blit(mage, (1300, 0))					# mage
	fenetre.blit(archer, (1150, 0))					# Archer

def deux_monstre():
	# BARRE DE VIES
	texte(f"{monstre2.vie}/{monstre2.MaxVie}", (1300, 40), 30, red)
	# definir notre couleur (vert clair)
	color_bar = (111, 210, 46)

	# définir notre couleur de l'arrière plan de la jauge (gris foncée)
	back_color_bar = (60, 63, 60)

	# definir position ainsi que la largeur et de l'epesseur

	bar_position2 = [1425, 70, (monstre2.vie - (monstre2.vie * 2)), 20]

	# definir la position de la jauge ainsi que la largeur et de l'epesseur

	back_bar_position2 = [1425, 70, (monstre2.MaxVie - (monstre2.MaxVie * 2)), 20]

	pygame.draw.rect(fenetre, back_color_bar, back_bar_position2)
	pygame.draw.rect(fenetre, color_bar, bar_position2)

	if monstre2.vie <= 100:
		pygame.draw.rect(fenetre, orange, bar_position2)

	if monstre2.vie <= 50:
		pygame.draw.rect(fenetre, red, bar_position2)


	# Ton attaque
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_1:
				attaque_qui = 1
			if event.key == K_2:
				attaque_qui = 2


#________________________________________________________________________________________________________

#Ouverture de la fenêtre Pygame

pygame.display.set_caption("► ► ► Monster fighter - Jeu Méga cool ◄ ◄ ◄")
fenetre = pygame.display.set_mode((1600, 900), RESIZABLE)

#________________________________________________________________________________________________________

#Chargements
fond = pygame.image.load("./gui/Fond/entree.png").convert()
fond = pygame.transform.scale(fond, (1600, 900))
	
attaque = pygame.image.load("./gui/Boutons/Attaque.png")
attaque = pygame.transform.scale(attaque, (150, 150))
	
attaque_spéciale = pygame.image.load("./gui/Boutons/attaque spéciale.png")
attaque_spéciale = pygame.transform.scale(attaque_spéciale, (150, 150))

bouton_esquive = pygame.image.load("./gui/Boutons/esquive.png")
bouton_esquive = pygame.transform.scale(bouton_esquive, (150, 150))

gagné_vie = pygame.image.load("./gui/Boutons/re-gagner de la vie.png")
gagné_vie = pygame.transform.scale(gagné_vie, (150, 150))
	
guerrier = pygame.image.load("./gui/Boutons/guerrier.png")
guerrier = pygame.transform.scale(guerrier, (150, 150))
	
mage = pygame.image.load("./gui/Boutons/Mage.png")
mage = pygame.transform.scale(mage, (150, 150))
	
archer = pygame.image.load("./gui/Boutons/archer.png")
archer = pygame.transform.scale(archer, (150, 150))
	
barre = pygame.image.load("./gui/barre.png")
	
monster_image = pygame.image.load("./gui/monster.png")
monster_image = pygame.transform.scale(monster_image, (150, 150))
	
guerrier_image = pygame.image.load("./gui/guerrier.png")
guerrier_image = pygame.transform.scale(guerrier_image, (100, 100))
	
mage_image = pygame.image.load("./gui/mage.png")
mage_image = pygame.transform.scale(mage_image, (100, 100))
	
archer_image = pygame.image.load("./gui/archer.png")
archer_image = pygame.transform.scale(archer_image, (100, 100))

coffre_fermee = pygame.image.load("./gui/coffre_fermee.png")
coffre_fermee = pygame.transform.scale(coffre_fermee, (400, 400))

coffre_ouvert = pygame.image.load("./gui/coffre_ouvert.png")
coffre_ouvert = pygame.transform.scale(coffre_ouvert, (400, 400))

case = pygame.image.load("./gui/case.png")
case = pygame.transform.scale(case, (150, 45))

esquive1 = pygame.image.load("./gui/Boutons/esquive_utiliser.png")
esquive1 = pygame.transform.scale(esquive1, (150, 150))

gagné_vie2 = pygame.image.load("./gui/Boutons/vie_max.png")
gagné_vie2 = pygame.transform.scale(gagné_vie2, (150, 150))

attaque_speciale2 = pygame.image.load("./gui/Boutons/attaque_speciale_utiliser.png")
attaque_speciale2 = pygame.transform.scale(attaque_speciale2, (150, 150))

banniere = pygame.image.load("./gui/banniere.png")

play = pygame.image.load("./gui/play.png")



# Collages
fenetre.blit(fond, (0,0))						# Fond
fenetre.blit(barre, (0, 700))
fenetre.blit(monster_image, (0, 0))
fenetre.blit(guerrier, (1450, 0))				# guerrier
fenetre.blit(mage, (1300, 0))					# mage
fenetre.blit(archer, (1150, 0))					# Archer


#________________________________________________________________________________________________________ 

texte("Quel métier choisis tu? ", (950, 40), 40, blue)
#Rafraîchissement de l'écran
pygame.display.flip()
pygame.mixer.music.load("./gui/musique.mp3")
pygame.mixer.music.queue("./gui/musique2.mp3")
pygame.mixer.music.play()



#________________________________________________________________________________________________________ 


#________________________________________________________________________________________________________

#BOUCLE INFINIE
continuer = 1
while continuer:
	
	for event in pygame.event.get():	#Attente des événements
		#commencement()
		#if is_playing == True:
			#apres_play()
			if event.type == MOUSEBUTTONDOWN:
				x,y = event.pos
				print(event)

				if hero == False:
					Choix_hero(event.pos, guerrier, mage, archer)

				health_bar(fenetre)	
				Choix_boutons()
				fin_de_vie()
				health_bar(fenetre)

			if event.type == KEYDOWN:

				if event.key == K_s:
					if personnage.argent >= 150:
						texte("Vous avez acheter 2 boules spéciales", (700, 100), 30, green)
						attack_speciale += 2
						personnage.argent -= 150
						time.sleep(3.0)
						efface_texte()
						
				if event.key == K_a:
					if personnage.argent >= 100:
						texte("Vous avez acheter une épée", (700, 100), 30, green)
						personnage.attaque += 10
						personnage.argent -= 100
						time.sleep(3.0)
						efface_texte()

				if event.key == K_e:
					if personnage.argent >= 100:
						texte("Vous avez acheter des ailes", (700, 100), 30, green)
						personnage.esquive += 10
						personnage.argent -= 100
						time.sleep(3.0)
						efface_texte()

				if event.key == K_r:
					if personnage.argent >= 100:
						texte("Vous avez acheter une baguette", (700, 100), 30, green)
						personnage.regeneration += 10
						personnage.argent -= 100
						time.sleep(3.0)
						efface_texte()

				if event.key == K_ASTERISK :
					if personnage.argent >= 150:
						texte("Vous avez acheter une pomme d'or", (700, 100), 30, green)
						personnage.maxVie += 10
						personnage.vie = personnage.maxVie
						personnage.argent -= 100
						time.sleep(3.0)
						efface_texte()

				if deuxieme_monstre == 1:
					if event.key == K_SPACE:
						attack = randint(0, personnage.attaque)
						coup_critique = randint(0, 1)
						son.play()
						if coup_critique == 1:
							attack += 20
							sleep += 4.0
							texte("Vous avez donner un coup critique", (700, 50), 30, yellow)
						texte(f'Vous avez attaquer de {attack}', (700, 100), 30, blue)
						monstre2.vie -= attack
						time.sleep(3.0)
						efface_texte()
						if monstre2.vie > 0:
							time.sleep(3.0)
							efface_texte()
							attaque_monstre2()
						else:
							fin_de_vie()
							if monstre.vie > 0:
								Attaque_monstre()
							else:
								fin_de_vie()

			if event.type == QUIT:
				continuer = 0
	#Rafraichissement
	pygame.display.flip()

