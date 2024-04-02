import pygame
from pomocnicze import Kierunek, Segment

class Snake:
    def __init__(self):
        self.obrazek_glowy = pygame.image.load('images/head.png')
        self.glowa = pygame.transform.rotate(self.obrazek_glowy, 0)
        self.pozycja = self.glowa.get_rect( center = (12*32+16, 9*32+16) )
        self.kierunek = Kierunek.GORA
        self.segments = []
        self.poprzednia_pozycja = self.pozycja.center

    def ustaw_kierunek(self, kierunek):
        self.kierunek = kierunek
        self.glowa = pygame.transform.rotate(self.obrazek_glowy, kierunek.value * -90)
    
    def move(self):
        self.poprzednia_pozycja = self.pozycja.center

        if self.kierunek == Kierunek.GORA:
            self.pozycja.move_ip( 0, -32 ) #góra
        elif self.kierunek == Kierunek.DOL:
            self.pozycja.move_ip( 0, 32 ) #dół
        elif self.kierunek == Kierunek.PRAWO:
            self.pozycja.move_ip( 32, 0 ) #prawo        
        elif self.kierunek == Kierunek.LEWO:
            self.pozycja.move_ip( -32, 0 ) #lewo

        #wychodzenie poza krawędzie
        if self.pozycja.left < 0:
            self.pozycja.left = 768
        if self.pozycja.left > 768:
            self.pozycja.left = 0
        if self.pozycja.top < 0:
            self.pozycja.top = 576
        if self.pozycja.top > 576:
            self.pozycja.top = 0
    
        for i in range( len(self.segments)):
            if i==0:
                self.segments[i].move(self.poprzednia_pozycja)
            else:
                self.segments[i].move( self.segments[i-1].poprzednia_pozycja )


    def new_segment(self):
        self.segments.append(Segment(self.poprzednia_pozycja))
    
    def sprawdz_kolizje(self):
        # Sprawdzenie kolizji głowy z segmentami węża
        for segment in self.segments:
            if self.pozycja.colliderect(segment.rect):
                return True

        # Sprawdzenie wychodzenia poza ekran
        if self.pozycja.left < 0 or self.pozycja.right > 800 or \
        self.pozycja.top < 0 or self.pozycja.bottom > 600:
            return True

        return False



        
        