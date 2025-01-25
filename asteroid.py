import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    

    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            # Generate a random angle in degrees for splitting directions
            angle = random.uniform(20,50)
            # Reduce size of new asteroids
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            # Create asteroids in opposite directions
            for direction in (1, -1):
                offset_angle = angle * direction
                new_v = self.velocity.rotate(offset_angle)*1.2
                # New asteroid inherits modified velocity and is added to sprite groups
                new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                new_asteroid.velocity = new_v
