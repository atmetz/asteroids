import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)    
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    # create player
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # create asteroid field
    asteroid_field = AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black")

        # udpate objects position/rotation
        updatable.update(dt)

        for aster in asteroids:
            if player1.collision(aster):
                print("Game Over!")
                return

        # draw objects
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        # limit the frame rate
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()