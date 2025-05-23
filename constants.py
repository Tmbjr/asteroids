import pygame
pygame.mixer.init()     

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (35, 35, 255)
GREEN = (35, 255, 35)
RED = (255, 35, 35)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

POWERUP_SPAWN_RATE = 15
POWERUP_DURATION = 5

PLAYER_RADIUS = 20
SHIELD_RADIUS = PLAYER_RADIUS + 20

PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.30

SHOT_RADIUS = 5

SHOOT_SOUND = pygame.mixer.Sound("sounds/shoot2.wav")
EXPLOSION_SOUND = pygame.mixer.Sound("sounds/explosion.wav")
SPLIT_SOUND = pygame.mixer.Sound("sounds/split.wav")
RAPID_SOUND = pygame.mixer.Sound("sounds/rapid.wav")
SHIELD_SOUND = pygame.mixer.Sound("sounds/shield.wav") 
HUM_SOUND = pygame.mixer.Sound("sounds/shield_hum.wav")