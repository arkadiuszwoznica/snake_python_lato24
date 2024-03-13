import pygame
from pomocnicze import Kierunek

class Snake:
    def __init__(self):
        self.obrazek_glowy = pygame.image.load('images/head.png')
        self.glowa = pygame.transform.rotate(self.obrazek_glowy, 0)
        self.pozycja = self.glowa.get_rect( center = (12*32+16, 9*32+16) )
        self.kierunek = Kierunek.GORA

    def ustaw_kierunek(self, kierunek):
        self.kierunek = kierunek
        self.glowa = pygame.transform.rotate(self.obrazek_glowy, kierunek.value * -90)
    
    def move(self):
        if self.kierunek == Kierunek.GORA:
            self.pozycja.move_ip( 0, -32 ) #góra
        elif self.kierunek == Kierunek.DOL:
            self.pozycja.move_ip( 0, 32 ) #dół
        elif self.kierunek == Kierunek.PRAWO:
            self.pozycja.move_ip( 32, 0 ) #prawo        
        elif self.kierunek == Kierunek.LEWO:
            self.pozycja.move_ip( -32, 0 ) #lewo