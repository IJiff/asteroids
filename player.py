import pygame
import circleshape
from constants import *
from shot import Shot


class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, pygame.Color("white"), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        self.cooldown = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position[0], self.position[1], SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def update(self, dt):
        self.cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            self.rotate(-dt)
        if keys[pygame.K_f]:
            self.rotate(dt)
        if keys[pygame.K_e]:
            self.move(dt)
        if keys[pygame.K_d]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.cooldown <= 0:
            self.shoot()
