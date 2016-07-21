#   PRIMERA VERSION EPN AVENTURE

import pygame
import time
pygame.init() 

tamanio=[1280, 720] #	Tamanioo de la pantalla a ejecutarse
pantalla = pygame.display.set_mode(tamanio)	#	Creacion de la ventana
pygame.display.set_caption("EPN AVENTURE") #	Titulo de la ventana del juego
nivel_1 = pygame.image.load("pista_1.jpg") #	 asignamos la imagen a una constante

sentido = pygame.image.load("Der_1.png")
bala=pygame.image.load("bala1.png")
dir=1

X=0
Y=405

echo = True
reloj = pygame.time.Clock()	#	Variaable para asignar el tiempo de actualizacion de la pantalla

while echo:
	pantalla.blit(nivel_1, [0,0])
	pantalla.blit(sentido, [X,Y])

	#	Bucle principal de los eventos realizados con teclado
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT: #	Si reciona cerrar la ventana cierra el bucle while y sale
			echo=False
		
		if evento.type==pygame.KEYDOWN:
			if evento.key==pygame.K_RIGHT: # TECLA DERECHA
				X +=5
				sentido=pygame.image.load("Der_1.png")
				dir=1
			if evento.key==pygame.K_LEFT: # TECLA IZQUIERDA
				X -=5
				sentido=pygame.image.load("Izq_1.png")
				dir=2
			if evento.key==pygame.K_UP: #	TECLA HACIA ARRIBA
				Y -=20
			if evento.key==pygame.K_DOWN:
				Y +=20
			if evento.key== pygame.K_SPACE:
				if dir ==1:
					for i in range (X, 1280, 15):
						pantalla.blit(bala, [90+i, Y+22])
				else:
					for i in range (X, 0, -15):
						pantalla.blit(bala, [i, Y+22])

	pygame.display.flip()
	reloj.tick(20)
pygame.quit()
