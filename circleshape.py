import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_check(self, other):
        distance = self.radius + other.radius

        if hasattr(other, "shield_timer") and other.shield_timer > 0:
            distance = self.radius + SHIELD_RADIUS

        return pygame.math.Vector2.distance_to(self.position, other.position) <= distance
