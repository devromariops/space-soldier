import pygame
import os

import utils
from enemies.enemy_standard_bullet import EnemyStandardBullet

image_enemy_standard_path = os.path.join('assets', 'sprites', 'space-ships', 'enemy-standard.png')


class EnemyStandard(pygame.sprite.Sprite):
    def __init__(self, midbottom_x, midbottom_y):
        super(EnemyStandard, self).__init__()
        self.image = pygame.image.load(image_enemy_standard_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (midbottom_x, midbottom_y)
        self.velocity = 5

    def move(self):
        self.rect.top += self.velocity

    def draw(self, screen_surface):
        screen_surface.blit(self.image, self.rect)

    def update(self, screen_surface, cont_frame):
        self.move()
        self.draw(screen_surface)
        if self.rect.top > utils.SCREEN_HEIGHT:
            self.kill()

    def fire(self):
        posx1 = -10
        posx2 = 10
        return [EnemyStandardBullet(self.rect, posx1), EnemyStandardBullet(self.rect, posx2)]
