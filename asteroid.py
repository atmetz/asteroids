import pygame
from circleshape import *
from constants import *
import random

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

    # split asteroid on hit
    def split(self):

        self.kill()

        # check asteroid size
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # create 2 new asteroids
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)            
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            # set new asteroids velocity
            asteroid1.velocity = self.velocity * 1.2
            asteroid1.velocity = asteroid1.velocity.rotate(random_angle)
            asteroid2.velocity = self.velocity * 1.2
            asteroid2.velocity = asteroid2.velocity.rotate(-random_angle)
            

        
        