import pygame
from config import load_config, save_config


class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.config = load_config()
        self.current_sound = pygame.mixer.Sound(self.config["sound_path"])
        self.volume = self.config["volume"]
        self.current_sound.set_volume(self.volume)

    def play_sound(self):
        self.current_sound.play()

    def set_sound(self, sound_name, sound_path):
        self.current_sound = pygame.mixer.Sound(sound_path)
        self.current_sound.set_volume(self.volume)
        self.config["sound_name"] = sound_name
        self.config["sound_path"] = sound_path
        save_config(self.config)
        print(f"Sound set to: {sound_path}")

    def set_volume(self, volume):
        self.volume = volume
        self.current_sound.set_volume(self.volume)
        self.config["volume"] = volume
        save_config(self.config)
