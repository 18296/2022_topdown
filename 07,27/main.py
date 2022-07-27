import pygame, sys
from pygame import *
from math import *

init()

# window
screendim = [800, 600]

screen = display.set_mode((screendim[0], screendim[1]))

# colours
white = (255, 255, 255)
red = (255, 0, 0)
turquoise = (49, 129, 138)
pink = (255, 105, 180)

# Map
# https://pythonprogramming.altervista.org/platform-game-in-detail-part-1/?doing_wp_cron=1655762207.1499760150909423828125
# t = solid tile, h = hole(death)
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


class Map:
    def __init__(self, m, rect_dim):  # self, map, graphical overlay, tiles in x axis, tiles in y axis
        self.tile_list = []
        self.tile_dict = {'t': [], 'h': []}
        self.m = m.splitlines()

        for y, line in enumerate(self.m):
            for x, c in enumerate(line):

                try:
                    self.tile_dict[c].append(Rect(x * rect_dim[0], y * rect_dim[1], rect_dim[0], rect_dim[1]))

                except KeyError:
                    pass

                if c == "t":
                    self.tile_list.append(Rect(x * rect_dim[0], y * rect_dim[1], rect_dim[0], rect_dim[1]))

    def draw_tiles(self):
        for key in self.tile_dict:
            for item in self.tile_dict[key]:
                draw.rect(screen, white, item)

    def collision_test(self, rect):
        collisions = {'t': [], 'h': []}
        for key in self.tile_dict:
            for tile in self.tile_dict[key]:
                if rect.colliderect(tile):
                    collisions[key].append(tile)

        return collisions


map1 = Map(map1, [40, 40])


# Player


class Player:
    def __init__(self, dim):
        self.dim = dim
        self.rect = Rect(50, 50, dim[0], dim[1])
        self.colour = pink
        self.left, self.right, self.up, self.down = False, False, False, False
        self.facing = pi
        self.movement = [0, 0]

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
        collisions = m.collision_test(self.rect)
        for list in collisions.values():
            for tile in list:
                if self.movement[0] > 0:
                    self.rect.right = tile.left
                if self.movement[0] < 0:
                    self.rect.left = tile.right

        self.rect.y += self.movement[1]
        collisions = m.collision_test(self.rect)
        for list in collisions.values():
            for tile in list:
                if self.movement[1] > 0:
                    self.rect.bottom = tile.top
                if self.movement[1] < 0:
                    self.rect.top = tile.bottom

    def draw_player(self):
        draw.rect(screen, self.colour, self.rect)

    def direction(self):  # all directions are in radians

        if self.movement[0] > 0 and self.movement[1] == 0:
            self.facing = pi * 0.5

        if self.movement[0] < 0 and self.movement[1] == 0:
            self.facing = pi * 1.5

        if self.movement[0] == 0 and self.movement[1] > 0:
            self.facing = pi

        if self.movement[0] == 0 and self.movement[1] < 0:
            self.facing = pi * 2

        elif self.movement[0] > 0 and self.movement[1] > 0:
            self.facing = pi * 0.75

        elif self.movement[0] > 0 > self.movement[1]:
            self.facing = pi * 0.25

        elif self.movement[0] < 0 < self.movement[1]:
            self.facing = pi * 1.25

        elif self.movement[0] < 0 and self.movement[1] < 0:
            self.facing = pi * 1.75


player1 = Player([40, 40])


# Weapon
class Sword:
    def __init__(self, dim):
        self.dim = dim
        self.rect = Rect(0, 0, dim[0], dim[1])
        self.swinging = False
        self.theta = [player1.facing - 0.78539816, player1.facing + 0.78539816]  # rendered direction, final position

    def swing(self, player):

        if self.swinging and self.theta[0] < self.theta[1]:
            radius = 30
            rotation_point = [(player.rect.x + player1.dim[0] / 2), (player.rect.y + player1.dim[1] / 2)]
            self.rect.x, self.rect.y = (rotation_point[0] + sin(self.theta[0]) * radius - self.dim[0] / 2), \
                                       (rotation_point[1] - cos(self.theta[0]) * radius - self.dim[1] / 2)

            draw.rect(screen, red, self.rect)

            self.theta[0] += pi / fps

        else:
            self.swinging = False


sword = Sword([2, 2])

# Main Loop
x = 0
game_loop = True
while game_loop:
    # FPS
    fps = 60
    time.Clock().tick(fps)
    screen.fill(turquoise)

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

            if event.key == K_SPACE and not sword.swinging:
                sword.swinging = True
                sword.theta = [player1.facing - 0.78539816, player1.facing + 0.78539816]

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                player1.right = False
            if event.key == K_LEFT:
                player1.left = False
            if event.key == K_DOWN:
                player1.down = False
            if event.key == K_UP:
                player1.up = False

    player1.move(map1)
    player1.direction()
    player1.draw_player()

    map1.draw_tiles()

    sword.swing(player1)

    display.update()
