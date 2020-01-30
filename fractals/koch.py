import math
import pygame
import sys
from vector import Vector


SCREEN = pygame.Rect(0, 0, 640, 480)
SIN_60 = math.sin(math.radians(60))  # used in the equilateral triangles


class Koch_line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, screen):
        pygame.draw.line(screen, (0, 0, 0), self.start, self.end, 2)


def koch(lines):
    new_lines = []
    for l in lines:
        start = l.start
        end = l.end
        tri_left = Vector.div(start, end, 3)[1]
        rotation = Vector.rotate(Vector.sub(tri_left, start), -60)
        tri_top = Vector.add(tri_left, rotation)
        tri_right = Vector.div(start, end, 3/2)[1]

        new_lines.append(Koch_line(start, tri_left))
        new_lines.append(Koch_line(tri_left, tri_top))
        new_lines.append(Koch_line(tri_top, tri_right))
        new_lines.append(Koch_line(tri_right, end))

    return new_lines


def main(recursion_limit):
    pygame.init()
    screen = pygame.display.set_mode(SCREEN[2:4])

    lines = [Koch_line([0, 2*SCREEN[3]/3], [SCREEN[2], 2*SCREEN[3]/3])]
    for _ in range(recursion_limit):
        lines = koch(lines)

    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))
        for l in lines:
            l.draw(screen)

        pygame.display.flip()
        pygame.time.Clock().tick(1)  # cap the framerate


if __name__ == '__main__':
    main(5)
