import pygame
import os
from config import SCREEN_WIDTH



class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 5
        self.image = pygame.image.load(os.path.join("assets", "sprites", "bullet.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self, bullet_group, players, enemies):
        self.rect.x += (self.speed * (self.direction * -1))
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
