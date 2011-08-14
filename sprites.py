from pygame.sprite import Sprite
import pygame

from locals import *

class Paddle(Sprite):
    def __init__(self, args):
        Sprite.__init__(self)
        #create a white rect for a player                                      
        self.surface = pygame.Surface(10,50)
        self.suface.fill(args['colour'])
        self.position = surface.get_rect()
        self.name = args['name']
        self.side = args['side']
        self.left = args['controls']['left']
        self.right = args['controls']['right']
        self.screen = pygame.display.get_surface()

        if side == SIDE_A:
            #center on top
        elif side == SIDE_B:
            #center on bottom
