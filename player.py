import pygame
from circleshape import *
from constants import *
from shot import *

# Player class
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # player shape is a triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # draw player on screen
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # rotate player
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # move player
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # shoot
    def shoot(self):
        shot_direction = pygame.Vector2(0,1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y, shot_direction)
        shot.velocity = self.velocity * PLAYER_SHOOT_SPEED
        pass

    # update for player movement
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # rotate right
        if keys[pygame.K_a]:
            self.rotate(-dt)
        # rotate left
        if keys[pygame.K_d]:
            self.rotate(dt)

        # move forward
        if keys[pygame.K_w]:
            self.move(dt)

        # move forward
        if keys[pygame.K_s]:
            self.move(-dt)

        # spacebar to shoot
        if keys[pygame.K_SPACE]:
            self.shoot()

