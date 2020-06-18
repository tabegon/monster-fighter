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
vies = 10
print("\033[34m1: guerrier\033[0m")
print("\033[32m2: Archer\033[0m")
print("\033[35m3: Mage\033[0m")
print ("écrivez n'importe quoi ici on est encore en train de développér Merci")
métier = input("\033[33mQuel métier choisi tu\033[0m")
rénitialiser_boss = 50
boss = 50
regagne_vie = 9
rénitialiser_AttackToi = 9 
Attack_Toi = 10
Attack_Boss = 15
boss_final = 0
Attack_spéciale = 2
Étages = 1
rénitialiser_toi = 30

print (f'vous êtes dans l étage {Étages} et vous êtes contre un monstre')


def code_boutique():
    global Attack_Toi, Argent, vies, Attack_spéciale, joueur, rénitialiser_toi
    print('   ___             _   _                  ')
    print('  / __\ ___  _   _| |_(_) __ _ _   _  ___ ')
    print(' /__\/// _ \| | | | __| |/ _  | | | |/ _ \ ')
    print('/ \/  \ (_) | |_| | |_| | (_| | |_| |  __/')
    print('\_____/\___/ \__,_|\__|_|\__, |\__,_|\___|')
    print('                            |_|           ')
    boutique = input('vous êtes dans la boutique vous pouvez vous acheter des trucs en tapant 1 sinon tapez 2.')
    if boutique == "1":
        print('nb à taper | objets         | Qualités   | Pour   | Coûte')
        print('   1 :     | épée           | +10 att    |guerrier| 100€')
        print('   2 :     | baguette       | +10 vies   | TLM    | 50€')
        print('   3 :     | ailes (X stock)| +10 esc    | TLM    | 50€')
        print('   4 :     | arc            | +10 att    | archer | 100€')
        print('   5 :     | potion         | +10 att    | Mage   | 100€')
        print('   6 :     | boules spéciale| +4 spé     | TLM    | 200€')
        print("   7 :     | pomme d'or     | +10 joueur | TLM    | 150€")
        print('   n :     | pour annuler   | +0 rien    | TLM    | 0€')
        achetée = input(
            "Qu'est ce que vous voulez vous achetés (vous avez le droit qu'a 1 objet après vous pourrez en re-acheter)")
        if achetée == "1":
            Attack_Toi = Attack_Toi + 10
            Argent = Argent - 100
            print("vous avez achetée et utilisée l'épée")
        if achetée == "2":
            vies = vies + 10
            Argent = Argent - 50
            print("vous avez achetée et utilisée la baguette")
        if achetée == "3":
            print("Il n'y a plus de stock")
        if achetée == "4":
            Attack_Toi = Attack_Toi + 10
            Argent = Argent - 100
            print("vous avez achetée et utilisée l'arc")
        if achetée == "5":
            Attack_Toi = Attack_Toi + 10
            Argent = Argent - 100
            print("vous avez achetée et utilisée les potions de force")
        if achetée == "6":
            Attack_spéciale = Attack_spéciale + 4
            Argent = Argent - 200
            print("vous avez achetée et utilisée les boules spéciales")
        if achetée == "7":
            joueur = rénitialiser_toi + 10
            rénitialiser_toi = rénitialiser_toi + 10
            Argent = Argent - 150
            print("vous avez achetée et utilisée la pomme d'or")


def attaque_personage(marche):
    global attack, coup_critique, boss
    if is_action_valid():
        attack = randint(0, Attack_Toi)
        coup_critique = randint(0, 1)
        if coup_critique == 1:
            attack = attack + 20
            print("\033[33mVous avez donner un coup critique\033[0m")
            print(f'Vous avez attaqué de {attack}')
            boss = boss - attack
            if après == 2:
                boss = boss + attack
            print(f'Le boss lui reste {boss} vies')


def regeneration_vie_personage(marche):
    global vies, joueur
    if is_action_valid:
        vies = randint(vies, vies + 20)
        print(f'Vous avez regagné {vies} de vies')
        joueur = joueur + vies


def esquiver_attaque_personage(marche):
    global esquive, après
    if is_action_valid:
        esquive = randint(0, 1)
        if esquive == 0:
            print("\033[33mvous avez esquivé le coup\033[0m")
            après = 1


def attaque_speciale_personage(marche):
    global Attack_spéciale, coup_spécial, boss
    if is_action_valid:
        if Attack_spéciale == 0:
            print(
                "Vous ne pouvez pas utilisez votre attaque spéciale plus de deux fois sauf si vous vous en acheter à la boutique")
            print("Vous n'avez pas attaqué")
        if Attack_spéciale > 0:
            Attack_spéciale = Attack_spéciale - 1
            coup_spécial = randint(Attack_Toi, 200)
            print(f"vous avez attaqué de {coup_spécial}")
            boss = boss - coup_spécial
            if après == 2:
                boss = boss + coup_spécial
            print(f"le boss lui reste {boss} vies")


def is_action_valid():
    marche = randint(0, 3)
    if marche == 0:
        print("\033[35mTon action à échouée\033[0m")
        return False
    else:
        return True


while boss > 0 and joueur > 0:
    print(f"\033[31mTu as {joueur} vies et le boss en a {boss}.\033[0m")
    print ("\033[32m·\033[0m")
    action = input ('tapez 1 si vous voulez attaquez, si vous voulez regagnez de la vie tapez 2, si vous voulez esquivez tapez 3 et si vous voulez utiliser votre attaque spécial taper 4.')
    #Ton attaque
    if action == "1":
        attaque_personage()
    if action == "2":
        regeneration_vie_personage()
    if action == "3":
        esquiver_attaque_personage()
    if action == "4":
        attaque_speciale_personage()


    #attaque du boss
    action_boss = randint(0, 2)
    if action_boss == 0 :
        attack_b = randint(0, Attack_Boss)
        print (f'Le boss vous a attaqué de {attack_b}')
        joueur = joueur - attack_b
        if après == 1 :
            après = 0
            joueur = joueur + attack_b
        print (f'Ils vous reste {joueur} vies')
    if action_boss == 1 :
        vies_b = randint(0, regagne_vie)
        print (f'Le boss à regagné {vies_b} de vies')
        boss = boss + vies_b
        print (f'Le boss lui reste {boss} vies')
    if action_boss == 2 :
        print ("\033[31mLe boss à esquivée votre coup\033[0m")
        après = 2
        attack_b = randint(0, Attack_Boss)
        print (f'Le boss vous a attaqué de {attack_b}')
        joueur = joueur - attack_b
        if après == 1 :
            après = 0
            joueur = joueur + attack_b
        print (f'Ils vous reste {joueur} vies')
    
    if boss <= 0 :
        boss = rénitialiser_boss + 10
        rénitialiser_boss = rénitialiser_boss + 10
        Attack_Boss = Attack_Boss + 5
        Attack_Toi = rénitialiser_AttackToi + 10
        joueur = rénitialiser_toi + 2

        Étages = Étages + 1
        if Étages == 20 :
            print ('Vous avez fini')
            print ('Maintenant contre le boss final mais juste avant un petit moment de plisir')
            boss_final = "oui"
        print (f"\033[32mTu as gagné:] maintenant tu est à l'étage n°{Étages}\033[0m")
        print (f"\033[32mVous aviez {Argent}€ avant\033[0m")
        Argent = Argent + randint(10, 50)
        choix = input (f"\033[32mTu as {Argent}€ tape 1 si tu veux continuer l'aventure, ou si tu veux regarder la boutique tape 2\033[0m")
        if choix == "2": code_boutique()

    if joueur <= 0 :
        joueur = rénitialiser_toi
        boss = rénitialiser_boss - 20
        rénitialiser_boss = rénitialiser_boss - 20
        Attack_Boss = Attack_Boss - 4
        Étages = Étages - 1
        if Étages == 0 :
            Étages = 1
        print(f"\033[36mTu as perdu vous descendez d'un étage dommage :[ maintenant tu est à l'étage n°{Étages}\033[0m")

    if boss_final == "oui" :
        boss = 500
        Attack_Boss = 25
        while boss_final == "oui" :
            print(f"\033[31mTu as {joueur} vies et le boss en a {boss}.\033[0m")
            print ("\033[32m·\033[0m")
            action = input ('tapez 1 si vous voulez attaquez, si vous voulez regagnez de la vie tapez 2, si vous voulez esquivez tapez 3 et si vous voulez utiliser votre attaque spécial taper 4.')
            marche = randint(0, 3)
            if marche == 0 :
                print ("\033[35mton attaque à échouée\033[0m")
            #Ton attaque
            if action == "1" :
                if marche > 0 :
                    attack = randint(0, Attack_Toi)
                    coup_critique = randint(0, 1)
                    if coup_critique == 1 :
                        attack = attack + 20
                    print ("\033[33mVous avez donner un coup critique\033[0m")
                    print (f'Vous avez attaqué de {attack}')
                    boss = boss - attack
                    if après == 2 :
                        boss = boss + attack
                        print (f'Le boss lui reste {boss} vies')
            if action == "2" :
                if marche > 0 :
                    vies = randint(vies, vies+20)
                    print (f'Vous avez regagné {vies} de vies')
                    joueur = joueur + vies       
            if action == "3" :
                if marche > 0 :
                    esquive = randint(0, 1)
                    if esquive == 0 :
                        print ("\033[33mvous avez esquivé le coup\033[0m")
                        après = 1
            if action == "4" :
                if marche > 0 :
                    if Attack_spéciale == 0 :
                        print ("Vous ne pouvez pas utilisez votre attaque spéciale plus de deux fois sauf si vous vous en acheter à la boutique")
                        print ("Vous n'avez pas attaqué")
                    if Attack_spéciale > 0 :
                        Attack_spéciale = Attack_spéciale - 1
                        coup_spécial = randint(Attack_Toi, 200)
                        print (f"vous avez attaqué de {coup_spécial}")
                        boss = boss - coup_spécial
                        if après == 2 :
                            boss = boss + coup_spécial
                            print (f"le boss lui reste {boss} vies")


            #attaque du boss
            action_boss = randint(0, 2)
            if action_boss == 0 :
                attack_b = randint(0, Attack_Boss)
                print (f'Le boss vous a attaqué de {attack_b}')
                joueur = joueur - attack_b
                if après == 1 :
                    après = 0
                    joueur = joueur + attack_b
                    print (f'Ils vous reste {joueur} vies')
            if action_boss == 1 :
                vies_b = randint(0, regagne_vie)
                print (f'Le boss à regagné {vies_b} de vies')
                boss = boss + vies_b
                print (f'Le boss lui reste {boss} vies')
            if action_boss == 2 :
                print ("\033[31mLe boss à esquivée votre coup\033[0m")
                après = 2
                attack_b = randint(0, Attack_Boss)
                print (f'Le boss vous a attaqué de {attack_b}')
                joueur = joueur - attack_b
            if après == 1 :
                après = 0
                joueur = joueur + attack_b
                print (f'Ils vous reste {joueur} vies')

