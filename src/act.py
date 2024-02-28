from gpiozero import MotionSensor
from .models import ActiveSound
from playsound import playsound

def play_active_sound():
    active_sound = ActiveSound()
    active_sound_path = active_sound.get_active_sound_path()

    if not active_sound_path.exists():
        print(f"Active sound file '{active_sound_path}' not found")
        return

    playsound(active_sound_path)


def main():
    pir = MotionSensor(4)
    pir.when_motion = play_active_sound
    print("Ready")
    input("Press Enter to exit")
    print("Exiting")

if __name__ == "__main__":
    play_active_sound()
    # main()