import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            EXPLOSION_SOUND.play()
            return
        else:
            SPLIT_SOUND.play()
            SPLIT_SOUND.set_volume(0.4)
            rand_angle = random.uniform(20, 50)
            rotated1 = self.velocity.rotate(rand_angle)
            rotated2 = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid1.velocity = rotated1 * 1.2
            new_asteroid2.velocity = rotated2 * 1.2


