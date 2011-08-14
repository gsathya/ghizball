from pygame.locals import *

gamefont = "Cantarell"
gamemode = [1024,600] # or None to use best full screen resolution

players = [
    {
        'name': "Genghiz",
        'controls': {
            #'up': K_w,
            #'down': K_s,
            'left': K_a,
            'right': K_d
            },
        'colour': (255, 255, 255)
        },
    {
        'name': "Zoreph",
        'controls': {
            #'up': K_UP,
            #'down': K_DOWN,
            'left': K_LEFT,
            'right': K_RIGHT
            },
        'colour': (255, 255, 255)
        }
    ]
