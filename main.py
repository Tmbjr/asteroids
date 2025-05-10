import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    pygame.init()
    pygame.mixer.init()
     
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill((0, 0, 0))
    
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                return
           
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision_check(asteroid):
                    shot.kill()
                    asteroid.split()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
