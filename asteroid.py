import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle_delta = random.uniform(20, 50)
        nr = self.radius - ASTEROID_MIN_RADIUS
        x = self.position.x
        y = self.position.y

        velocity1 = self.velocity.rotate(angle_delta) * 1.5
        velocity2 = self.velocity.rotate(-angle_delta) * 1.5
        ast1 = Asteroid(x, y, nr)
        ast1.velocity = velocity1
        ast2 = Asteroid(x, y, nr)
        ast2.velocity = velocity2
        print(f"asteroid split @ {(x, y)} w/ 1:{velocity1} 2:{velocity2}")
