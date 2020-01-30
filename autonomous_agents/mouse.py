import math
import pygame
from vector import Vector


class Mouse:
    def __init__(self, SCREEN):
        self.screen = SCREEN
        self.orig_image = pygame.image.load("images/mouse.png").convert_alpha()
        self.image = self.orig_image
        self.rect = self.image.get_rect(center=self.screen.center)
        self.angle = 0
        self.speed = [0, 0]
        self.max_speed = 15
        self.acceleration = 5

    def follow_mouse(self):
        """
        Locates itself and the mouse, and moves towards it.
        """
        x, y = Vector.sub(pygame.mouse.get_pos(), self.rect.center)
        if abs(x) + abs(y) < 10:  # don't move if distance so small
            return

        else:
            # steering force = desired velocity - current velocity
            force = Vector.sub([x, y], self.speed)
            if Vector.mag(force) > self.acceleration:
                force = [i * 3 for i in Vector.norm(force)]
            force = [math.floor(i) for i in force]

            # new direction = old direction + steering force
            self.speed = Vector.add(self.speed, force)
            if Vector.mag(self.speed) > self.max_speed:
                norm_speed = Vector.norm(self.speed)
                mag_norm_speed = Vector.mag(norm_speed)
                self.speed = norm_speed
                while Vector.mag(self.speed) < self.max_speed - mag_norm_speed:
                    self.speed = Vector.add(self.speed, norm_speed)
                self.speed = [math.floor(i) for i in self.speed]

            self.steer()
            self.move()

    def follow_field(self, force):
        """
        The mouse follows the direction given by the vector beneath it.
        """
        # steering force = desired velocity - current velocity
        if Vector.mag(force) > self.acceleration:
            force = [i * 3 for i in Vector.norm(force)]
        force = [math.floor(i) for i in force]

        # new direction = old direction + steering force
        self.speed = Vector.add(self.speed, force)
        if Vector.mag(self.speed) > self.max_speed:
            norm_speed = Vector.norm(self.speed)
            mag_norm_speed = Vector.mag(norm_speed)
            self.speed = norm_speed
            while Vector.mag(self.speed) < self.max_speed - mag_norm_speed:
                self.speed = Vector.add(self.speed, norm_speed)
            self.speed = [math.floor(i) for i in self.speed]

        self.steer()
        self.move()

    def steer(self):
        """
        Speed = (-1, -1) => Angle = 0
        Rotate it so that its point is always at its front
        The angle argument represents degrees and can be any floating
        point value. Negative angle amounts will rotate clockwise.
        """
        if self.speed[1] == 0:  # y = 0
            if self.speed[0] > 0:
                self.angle = 270
            elif self.speed[0] < 0:
                self.angle = 90

        else:  # use arctan to calculate the angle of the mouse
            self.angle = math.degrees(math.atan(self.speed[0]/self.speed[1]))
            if self.speed[1] > 0:
                self.angle += 180

        pos = self.rect.center  # rotate maintaining position
        self.image = pygame.transform.rotate(self.orig_image, self.angle) \
                                     .convert_alpha()
        self.rect = self.image.get_rect(center=pos)

    def move(self):
        self.rect.move_ip(self.speed[0], self.speed[1])
        self.rect.clamp_ip(self.screen)
