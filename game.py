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
            elif event.type == KEYUP || event.type == KEYDOWN:
                if filter(lambda p: event.key == p.left || event.key == p.right, paddles):
                    p[0].move(event.type, event.key) #pseudocode
