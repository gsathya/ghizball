import pygame
from pygame.locals import *

from itertools import cycle, izip

from settings import gamefont, gamemode, players
from sprites import Paddle
from locals import *

paddles = []

def init():
    pygame.init()

    gamemode = settings.gamemode or pygame.display.list_modes()[0]

    screen = pygame.display.set_mode(gamemode, FULLSCREEN)
    pygame.display.set_caption('Ghizball')

def gameloop():
    screen = pygame.display.get_surface()

    for side, player in izip(cycle((SIDE_A, SIDE_B)), setting.players):
        player['side'] = side
        paddles.append(Paddle(player))

    while 1:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            #should be able to rewrite and reduce the following code?
            elif event.type == KEYUP:
                if filter(lambda p: p.left == event.key, paddles):
                    p[0].move(STOP, LEFT) #pseudocode
                elif filter(lambda p: p.right == event.key, paddles):
                    p[0].move(STOP, RIGHT)
            elif event.type == KEYDOWN:
                if filter(lambda p: p.left == event.key, paddles):
                    p[0].move(START, RIGHT) #pseudocode
                elif filter(lambda p: p.right == event.key, paddles):
                    p[0].move(START, RIGHT) #pseudocode
