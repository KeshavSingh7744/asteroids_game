import pygame
from constants import SCREEN_HEIGHT , SCREEN_WIDTH
from logger import log_state
from player import Player 
from asteroid import Asteroids
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt=0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    asteroidfield_obj = AsteroidField()

    player = Player(x,y)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)        

        screen.fill("black") 
    
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000
        



if __name__ == "__main__":
    main()
