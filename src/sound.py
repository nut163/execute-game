import pygame
from pygame import mixer

class GameSounds:
    def __init__(self):
        self.background_music = 'assets/sounds/background_music.wav'
        self.sound_effects = 'assets/sounds/sound_effects.wav'

    def play_background_music(self):
        mixer.music.load(self.background_music)
        mixer.music.play(-1)

    def play_sound_effect(self, effect):
        sound = mixer.Sound(self.sound_effects)
        sound.play()

game_sounds = GameSounds()

def render_game():
    game_sounds.play_background_music()