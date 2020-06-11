from random import *
from pygame import *
après = 0
Argent = 0
#mage
esc_mage = 5
vie_mage = 20
att_mage = 10
#archer
esc_Arché = 20
vie_archer = 10
att_archer = 5
#guerrier
esc_guerrier = 10
att_guerrier = 20
vie_guerrier = 5
#joueur
joueur = 30
print("\033[34m1: guerrier\033[0m")
print("\033[32m2: Archer\033[0m")
print("\033[35m3: Mage\033[0m")
métier = input("\033[33mQuel métier choisi tu\033[0m")
rénitialiser_boss = 50
boss = 50
regagne_vie = 9
rénitialiser_AttackToi = 9 
Attack_Toi = 10
Attack_Boss = 15
Étages = 1


print (f'vous êtes dans l étage {Étages} et vous êtes contre un monstre')
while boss > 0 and joueur > 0 :
    print(f"\033[31mTu as {joueur} vies et le boss en a {boss}.\033[0m")
    action = input ('tapez 1 si vous voulez attaquez, si vous voulez regagnez de la vie tapez 2 et si vous voulez esquivez tapez 3.')
    #Ton attaque
    if action == "1" :
        attack = randint(0, Attack_Toi)
        coup_critique = randint(0, 1)
        if coup_critique == 1 :
            attack = attack + 20
            print ("\033[33mVous avez donner un coup critique\033[0m")
        print (f'Vous avez attaqué de {attack}')
        boss = boss - attack
        print (f'Le boss lui reste {boss} vies')
    if action == "2" :
        vies = randint(0, Attack_Toi)
        print (f'Vous avez regagné {vies} de vies')
        joueur = joueur + vies
    if action == "3" :
        esquive = randint(0, 1)
        if esquive == 0 :
            print ("\033[33mvous avez esquivé le coup\033[0m")
            après = 1


    #attaque du boss
    action_boss = randint(0, 1)
    if action_boss == 0 :
        attack_b = randint(0, Attack_Boss)
        print (f'Le boss vous a attaqué de {attack_b}')
        joueur = joueur - attack_b
        if après == 1 :
            joueur = joueur + attack_b
        print (f'Ils vous reste {joueur} vies')
    if action_boss == 1 :
        vies_b = randint(0, regagne_vie)
        print (f'Le boss à regagné {vies_b} de vies')
        boss = boss + vies_b
        print (f'Le boss lui reste {boss} vies')
    
    if boss <= 0 :
        boss = rénitialiser_boss + 10
        rénitialiser_boss = rénitialiser_boss + 10
        Attack_Boss = Attack_Boss + 5
        Attack_Toi = rénitialiser_AttackToi + 10
        joueur = rénitialiser_AttackToi + 21
        Étages = Étages + 1
        print (f"\033[32mTu as gagné:] maintenant tu est à l'étage n°{Étages}\033[0m")
        Argent = Argent + randint(0, 30)
        choix = input (f"\033[32mTu as {Argent}€ tape 1 si tu veux continuer l'aventure, ou si tu veux regarder la boutique tape 2\033[0m")
        if choix == "2" :
            print ('   ___             _   _                  ')
            print ('  / __\ ___  _   _| |_(_) __ _ _   _  ___ ')
            print (' /__\/// _ \| | | | __| |/ _  | | | |/ _ \ ')
            print ('/ \/  \ (_) | |_| | |_| | (_| | |_| |  __/')
            print ('\_____/\___/ \__,_|\__|_|\__, |\__,_|\___|')
            print ('                            |_|           ')
            boutique = input('vous êtes dans la boutique vous pouvez vous acheter des trucs en tapant 1 sinon tapez 2.')
            if boutique == "1" :
                print ('nb à taper | objets         | Qualités | Pour   | Coûte')
                print ('   1 :     | épée           | +10 att  |guerrier| 100€')
                print ('   2 :     | baguette       | +10 vies | TLM    | 50€')
                print ('   3 :     | ailes          | +10 esc  | TLM    | 50€')
                print ('   4 :     | arc            | +10 att  | archer | 100€')
                print ('   5 :     | potion         | +10 att  | Mage   | 100€')
                print ('   6 :     | boules spéciale| +2 spé   | TLM    | 200€')
                achetée = input ("Qu'est ce vous voulez acheter?")
                achetée2 = input ("Une autre chose ?")


    if joueur <= 0 :
        joueur = rénitialiser_AttackToi + 21
        boss = rénitialiser_boss
        Étages = Étages - 1
        if Étages == 0 :
            Étages = 1
        print(f"\033[36mTu as perdu vous descendez d'un étage dommage :[ maintenant tu est à l'étage n°{Étages}\033[0m")


