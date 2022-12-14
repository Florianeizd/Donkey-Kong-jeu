"""Classe Enemy du jeu de Labyrinthe Donkey Kong"""
import pygame
from pygame.locals import * 
from constantes import *

class Enemy(pygame.sprite.Sprite):
	"""Classe permettant de créer un ennemi"""

	def __init__(self):
		super().__init__()
		self.attack = 100
		self.image = pygame.image.load(image_enemy).convert_alpha()
		self.rect = self.image.get_rect()
		