import pickle

game_state = None
player_character = None
enemies = None
current_level = None
game_settings = None
game_graphics = None
game_sounds = None

def save_game():
    global game_state, player_character, enemies, current_level, game_settings, game_graphics, game_sounds
    with open('savegame.pkl', 'wb') as f:
        pickle.dump((game_state, player_character, enemies, current_level, game_settings, game_graphics, game_sounds), f, pickle.HIGHEST_PROTOCOL)

def load_game():
    global game_state, player_character, enemies, current_level, game_settings, game_graphics, game_sounds
    with open('savegame.pkl', 'rb') as f:
        game_state, player_character, enemies, current_level, game_settings, game_graphics, game_sounds = pickle.load(f)