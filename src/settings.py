class Settings:
    def __init__(self):
        self.resolution = (800, 600)
        self.fullscreen = False
        self.sound_volume = 1.0
        self.music_volume = 1.0

game_settings = Settings()

def save_settings():
    with open('settings.json', 'w') as f:
        json.dump(game_settings.__dict__, f)

def load_settings():
    global game_settings
    try:
        with open('settings.json', 'r') as f:
            settings_data = json.load(f)
            game_settings = Settings()
            game_settings.__dict__.update(settings_data)
    except FileNotFoundError:
        save_settings()