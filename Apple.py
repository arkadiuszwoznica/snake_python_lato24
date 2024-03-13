import pygame
from random import randint

class Apple:
    def __init__(self):
        self.obrazek = pygame.image.load("images/apple.png")
        self.rect = pygame.Rect( randint(0, 24) * 32, randint(0, 18) * 32, 32, 32 )