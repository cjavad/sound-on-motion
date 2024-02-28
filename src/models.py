from typing import Optional
from pydantic import BaseModel

from .consts import ACTIVE_SOUND_FILE, SOUND_PATH

class SoundFile(BaseModel):
    id: str
    filename: str
    is_active: Optional[bool] = False

class ActiveSound:
    def __init__(self):
        self.active_sound = None
        self.load_active_sound()

    def load_active_sound(self):
        if ACTIVE_SOUND_FILE.exists():
            with open(ACTIVE_SOUND_FILE, "r") as file:
                self.active_sound = file.read().strip()

    def set_active_sound(self, sound):
        self.active_sound = sound
        with open(ACTIVE_SOUND_FILE, "w") as file:
            file.write(sound)

    def get_active_sound_path(self):
        if not self.active_sound:
            return None

        return SOUND_PATH / self.active_sound

