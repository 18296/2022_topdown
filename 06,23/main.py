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


# Map
map1 = """tttttttttttttttttttt
t                  t
t                  t
t                  t
t        tt        t
t                  t
t      tttttt      t
t                  t
t                  t
t                  t
t         h        t
t     tttttttt     t
t                  t
t     tt    tt     t
tttttttttttttttttttt
"""

map1 = map1.splitlines()
tile = []


def tiles(map1):
    for y, line in enumerate(map1):
        for x, c in enumerate(line):
            if c == "t":
                tile.append(Rect(x * 40, y * 40, 40, 40))


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
