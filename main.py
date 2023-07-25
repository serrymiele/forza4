import pygame, sys, os 
from pygame.locals import *
from oggetti import *

os.system("cls")

#finestra base
WINDOW_SIZE = (700, 600)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption('Finestra Base')

#clock del programma
clock = pygame.time.Clock()
fps = 60

n = 7
m = 6

tavolo = Tavolo(n, m, screen)
turno = tavolo.giallo

pygame.font.init()
font = pygame.font.SysFont(pygame.font.get_default_font(), int(60), bold = True, italic = True)

#ciclo fondamentale
while True:
    #inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if tavolo.bloccato:
                screen.fill((0, 0, 0))
                tavolo = Tavolo(n, m, screen)
            else:
                mouse_pos = pygame.mouse.get_pos()
                pos = [0, 0]
                pos[0] = (mouse_pos[0]) * n // screen.get_width()
                pos[1] = (mouse_pos[1]) * m //screen.get_height()
                tavolo.piazza(pos[0], turno)
                if tavolo.controlloVittoria(turno):
                    tavolo.bloccato = True
                    
                    nome_turno = "Giallo" if turno == tavolo.giallo else "Rosso"
                    colore = (0, 153, 255)

                    img_txt = font.render(f"Il {nome_turno} ha vinto!!", True, colore)
                    img_txt_rect = pygame.Rect(screen.get_width()/2-img_txt.get_width()/2, screen.get_height()/2-img_txt.get_height()/2, img_txt.get_width(), img_txt.get_height())

                    screen.blit(img_txt, img_txt_rect)

                turno = tavolo.rosso if turno == tavolo.giallo else tavolo.giallo

    pygame.display.update()

    clock.tick(fps)