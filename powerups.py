from constants import *
from circleshape import CircleShape

class Powerup(CircleShape):
    def __init__(self, x, y, radius, type):
        super().__init__(x, y, radius)
        self.type = type

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, pygame.Rect(self.position.x, self.position.y, 20, 20), 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)