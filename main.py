import pygame
from constants import *
from player import *
from asteroidfield import *
from shot import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable) 


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asf = AsteroidField()

    while True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for e in updatable:
            e.update(dt)
        
        for e in asteroids:
            if e.is_collided(player):
                print("Game over!")
                return

        for e in asteroids:
            for s in shots:
                if e.is_collided(s):
                    e.split()

        for e in drawable:
            e.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()
