import pygame
import random
from asteroid import Asteroid
from constants import *
from powerups import Powerup


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.powerup_timer = 0.0

    def spawn(self, radius, position, velocity, type):

        if type == "asteroid":
            asteroid = Asteroid(position.x, position.y, radius)
            asteroid.velocity = velocity
        elif type == "powerup":
            powerup = Powerup(position.x, position.y, radius, "rapid")
            powerup.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        self.powerup_timer += dt

        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity, "asteroid")

        if self.powerup_timer > POWERUP_SPAWN_RATE:
            self.powerup_timer = 0

            #spawn a new powerup at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(80, 120)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))

            self.spawn(20, position, velocity, "powerup")