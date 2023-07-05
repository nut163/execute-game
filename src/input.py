import pygame
from pygame.locals import *

def input_handler(game_state, player_character, game_settings):
    for event in pygame.event.get():
        if event.type == QUIT:
            game_state['running'] = False
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                player_character.move_up()
            elif event.key == K_DOWN:
                player_character.move_down()
            elif event.key == K_LEFT:
                player_character.move_left()
            elif event.key == K_RIGHT:
                player_character.move_right()
            elif event.key == K_SPACE:
                player_character.attack()
            elif event.key == K_ESCAPE:
                game_state['paused'] = not game_state['paused']
            elif event.key == K_s:
                save_game(game_state, player_character, game_settings)
            elif event.key == K_l:
                load_game(game_state, player_character, game_settings)