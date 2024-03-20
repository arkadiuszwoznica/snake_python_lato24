import pygame
import random
import time
from Snake import Snake
from pomocnicze import Kierunek
from Apple import Apple

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
        clock.tick(700)

#obiekty
snake = Snake()
apples = []
apple = Apple()
apples.append(apple)

#zdarzenia
game_tick = pygame.USEREVENT + 0
pygame.time.set_timer(game_tick, 200)

#główna pętla
runnig = True
while runnig:
    #zdarzenia
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                runnig = False

            #sterowanie
            if event.key == pygame.K_d:
                snake.ustaw_kierunek(Kierunek.PRAWO)
            if event.key == pygame.K_a:
                snake.ustaw_kierunek(Kierunek.LEWO)
            if event.key == pygame.K_w:
                snake.ustaw_kierunek(Kierunek.GORA)
            if event.key == pygame.K_s:
                snake.ustaw_kierunek(Kierunek.DOL)

        if event.type == game_tick:
            snake.move()

        elif event.type == pygame.QUIT:
            runnig = False
    
    #rysowanie
    screen.blit(tlo, (0,0))

    screen.blit(snake.glowa, snake.pozycja)
    for a in apples:
        screen.blit(a.obrazek, a.rect)

    for s in snake.segments:
        screen.blit(s.obraz, s.rect)

    pygame.display.flip()

    #kolizje
    eat_apple = snake.pozycja == apple.rect
    if eat_apple:
        print("eat apple")
        apples.remove(apple)
        apple = Apple()
        apples.append(apple)
        snake.new_segment()

    
    przegrana = False
