import pygame
import time

def timer(duration):
    time_rest = duration
    while time_rest >= 0:
        mins, secs = divmod(time_rest, 60)
        print(f"{mins:02d}:{secs:02d}", end='\r')
        time.sleep(1)
        time_rest -= 1

def play_sound(number):
    if number == 0:
        pygame.mixer.Sound("sounds/level_up.wav").play()
    elif number == 1:
        pygame.mixer.Sound("sounds/Explosion_meteor.wav").play()
    else :
        pygame.mixer.Sound("sounds/big_explosion.wav").play()

    # Wait a bit so the sound doesn't get cut off immediately
    time.sleep(3)

def main():
    pygame.mixer.init()

    repeat = 0
    while True:
        a = input("\nWelcome to our Pomodoro!\nType 'y' to start: ")
        if a.lower() == 'y':
            repeat += 1
            print(f"\n🍅 Pomodoro #{repeat} started (25 mins)")
            timer(1500)  # 25 minutes
            play_sound(0)

            if repeat == 4:
                print("\n🛌 Long break (15 mins)")
                timer(900)  # 15 minutes
                play_sound(3)
                repeat = 0  # Reset cycle
            else:
                print("\n☕ Short break (5 mins)")
                timer(300)  # 5 minutes
                play_sound(1)

if __name__ == '__main__':
    main()
