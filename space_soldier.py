""" Space Soldier, by romariops ifrnromariosilva@gmail.com
*
* (Pygame) A simple infinity run style game
*
* Sprites: https://opengameart.org/content/barrier-frontier-spaceships
*          https://opengameart.org/content/space-ship-construction-kit
*          https://opengameart.org/content/sci-fi-space-simple-bullets
*          https://opengameart.org/content/explosion
*          Autor
* Sounds: https://opengameart.org/content/retro-shooter-sound-effects
* Fonts: https://www.dafont.com/pt/alien-eclipse.font
"""

import pygame
from pygame.time import Clock
from pygame.locals import *
import sys
import os

import utils
from background import Background
from enemies.enemies_manager import EnemiesManager
from player.player_manager import PlayerManager
from target import Target



pygame.init()
pygame.mixer.init()
FPS = 30
clock = Clock()
SCREEN_SURFACE = pygame.display.set_mode((utils.SCREEN_WIDTH, utils.SCREEN_HEIGHT))
pygame.display.set_caption("Space Soldier")

font_path = os.path.join('assets', 'fonts', 'Alien-Eclipse.ttf')


class Game:
    def __init__(self):
        self.background = Background()
        self.player_manager = PlayerManager()
        self.enemies_manager = EnemiesManager()
        self.cont_frame = 0
        self.target = Target()
        self.mouse_on_screen = False
        self.start = False
        self.title_part_a = "Space"
        self.title_part_b = "Soldier"
        self.font_title = pygame.font.Font(font_path, 90)
        self.font_score_on_pause = pygame.font.Font(font_path, 40)
        self.font_score = pygame.font.Font(font_path, 24)
        self.info_autor_font = pygame.font.Font(font_path, 18)
        self.score = 0
        self.draw_title_first_time = True

    def draw_title(self):
        if not self.draw_title_first_time:
            score_text = "Scores "+str(self.player_manager.score)
            score_surface = self.font_score_on_pause.render(score_text, True, (255, 165, 0))
            x = int(utils.SCREEN_WIDTH / len(score_text))
            SCREEN_SURFACE.blit(score_surface, (x, 300))
        
        autor_info_text = "By romariops"
        autor_info_text_surface = self.info_autor_font.render(autor_info_text, True, (255, 165, 0))
        SCREEN_SURFACE.blit(autor_info_text_surface, (20, 20))

        autor_info_text = "github.com/romariops/space-soldier"
        autor_info_text_surface = self.info_autor_font.render(autor_info_text, True, (255, 165, 0))
        SCREEN_SURFACE.blit(autor_info_text_surface, (20, 45))

        title_surface = self.font_title.render(self.title_part_a, True, (255, 69, 0))
        SCREEN_SURFACE.blit(title_surface, (65, 100))

        title_surface = self.font_title.render(self.title_part_b, True, (255, 69, 0))
        SCREEN_SURFACE.blit(title_surface, (20, 200))

    def draw_score(self, score):
        score_text = str(score)
        score_surface = self.font_score.render(score_text, True, (255, 165, 0))
        x = 20
        SCREEN_SURFACE.blit(score_surface, (x, 20))

    def start_game(self):
        self.enemies_manager.create(self.cont_frame)
        self.enemies_manager.fire(SCREEN_SURFACE, self.cont_frame)
        self.enemies_manager.update(SCREEN_SURFACE, self.cont_frame)

    def palse_game(self):
        while len(self.player_manager.player_group) == 0:
            self.enemies_manager.enemy_group.empty()
            self.enemies_manager.bullet_group.empty()
            self.target.target_on_player = False
            self.player_manager.create(200, 550)

    def draw_player(self, x, y):
        self.player_manager.update(SCREEN_SURFACE, x, y, self.target)
        self.player_manager.fire(SCREEN_SURFACE, self.cont_frame)

    def run(self):
        x = 0
        y = 0
        score = 0

        while True:
            self.cont_frame += 1
            if self.cont_frame == 100:
                self.cont_frame = 0

            for event in pygame.event.get():
                if event.type == MOUSEMOTION:
                    if event.pos[0] == 0 or event.pos[0] >= utils.SCREEN_WIDTH - 5 or \
                            event.pos[1] == 0 or event.pos[1] >= utils.SCREEN_HEIGHT - 5:
                        self.mouse_on_screen = False
                    else:
                        self.mouse_on_screen = True
                        x = event.pos[0]
                        y = event.pos[1]
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.background.draw_background(SCREEN_SURFACE)

            if self.target.target_on_player:
                self.draw_title_first_time = False
                self.start = True
            if self.start:
                self.start_game()
                self.draw_score(score)

            score += self.enemies_manager.destroy(SCREEN_SURFACE, self.player_manager.bullet_group)

            enemies = self.enemies_manager.enemy_group
            enemy_bullets = self.enemies_manager.bullet_group

            if self.player_manager.destroy(enemies, enemy_bullets):
                self.start = False
                self.player_manager.score = score
                score = 0

            if not self.start:
                self.palse_game()
                self.draw_title()

            self.draw_player(x, y)

            player_rect = self.player_manager.player.rect
            if self.mouse_on_screen:
                self.target.update(SCREEN_SURFACE, x, y, player_rect)

            else:
                self.target.update(SCREEN_SURFACE, -100, -100, player_rect)

            pygame.display.update()
            clock.tick(FPS)


if __name__ == "__main__":
    Game().run()
