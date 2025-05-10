from constants import *
from circleshape import CircleShape

class Powerup(CircleShape):
    def __init__(self, x, y, radius, type_index):
        super().__init__(x, y, radius)
        self.types = ["rapid", "shield", "super"]
        self.type = self.types[type_index]

    def draw(self, screen):
        color = None
        if self.type == "rapid":
            color = BLUE
        elif self.type == "shield":
            color = GREEN
        elif self.type == "super":
            color = RED

        pygame.draw.rect(screen, color, pygame.Rect(self.position.x, self.position.y, 20, 20), 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)