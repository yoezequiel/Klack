from key_listener import KeyListener
from sound_manager import SoundManager
from gui import main

if __name__ == "__main__":
    sound_manager = SoundManager()
    key_listener = KeyListener(sound_manager)
    key_listener.start()
    main()
