import pygame
from src.game_logic import update_game_state
from src.character import player_character
from src.enemy import enemies
from src.level import current_level
from src.graphics import game_graphics, render_game
from src.sound import game_sounds
from src.input import input_handler
from src.settings import game_settings
from src.save_load import save_game, load_game

def main():
    pygame.init()
    game_state = "start"
    while game_state != "quit":
        input_handler(game_state, player_character, enemies, current_level, game_settings)
        update_game_state(game_state, player_character, enemies, current_level, game_settings)
        render_game(game_graphics, game_sounds, player_character, enemies, current_level)
        if game_state == "save":
            save_game(game_state, player_character, enemies, current_level, game_settings, game_graphics, game_sounds)
        elif game_state == "load":
            load_game(game_state, player_character, enemies, current_level, game_settings, game_graphics, game_sounds)
    pygame.quit()

if __name__ == "__main__":
    main()