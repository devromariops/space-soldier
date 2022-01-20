import pygame
import os

from .player_bullet import PlayerBullet

image_player_path = os.path.join('assets', 'sprites', 'space-ships', 'player.png')
sound_player_fire_path = os.path.join('assets', 'sounds', 'player_fire.mp3')


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.image = pygame.image.load(image_player_path).convert_alpha()
        self._rect = self.image.get_rect(center=(x, y))

    @property
    def rect(self):
        return self._rect

    def move(self, x, y, target):
        if target.target_on_player:
            self.rect.centerx = x
            self.rect.centery = y

    def draw(self, screen_surface):
        screen_surface.blit(self.image, self.rect)

    def update(self, screen_surface, x, y, target):
        self.move(x, y, target)
        self.draw(screen_surface)

    def fire(self):
        fire = pygame.mixer.Sound(sound_player_fire_path)
        fire.play()
        posx1, posx2 = -10, 10
        return [PlayerBullet(self.rect, posx1), PlayerBullet(self.rect, posx2)]

