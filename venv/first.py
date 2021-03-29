import pygame, sys
import random
import time

from pygame.locals import (
K_UP,
K_DOWN,
K_LEFT,
K_RIGHT,
KEYDOWN,
K_ESCAPE,
QUIT
)

pygame.init()

ventana=pygame.display.set_mode((800,500))
pygame.display.set_caption("Titulo Aquí")
ventana.fill((0,0,0))

holeX=50
holeY=50


bandera=True
while bandera:
    pygame.display.update()

    pygame.draw.circle(ventana,(100,0,100),(holeX,holeY),30)

    pygame.draw.rect(ventana,(250,250,250),(100,0,10,800))

#estos son los sucesos que ocurren dentro del juego
    for event in pygame.event.get():

        #cierra la ventana
        if event.type == pygame.QUIT:
            bandera = False

        #que boton hay presionad, si lo hay
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                holeX=holeX+10





pygame.quit()