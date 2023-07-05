```python
import os
from src.character import player_character
from src.enemy import enemies

game_state = None
current_level = None

def load_level(level_number):
    global current_level
    with open(f'assets/levels/level_designs.txt', 'r') as file:
        levels = file.readlines()
        current_level = levels[level_number].strip()

def spawn_enemies():
    global enemies
    enemies = []
    for i in range(current_level.count('E')):
        enemies.append(Enemy())

def spawn_player():
    global player_character
    player_character = Character()

def initialize_level(level_number):
    global game_state
    load_level(level_number)
    spawn_enemies()
    spawn_player()
    game_state = 'PLAYING'

def update_level():
    global game_state
    if player_character.health <= 0:
        game_state = 'GAME_OVER'
    elif not enemies:
        game_state = 'LEVEL_COMPLETE'
```
