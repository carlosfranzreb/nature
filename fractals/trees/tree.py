import math
import pygame
import sys
from vector import Vector


SCREEN = pygame.Rect(0, 0, 640, 480)
SIN_60 = math.sin(math.radians(60))  # used in the equilateral triangles


class Line:
    def __init__(self, start, end, width):
        self.start = start
        self.end = end
        self.width = round(width)
        self.branch = True

    def draw(self, screen):
        pygame.draw.line(screen, (0, 0, 0), self.start, self.end, self.width)


def generate(tree, angle):
    branches = []
    for t in tree:
        if t.branch:
            t.branch = False
            branch = Vector.div([t.start, t.end], 1.5)
            branch = Vector.move(branch, [t.start, t.end])
            right = Vector.rotate(branch, angle)
            left = Vector.rotate(branch, -angle)
            branches.append([right, t.width-0.5])
            branches.append([left, t.width-0.5])

    for b in branches:
        tree.append(Line(b[0][0], b[0][1], b[1]))

    return tree


def main(recursion_limit, angle):
    pygame.init()
    screen = pygame.display.set_mode(SCREEN[2:4])

    tree = [Line([SCREEN[2]/2, SCREEN[3]], [SCREEN[2]/2, 320], 5)]
    for _ in range(recursion_limit):
        tree = generate(tree, angle)

    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))
        for l in tree:
            l.draw(screen)

        pygame.display.flip()
        pygame.time.Clock().tick(1)  # cap the framerate


if __name__ == '__main__':
    main(15, 20)
