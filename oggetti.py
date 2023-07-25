import pygame, sys 
from pygame.locals import *

class Tavolo:
    def __init__(self, n, m, screen):
        self.vuoto = ''
        self.giallo = 'o'
        self.rosso = 'x'

        self.n = n
        self.m = m

        self.screen = screen

        self.bloccato = False

        self.mtx = [[self.vuoto for _ in range(self.m)] for _ in range(self.n)]

        self.draw()

        def draw(self):
            size = (self.screen.get_width()/self.n, self.screen.get_height()/self.m)

            rosso_image = pygame.image.load('Rosso.png')
            giallo_image = pygame.image.load('Giallo.png')

            for i in range(self.n):
                for j in range(self.m):
                    rect = pygame.Rect(size[0] * i, size[1] * j, size[0], size[1])

                    if (i+j) % 2 == 0:
                        self.screen.fill((25, 25, 25), rect)

                    if self.mtx[i][j] != self.vuoto:
                        img = rosso_image if self.mtx[i][j] == self.rosso else giallo_image
                        img = pygame.transform.scale(img, rect.size)

                        self.screen.blit(img, rect)

        def piazza(self, colonna, turno):
            if self.bloccato:
                return
            
            riga = self.n-2
            for cella in self.mtx[colonna]:
                if cella != self.vuoto:
                    riga -= 1

            if riga >= 0:
                self.mtx[colonna][riga] = turno
                self.draw()

        def controlloVittoria(self, turno):
            #controllo orizzontale
            for y in range(self.m):
                for x in range(self.n - 3):
                    if self.mtx[x][y] == turno and self.mtx[x+1][y] == turno and self.mtx[x+2][y] == turno and self.mtx[x+3][y] == turno:
                        return True
        
            #controllo verticale
            for x in range(self.n):
                for y in range(self.m - 3):
                    if self.mtx[x][y] == turno and self.mtx[x][y+1] == turno and self.mtx[x][y+2] == turno and self.mtx[x][y+3] == turno:
                        return True
        
            #controllo diagonale: /
            for x in range(self.n - 3):
                for y in range(3, self.m):
                    if self.mtx[x][y] == turno and self.mtx[x+1][y-1] == turno and self.mtx[x+2][y-2] == turno and self.mtx[x+3][y-3] == turno:
                        return True
        
            #controllo diagonale: \
            for x in range(self.n - 3):
                for y in range(self.m - 3):
                    if self.mtx[x][y] == turno and self.mtx[x+1][y+1] == turno and self.mtx[x+2][y+2] == turno and self.mtx[x+3][y+3] == turno:
                        return True

            return False