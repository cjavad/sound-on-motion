from pathlib import Path 

TEMPLATE_PATH = Path(__file__).parent / "templates"
STATIC_PATH = Path(__file__).parent / "static"
SOUND_PATH = STATIC_PATH / "sounds"
ACTIVE_SOUND_FILE = STATIC_PATH / "active_sound.txt"