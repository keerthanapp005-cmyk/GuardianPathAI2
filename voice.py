import pyttsx3
import time

engine = pyttsx3.init()
engine.setProperty("rate", 170)

last_message = ""
last_time = 0

REPEAT_DELAY = 3  # seconds

def speak(message):
    global last_message, last_time

    current_time = time.time()

    if message != last_message or current_time - last_time >= REPEAT_DELAY:
        print("VOICE:", message)
        engine.say(message)
        engine.runAndWait()

        last_message = message
        last_time = current_time