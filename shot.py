import pygame
from circleshape import *
from constants import *

# Shot class
class Shot(CircleShape):
    def __init__(self, x, y, shot_direction):
        super().__init__(x, y, SHOT_RADIUS)
        self.shot_direction = shot_direction

    # draw asteroid on screen
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)

    # update for asteroid movement
    def update(self, dt):
        self.position += (self.velocity * dt) + self.shot_direction