#1-imports
import pygame
from pygame.locals import *
import sys #Con esto permite cerrar el programa
import random

#2-Constants
COLOR = (200, 200, 200)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 120
TARGET_WIDTH_HEIGT = 120
N_PIXELES_TO_MOVE = 3

#3-Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4-Load Assets
ballImage = pygame.image.load("POO/Pygames/images/sprite001.png")
targetImage = pygame.image.load("POO/Pygames/images/target.png")

#5-Initialize variables
ballx = random.randrange(MAX_WIDTH)
bally = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballx, bally, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)#pygames.Rect define un rectangulo y pide 4 parametros (Posicion x, y, Ancho y Alto)
targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGT, TARGET_WIDTH_HEIGT)

#6-Loop
while True:
    #7-Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballx = ballx - N_PIXELES_TO_MOVE
            elif event.key == pygame.K_RIGHT:
                ballx = ballx + N_PIXELES_TO_MOVE
            elif event.key == pygame.K_UP:
                bally = bally - N_PIXELES_TO_MOVE
            elif event.key == pygame.K_DOWN:
                bally = bally + N_PIXELES_TO_MOVE

    
    #8-Do any "per frame" actions
    ballRect = pygame.Rect(ballx, bally, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
    if ballRect.colliderect(targetRect):
        print("La bola llego al objetivo")

    #9-Clear the window
    window.fill(COLOR)

    #10-Draw all window elements
    #Toman posicion cardinal empenzando de la parte superior izquierda (x: Izq -> Der; y: Arriba -> Abajo)
    window.blit(ballImage, (ballx, bally)) #blit dibuja/muestra la imagen

    #11-Update the window
    pygame.display.update()

    #12-Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)