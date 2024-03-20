import pygame
from enum import Enum

class Kierunek(Enum):
    GORA = 0
    PRAWO = 1
    DOL = 2
    LEWO = 3

class Segment:
    def __init__(self, pozycja):
        self.obraz = pygame.image.load('images/segment.png')
        self.rect = self.obraz.get_rect()
        self.rect.center = pozycja
        self.poprzednia_pozycja = self.rect.center

    def move(self, nowa_pozycja):
        self.poprzednia_pozycja = self.rect.center
        self.rect.center = nowa_pozycja