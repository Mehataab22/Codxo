import time
import datetime
import os
from playsound import playsound

def play_alarm_sound(sound_file_path):
    """
    Play the alarm sound and print an alert message.

    Args:
        sound_file_path (str): The path to the alarm sound file.
    """
    try:
        playsound(sound_file_path)
        print("\n** ALARM! **\n")
    except Exception as e:
        print(f"Error playing sound: {e}")

def set_alarm():
    """
    Set the alarm time based on user input.

    Returns:
        str: The valid alarm time in HH:MM:SS format.
    """
    while True:
        alarm_time = input("Enter the alarm time (HH:MM:SS): ")
        try:
            datetime.datetime.strptime(alarm_time, "%H:%M:%S")
            return alarm_time
        except ValueError:
            print("Incorrect time format. Please use HH:MM:SS.")

def main():
    """
    Main function to execute the alarm setting and monitoring process.
    """
    alarm_time = set_alarm()
    print(f"Alarm set for {alarm_time}")

    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now == alarm_time:
            play_alarm_sound('/path/note.mp3')  # Replace with the actual sound file path
            break
        time.sleep(1)

if __name__ == "__main__":
    main()
