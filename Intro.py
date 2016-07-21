import sys, pygame
from pygame.locals import *

WIDTH = 900
HEIGHT = 600

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("INTRODUCCION EPN ADVENTURE")
    fondo = pygame.image.load("fondo.jpg").convert()
    screen.blit(fondo, (0, 0))
    # se muestran lo cambios en pantalla
    pygame.display.flip()

    while True:
        pygame.display.flip()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
    return 0

if __name__ == '__main__':
    pygame.init()
main()
