import pygame.display
from pygame import *
init()
# window
screen = pygame.display.set_mode((800, 600))

# colours
white = (255, 255, 255)
red = (255, 0, 0)
turquoise = (949, 129, 138)

# Classes

# Player
class Player():
    def __init__(self):
        self.rect = Rect(0, 0, 40, 60)
        self.colour = white

    def move(self):
        pass


game_loop = True
while game_loop:
    fps = 60
    time.Clock().tick(fps)
    screen.fill(turquoise)
