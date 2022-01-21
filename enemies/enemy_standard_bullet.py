import pygame
import os

import utils

image_enemy_standard_bullet_path = os.path.join('assets', 'sprites', 'space-bullets', 'enemy-standard-bullet.png')

image_enemy_standard_bullet_path = utils.resource_path(image_enemy_standard_bullet_path)

class EnemyStandardBullet(pygame.sprite.Sprite):
    def __init__(self, enemy_stanard_rect, posx):
        super(EnemyStandardBullet, self).__init__()
        self.image = pygame.image.load(image_enemy_standard_bullet_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = enemy_stanard_rect.centerx + posx
        self.rect.centery = enemy_stanard_rect.centery
        self.speed = 15

    def update(self, screen_surface):
        self.move()
        if self.rect.top > utils.SCREEN_HEIGHT:
            self.kill()

    def move(self):
        self.rect.centery += self.speed

    def draw(self, screen_surface):
        screen_surface.blit(self.image, self.rect)
