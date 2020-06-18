import pygame
from pygame.locals import *
pygame.init()
 
win = pygame.display.set_mode((400,500))
run = True
 
nb_cases_cote = 10
taille_case = min(win.get_size()) / nb_cases_cote # min renvoie la valeur minimale d'une liste, ici la dimension de la fenêtre
 
 
font = pygame.font.SysFont("",20)
 
while run:
    win.fill((0,0,0))
 
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            run = False
 
    for x in range(nb_cases_cote):
        for y in range(nb_cases_cote): # on parcoure les 2 dimensions
 
            pygame.draw.rect(win, [255]*3, [x*taille_case, y*taille_case, taille_case, taille_case], 1) # dessin du rect avec la méthode que je t'avais marqué
 
            lettre = font.render("ciao", True, [255]*3) # on crée la lettre
            lettre_rect = lettre.get_rect() # je recupere le rect
            lettre_rect.center = [x*taille_case + 1/2*taille_case, y*taille_case + 1/2*taille_case] # je place le centre du rect au milieu de la case
            win.blit( lettre , lettre_rect ) # on blit le tout
 
    pygame.display.flip()