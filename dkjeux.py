"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.
"""
# pip install pygame
import pygame
from pygame.locals import *
from classDk import Player
from ClassNiveau import Niveau
from classEnemy import Enemy
from constantes import *

# initialise pygame
pygame.init()

#creee une fenetre 
screen = pygame.display.set_mode((cote_fenetre, cote_fenetre))
#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(titre_fenetre)


#BOUCLE PRINCIPALE
continuer=1
while continuer:
    #Chargement et affichage de l'écran d'accueil
    accueil = pygame.image.load(image_accueil).convert()
    screen.blit(accueil, (0,0))

    #Rafraichissement
    pygame.display.flip()

    #On remet ces variables à 1 à chaque tour de boucle
    continuer_jeu = 1
    continuer_accueil = 1

    #BOUCLE D'ACCUEIL
    while continuer_accueil:

        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        #On parcours la liste de tous les événements reçus
        for event in pygame.event.get():

            #Si l'utilisateur quitte, on met les variables 
			#de boucle à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0
                #Variable de choix du niveau
                choix = 0
            elif event.type == KEYDOWN:
                #Lancement du niveau 1
                if event.key == K_F1:
                    continuer_accueil = 0 #On quitte l'accueil
                    choix = "n1"          #On définit le niveau à charger
                #Lancement du niveau 2
                elif event.key == K_F2:
                    continuer_accueil = 0
                    choix = "n2"

    #on verifie que le joueur a choisi un niveau
    #pour ne pas charger s'il quitte
    if choix != 0:
        #Chargement du fond
        fond = pygame.image.load(image_fond).convert()

        #Chargement du niveau
        niveau = Niveau(choix)
        niveau.generer()
        niveau.afficher(screen)

        #Création de Donkey Kong
        dk = Player("images/dkdroite.png", "images/dkgauche.png",
        "images/dkhaut.png", "images/dkbas.png", niveau)

    #BOUCLE DE JEU
    while continuer_jeu:
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        #On parcours la liste de tous les événements reçus
        for event in pygame.event.get():

            #Si l'utilisateur quitte, on met les variables qui continue le jeu
            #et la boucle d'accueil à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT:
                continuer_jeu = 0
                continuer = 0
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continuer_jeu = 0 #On revient au menu si echap est pressé

                #Touches de déplacement de Donkey Kong
                elif event.key == K_RIGHT:
                    dk.deplacer('droite')
                elif event.key == K_LEFT:
                    dk.deplacer('gauche')
                elif event.key == K_UP:
                    dk.deplacer('haut')
                elif event.key == K_DOWN:
                    dk.deplacer('bas')

        #Affichages aux nouvelles positions
        screen.blit(fond, (0,0))
        niveau.afficher(screen)
        screen.blit(dk.direction, (dk.x, dk.y)) #dk.direction contient l'image dans la bonne direction

        
        pygame.display.flip()

        #Victoire -> Retour à l'accueil
        if niveau.structure[dk.case_y][dk.case_x] == 'a':
            continuer_jeu = 0
            vic = pygame.image.load(image_victoire).convert()
            screen.blit(vic, (0,0))