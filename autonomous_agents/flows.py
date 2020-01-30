"""
The mouse follows the flow field.
"""


import pygame
import sys
import math
from flow_field import Flow_field
from mouse import Mouse


SCREEN = pygame.Rect(0, 0, 640, 480)


def main():
    pygame.init()

    black = 0, 0, 0
    screen = pygame.display.set_mode(SCREEN[2:4])

    mouse = Mouse(SCREEN)
    field = Flow_field(SCREEN)
    field.perlin()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        row = math.floor(mouse.rect.centery / 10) - 1
        col = math.floor(mouse.rect.centerx / 10) - 1
        try:
            cell = field.grid[row][col]
            mouse.follow_field(cell)
        except IndexError:
            print(mouse.rect.center)
            print(row, col)
            print(len(field.grid), len(field.grid[0]))
            return

        screen.fill(black)
        field.draw_arrows(screen)
        screen.blit(mouse.image, mouse.rect)
        pygame.display.flip()
        pygame.time.Clock().tick(35)  # cap the framerate


if __name__ == '__main__':
    main()
