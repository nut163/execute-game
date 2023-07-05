```python
from character import player_character
from enemy import enemies
from level import current_level
from input import input_handler
from save_load import save_game, load_game

game_state = {
    'player': player_character,
    'enemies': enemies,
    'level': current_level,
}

def update_game_state():
    player_input = input_handler()
    player_character.update(player_input)
    for enemy in enemies:
        enemy.update()
    current_level.update()
    save_game(game_state)

def load_saved_game():
    global game_state
    game_state = load_game()

def start_new_game():
    global game_state
    game_state = {
        'player': player_character,
        'enemies': enemies,
        'level': current_level,
    }
    save_game(game_state)
```