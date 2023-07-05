```python
import pygame
from src.game_logic import update_game_state

class Character:
    def __init__(self, sprite_path):
        self.sprite = pygame.image.load(sprite_path)
        self.position = [0, 0]
        self.speed = 5
        self.health = 100

    def move(self, direction):
        if direction == 'up':
            self.position[1] -= self.speed
        elif direction == 'down':
            self.position[1] += self.speed
        elif direction == 'left':
            self.position[0] -= self.speed
        elif direction == 'right':
            self.position[0] += self.speed

        update_game_state()

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        global game_state
        game_state = 'game_over'

player_character = Character('assets/characters/character_sprites.png')
```