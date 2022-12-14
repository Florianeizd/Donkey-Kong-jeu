"""Classe game du jeu de Labyrinthe Donkey Kong"""

import pygame
from pygame.locals import * 
from constantes import *
from classEnemy import Enemy
from classDk import Player


class Game():
	"""Classe permettant de créer un ennemi"""

	def __init__(self):
		# generer notre ennemi
		self.player = Player()
		self.all_enemy = pygame.sprite.Group()
		self.enemy = Enemy()
		self.spawnEnemy
		

	def spawnEnemy(self):
		enemy = Enemy()
		self.all_enemy.add(enemy)