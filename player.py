from circleshape import CircleShape
from shot import Shot
from constants import *
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.rapid_timer = 0
        self.shield_timer = 0
        self.super_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)
        if self.shield_timer > 0:
            pygame.draw.circle(screen, GREEN, self.position, SHIELD_RADIUS, 2)

    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time


    def update(self, dt):
        if self.rapid_timer > 0:
            self.timer -= (dt * 2)
            self.rapid_timer -= dt
        elif self.shield_timer > 0:
            self.shield_timer -= dt
            self.timer -= dt
        elif self.super_timer > 0:
            self.super_timer -= dt
        else:
            self.timer -= dt
            

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            if self.timer > 0:
                return
            else:
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    
    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot_vec = pygame.Vector2(0, 1)
        rotated = shot_vec.rotate(self.rotation)
        velocity = rotated * PLAYER_SHOOT_SPEED

        new_shot.velocity = velocity
        SHOOT_SOUND.play()
        SHOOT_SOUND.set_volume(0.4) 
