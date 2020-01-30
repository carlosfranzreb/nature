import pygame
import math
from perlin_arr import Perlin
from vector import Vector


class Flow_field:
    def __init__(self, screen):
        self.screen = screen
        # self.grid = [[[0, 0]] * int(screen[2]/10)] * int(screen[3]/10)
        self.grid = [[[0, 0] for _ in range(int(screen[2]/10))] for _ in
                     range(int(screen[3]/10))]

    def right(self):
        self.grid = [[[1, 0]] * int(self.screen[2]/10)] * \
                     int(self.screen[3]/10)

    def draw_arrows(self, screen):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                center = (j*10 + 5, i*10 + 5)
                norm_arrow = Vector.norm(self.grid[i][j])
                arrow = [i*5 for i in norm_arrow]
                end_pos = [center[i] + arrow[i] for i in range(len(arrow))]
                pygame.draw.line(screen, (255, 0, 0), center, end_pos)

    def circle(self):
        """
        Each vector is orthogonal to the vector that reaches the center of
        its cell from the center of the screen, with a clockwise orientation.
        """
        screen_center = (self.screen[2] / 2, self.screen[3] / 2)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                center = [j*10 + 5, i*10 + 5]
                v = Vector.norm(Vector.sub(center, screen_center))
                v = [i * 5 for i in v]
                self.grid[i][j] = [-v[1], v[0]]  # orthogonal

    def perlin(self):
        """
        Every vector can't be very far off of its 8 neighbors.
        """
        perlin = Perlin()
        noise = perlin.perlin_noise(len(self.grid[0]), len(self.grid), 0.1)
        angles = [i * 360 for i in noise]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                ang = angles[i][j]
                if ang < 0:
                    ang = 360 - ang
                x = math.tan(angles[i][j])
                if ang >= 0 and ang < 90 or ang > 270 and ang <= 360:
                    vector = [x, 1]
                elif ang == 90:
                    vector = [1, 0]
                elif ang > 90 and ang <= 180:
                    vector = [-x, -1]
                elif ang > 180 and ang < 270:
                    vector = [-x, 1]
                elif ang == 270:
                    vector = [-1, 0]

                norm_vector = Vector.norm(vector)
                self.grid[i][j] = [x * 5 for x in norm_vector]
