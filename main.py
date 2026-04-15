
import sys
import pygame
from constants import SCREEN_HEIGHT , SCREEN_WIDTH
from logger import log_state
from logger import log_event
from player import Player 
from asteroid import Asteroids
from asteroidfield import AsteroidField
from shot import Shot


def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt=0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2


    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()


    # containers
    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots,updatable,drawable)
    AsteroidField.containers = (updatable)

    # instances
    asteroidfield_obj = AsteroidField()
    player = Player(x,y)


    # game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)   

        for obj in asteroids:
            
            if player.collides_with(obj):
                log_event("player_hit")
                print("Game over")
                sys.exit()

            for sh in shots:

                if sh.collides_with(obj):
                    log_event("asteroid_shot")
                    sh.kill()
                    obj.split()    


        screen.fill("black") 
    
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000
        



if __name__ == "__main__":
    main()
