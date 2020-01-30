import pygame
import sys


SCREEN = pygame.Rect(0, 0, 640, 480)


def cantor(screen, x_1, x_2, y):
    pygame.draw.line(screen, (0, 0, 0), (x_1, y), (x_2, y), 2)

    y += 30
    if y >= SCREEN[3]:
        return
    else:
        length = (x_2 - x_1) / 3
        cantor(screen, x_1, x_1 + length, y)
        cantor(screen, x_1 + 2*length, x_2, y)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN[2:4])

    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))
        cantor(screen, 1, SCREEN[2], 5)

        pygame.display.flip()
        pygame.time.Clock().tick(1)  # cap the framerate


if __name__ == '__main__':
    main()
