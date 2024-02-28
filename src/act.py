from gpiozero import MotionSensor
from .models import ActiveSound
from playsound import playsound

def play_active_sound():
    active_sound = ActiveSound()
    active_sound_path = active_sound.get_active_sound_path()

    if not active_sound_path or not active_sound_path.exists():
        print(f"Active sound file '{active_sound_path}' not found")
        return
    
    # Spawn aplay
    playsound(active_sound_path)


def main():
    pir = MotionSensor(4)

    while True:
        try:
            pir.wait_for_motion()
            play_active_sound()
            pir.wait_for_no_motion()
        except KeyboardInterrupt:
            break

        except:
            pass


if __name__ == "__main__":
    play_active_sound()
    main()
