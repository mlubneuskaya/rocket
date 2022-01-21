import math

import pygame


class Rocket(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, vector, image=None):
        if image:
            self.image = image
        self.rect.x += vector.x
        self.rect.y += vector.y

    def get_position(self):
        return self.rect.x, self.rect.y

    def set_image(self, image):
        self.image = image

    def get_distance(self, rocket):
        distance = pow(self.rect.x - rocket.rect.x, 2) + pow(self.rect.y - rocket.rect.y, 2)
        return math.sqrt(distance)

    def __str__(self):
        return f'x = {self.rect.x}, y = {self.rect.y}'


class AutoPilotRocket(Rocket):
    def __init__(self, x, y, image, parent_screen, delay, vector):
        super().__init__(x, y, image)
        self.parent_screen = parent_screen
        self.delay = delay
        self.vector = vector

    def update(self, vector, image=None):
        if image:
            self.image = image
        if self.rect.x + vector.x < 0 or self.rect.x + vector.x > self.parent_screen.get_width():
            vector.x, vector.y = -vector.y, vector.x
        elif self.rect.y - vector.y < 0 or self.rect.y - vector.y > self.parent_screen.get_height():
            vector.x, vector.y = -vector.y, vector.x
        self.rect.x += vector.x
        self.rect.y -= vector.y  # increasing y means sprite goes downwards
        pygame.time.delay(self.delay)
