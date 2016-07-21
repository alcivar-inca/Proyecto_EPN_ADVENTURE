import sys, pygame
from pygame.locals import *
from tkinter import *

WIDTH = 900
HEIGHT = 600
class Cursor(pygame.Rect):
    def_init_(self):
        pygame.Rect._init_(self, 0,0,1,1)
    def update (self):
        self.left,self.top=pygame.mouse.get_pos()
class Boton (pygame.sprite.Sprite):
    def_init_(self, image,x=200, y=200):
        self.imagenorm=imag1
        self.imagenselec=imag2
        self.imagenact=self.imagenorm
        self.rect=self.imagenact.get_rect()
        self.rect.left,self.rect.top=(x,y)

    def update (self, pantalla, cursor):
        if cursor.colliderect(self.rect):
            self.imagenact=self.imagenorm
        else: self.imagenact=self.imagenorm
            pantalla.blit(self.imagenact, self.rect)



def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("INTRODUCCION EPN ADVENTURE")
    fondo = pygame.image.load("fondo.jpg").convert()
    screen.blit(fondo, (0, 0))
    # se muestran lo cambios en pantalla
    pygame.display.flip()
    img1=pygame.image.load("iniciar.png")
    img2=pygame.image.load("iniciar.png")
    boton1=Boton(img1, img2)
    cursor1= Cursor()
    salir=false
    while salir!=True:
        pygame.display.flip()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)

    cursor1.update()
    boton1.update(pantalla,cursor1)
    return 0

if __name__ == '__main__':
    pygame.init()
main()

