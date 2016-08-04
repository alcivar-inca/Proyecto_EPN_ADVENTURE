#   PRIMERA VERSION EPN AVENTURE

#   importamos la libreria Pygame
import pygame

#	DECLARACION DE CONSTANTES DE LOS COLORES DE PANTALLA A UTILIZAR
BLANCO = (255, 255, 255)
NEGRO = (0, 0 ,0)


pygame.init() #	Inicializa el pygame

tamanio=[800, 600] #	Tamaño de la ventana

pantalla = pygame.display.set_mode(tamanio)	#	Creacion de la ventana
pygame.display.set_caption("Mi primera animacion")	#	Nombre de la ventana

echo = True	# Variable para ingrear al bucle WHILE
reloj = pygame.time.Clock()	#	Variaable para asignar el tiempo de actualizacion de la pantalla

sonido_click = pygame.mixer.music.load("accion.mp3") #sonido de fondo de juego primer nivel 
sonido_click = pygame.mixer.music.play(1)

while echo:
	#	Bucle principal de los eventos realizados con teclado
    for evento in pygame.event.get():
    	#	INICIA GRUPO DE CONDICIONES PARA LOS DIFERENTES EVENTOS
        if evento.type == pygame.QUIT: #	Si reciona cerrar la ventana cierra el bucle while y sale
        	echo=False
       	#	CIERRA TODAS LAS CONDICIONES PARA LOS EVENTOS

    #	INICIA BLOQUE DE LA LOGICA DEL JUEGO
    #	FINALIZA BLOQUE DE LA LOGICA DEL JUEGO

    
    #	Inicia bloque que dibuja el juego
    pantalla.fill(NEGRO)
    #	Cierra el bloque de dibuja el juego	

	
	pygame.display.flip()
    reloj.tick(60)
pygame.quit()
