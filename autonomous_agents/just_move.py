"""
The mouse just moves around.
"""


import math
import pygame
import sys


class Mouse:
    def __init__(self):
        self.image = pygame.image.load("images/mouse.png")
        self.rect = self.image.get_rect()
        self.angle = 0

    def steer(self, speed):
        """
        Speed = (-1, -1) => Angle = 0
        Rotate it so that its point is always at its front
        The angle argument represents degrees and can be any floating
        point value. Negative angle amounts will rotate clockwise.
        """
        angle_should = math.degrees(math.atan(speed[1] / speed[0]))
        if speed[1] >= 0:
            angle_should = 180 + angle_should
        if angle_should < 0:
            angle_should = 360 + angle_should

        rotation = angle_should - self.angle
        self.image = pygame.transform.rotate(self.image, rotation)
        self.angle = angle_should


def main():
    pygame.init()

    size = width, height = 640, 480
    speed = [2, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    mouse = Mouse()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        mouse.rect = mouse.rect.move(speed)
        if mouse.rect.left < 0 or mouse.rect.right > width:
            speed[0] = -speed[0]
        if mouse.rect.top < 0 or mouse.rect.bottom > height:
            speed[1] = -speed[1]

        mouse.steer(speed)

        pygame.time.Clock().tick(100)

        screen.fill(black)
        screen.blit(mouse.image, mouse.rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()
