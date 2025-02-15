import pygame
from circleshape import *
from constants import *

# Asteroid class
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # draw asteroid on screen
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    # update for asteroid movement
    def update(self, dt):
        self.position += (self.velocity * dt)