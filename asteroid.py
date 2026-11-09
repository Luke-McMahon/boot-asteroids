
import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius >= ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            first = self.velocity.rotate(angle)
            second = self.velocity.rotate(-angle)

            radius = self.radius - ASTEROID_MIN_RADIUS
            one = Asteroid(self.position.x, self.position.y, radius)
            one.velocity = first * 1.2
            two = Asteroid(self.position.x, self.position.y, radius)
            two.velocity = second * 1.2

