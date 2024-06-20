from pynput import keyboard
from sound_manager import SoundManager


class KeyListener:
    def __init__(self, sound_manager):
        self.sound_manager = sound_manager
        self.listener = keyboard.Listener(on_press=self.on_press)

    def on_press(self, key):
        self.sound_manager.play_sound()

    def start(self):
        self.listener.start()

    def stop(self):
        self.listener.stop()
