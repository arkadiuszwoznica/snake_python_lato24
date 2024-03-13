import pygame
import random
import time
from Snake import Snake

#ustawienia
width = 800
height = 608

#inicjacja
pygame.init()
screen = pygame.display.set_mode( (width,height) )
clock = pygame.time.Clock()

#obrazki
tlo = pygame.Surface((width, height))
kafelek = pygame.image.load('images/background.png')
for x in range(25):
    for y in range(19):
        pozycja = (x * 32, y * 32)
        kolor = ( random.randrange(0, 20), random.randrange(0, 20), random.randrange(0, 20) )
        c_kafelek = kafelek.copy()
        c_kafelek.fill(kolor, special_flags=pygame.BLEND_ADD)
        tlo.blit(c_kafelek, pozycja)
        screen.blit(tlo, (0,0))
        pygame.display.flip()
        clock.tick(202)

#obiekty
snake = Snake()

#główna pętla
runnig = True
while runnig:
    #zdarzenia
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                runnig = False

        elif event.type == pygame.QUIT:
            runnig = False
    
    #rysowanie
    screen.blit(tlo, (0,0))
    # decyzja do podjęcia: 1 albo 2
    #snake.blit(screen)
    #screen.blit(snake.obraz, snake.pozycja)
    pygame.display.flip()