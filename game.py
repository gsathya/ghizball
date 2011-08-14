import pygame
from pygame.locals import *

import settings
from settings import player1, player2

def init():
    pygame.init()

    gamemode = settings.gamemode or pygame.display.list_modes()[0]

    screen = pygame.display.set_mode(gamemode, FULLSCREEN)
    pygame.display.set_caption('Ghizball')

def gameloop():
    screen = pygame.display.set_mode()
    while 1:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYUP:
                if event.key == player1['controls']['left']:
                    #stop moving left
                    pass
                elif event.key == player1['controls']['right']:
                    #stop moving right
                    pass
                elif event.key == player2['controls']['left']:
                    #stop moving left
                    pass
                elif event.key == player2['controls']['right']:
                    #stop moving right
                    pass
            elif event.type == KEYDOWN:
                if event.key == player1['controls']['left']:
                    #start moving left
                    pass
                elif event.key == player1['controls']['right']:
                    #start moving right
                    pass
                elif event.key == player2['controls']['left']:
                    #start moving left
                    pass
                elif event.key == player2['controls']['right']:
                    #start moving right
                    pass
