"""Classe Niveau du jeu de Labyrinthe Donkey Kong"""

import pygame
from pygame.locals import * 
from constantes import *

class Niveau:
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0

    def generer(self):
        #Ouverture du fichier
        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            #On parcourt les lignes du fichier
            for ligne in fichier:
                ligne_niveau = []
                #On parcourt les sprites (lettres) contenus dans le fichier
                for sprite in ligne:
                    #On ignore les "\n" de fin de ligne
                    if sprite != '\n':
                        #On ajoute le sprite à la liste de la ligne
                        ligne_niveau.append(sprite)
                #On ajoute la ligne à la liste du niveau
                structure_niveau.append(ligne_niveau)
            #On sauvegarde cette structure
            self.structure = structure_niveau

    def afficher(self, screen):
        #Chargement des images (seules celles correspondant à des murs sont chargées)
        mur = pygame.image.load(image_mur).convert()
        depart= pygame.image.load(image_depart).convert()
        arrivee = pygame.image.load(image_arrivee).convert()
        enemy = pygame.image.load(image_enemy).convert()

        #On parcourt la liste du niveau
        num_ligne = 0
        for ligne in self.structure:
            #On parcourt les listes de lignes
            num_case = 0
            for sprite in ligne:
                #On calcule la position réelle en pixels
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprite == 'm':		   #m = Mur
                    screen.blit(mur, (x,y))
                elif sprite == 'd':		   #d = Départ
                    screen.blit(depart, (x,y))
                elif sprite == 'e':		   #e = enemy
                    screen.blit(enemy, (x,y))
                elif sprite == 'a':		   #a = Arrivée
                    screen.blit(arrivee, (x,y))
                num_case += 1
            num_ligne += 1

