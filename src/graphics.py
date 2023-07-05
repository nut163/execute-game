import pygame
from pygame.locals import *

class Graphics:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.background = pygame.image.load('assets/graphics/game_background.png')
        self.UI = pygame.image.load('assets/graphics/game_UI.png')

    def draw_character(self, player_character):
        character_sprite = pygame.image.load('assets/characters/character_sprites.png')
        self.screen.blit(character_sprite, (player_character.x, player_character.y))

    def draw_enemies(self, enemies):
        enemy_sprite = pygame.image.load('assets/enemies/enemy_sprites.png')
        for enemy in enemies:
            self.screen.blit(enemy_sprite, (enemy.x, enemy.y))

    def draw_level(self, current_level):
        level_design = open('assets/levels/level_designs.txt', 'r')
        for line in level_design:
            for tile in line:
                if tile == '1':
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x, y, 32, 32))
                x += 32
            y += 32
            x = 0

    def update_display(self):
        pygame.display.flip()

game_graphics = Graphics()