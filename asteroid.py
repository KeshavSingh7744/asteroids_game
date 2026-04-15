from circleshape import CircleShape
from constants import *

import pygame
import random
from logger import log_event


class Asteroids(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)



    def update(self,dt):
        self.position += self.velocity * dt      


    def split(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return

        else:
            log_event("asteroid_split")
            rand_angle = random.uniform(20,50)

            new_rot1 = self.velocity.rotate(rand_angle)
            new_rot2 = self.velocity.rotate(-1*rand_angle)

            new_r_small = self.radius - ASTEROID_MIN_RADIUS

            ast1 = Asteroids(self.position.x,self.position.y, new_r_small)
            ast2 = Asteroids(self.position.x,self.position.y, new_r_small)

            ast1.velocity = new_rot1*1.2
            ast2.velocity = new_rot2*1.2





