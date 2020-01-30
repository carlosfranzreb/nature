"""
The mouse follows the actual mouse.
"""


import pygame
import sys
from mouse import Mouse


SCREEN = pygame.Rect(0, 0, 640, 480)


def main():
    pygame.init()

    black = 0, 0, 0
    screen = pygame.display.set_mode(SCREEN[2:4])

    mouse = Mouse(SCREEN)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        mouse.follow_mouse()

        screen.fill(black)
        screen.blit(mouse.image, mouse.rect)
        pygame.display.flip()
        pygame.time.Clock().tick(35)  # cap the framerate


if __name__ == '__main__':
    main()
