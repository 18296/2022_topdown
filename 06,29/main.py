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
        self.left, self.right, self.up, self.down = False, False, False, False

    def move(self, m):  # movement = [x,y]
        self.movement = [0, 0]
        if self.right:
            self.movement[0] += 5
        if self.left:
            self.movement[0] -= 5
        if self.up:
            self.movement[1] -= 5
        if self.down:
            self.movement[1] += 5

        self.rect.x += self.movement[0]
        self.rect.x += self.movement[1]


player1 = Player()

game_loop = True
while game_loop:
    fps = 60
    time.Clock().tick(fps)

    # Human Interaction
    for event in pygame.event.get():
        if event.type == QUIT:
            game_loop = False

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                player1.right = True
            if event.key == K_LEFT:
                player1.left = True
            if event.key == K_DOWN:
                player1.down = True
            if event.key == K_UP:
                player1.up = True

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                player1.right = False
            if event.key == K_LEFT:
                player1.left = False
            if event.key == K_DOWN:
                player1.down = False
            if event.key == K_UP:
                player1.up = False

    screen.fill(turquoise)
