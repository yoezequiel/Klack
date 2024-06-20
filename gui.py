import tkinter as tk
from tkinter import ttk
from sound_manager import SoundManager
from config import load_config


class App:
    def __init__(self, root, sound_manager):
        self.root = root
        self.sound_manager = sound_manager
        self.root.title("Teclado Mecánico Virtual")
        self.create_widgets()

    def create_widgets(self):
        config = load_config()

        self.sound_var = tk.StringVar(value=config["sound_name"])
        sound_menu = ttk.OptionMenu(
            self.root,
            self.sound_var,
            self.sound_var.get(),
            *self.get_sound_options(),
            command=self.change_sound,
        )
        sound_menu.pack(pady=10)

        self.volume_slider = ttk.Scale(
            self.root, from_=0, to=1, orient="horizontal", command=self.change_volume
        )
        self.volume_slider.set(config["volume"])
        self.volume_slider.pack(pady=10)

    def get_sound_options(self):
        sound_options = ["CherryMX", "HolyPanda", "SilentRed"]
        return sound_options

    def change_sound(self, sound_name):
        sound_path = f"sounds/{sound_name.lower()}.mp3"
        print(f"Changing sound to: {sound_name} at {sound_path}")
        self.sound_manager.set_sound(sound_name, sound_path)

    def change_volume(self, volume):
        self.sound_manager.set_volume(float(volume))


def main():
    root = tk.Tk()
    sound_manager = SoundManager()
    app = App(root, sound_manager)
    root.mainloop()
