import pygame
import sys
from player import Player
from asteroid import Asteroid
from constants import *
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player1 = Player(x,y)
    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60) / 1000

        for sprite in updatable:
            sprite.update(dt)

        for sprite in asteroids:
            if sprite.check_collision(player1):
                print("Game over!")
                sys.exit()
        
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()

if __name__=="__main__":
    main()