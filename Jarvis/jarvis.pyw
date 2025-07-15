import speech_recognition as sr
import datetime
import threading
import time
import re
import os
import webbrowser
import ollama
import pyttsx3
import keyboard

reminders = []
exit_flag = False
SHUTDOWN_SIGNAL = "D:/Jarvis/shutdown.txt"

engine = pyttsx3.init()
engine.setProperty("rate", 180)

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def log(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("D:/Jarvis/logs/jarvis_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {msg}\n")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic)
        try:
            audio = r.listen(mic, timeout=5, phrase_time_limit=5)
            text = r.recognize_google(audio, language='en-in').lower()
            log(f"Command: {text}")
            return text
        except:
            return ""

def parse_reminder(cmd):
    match = re.search(r"remind me in (\d+) (second|seconds|minute|minutes|hour|hours) to (.+)", cmd)
    if match:
        amount = int(match.group(1))
        unit = match.group(2)
        task = match.group(3).strip()
        if "second" in unit:
            delta = datetime.timedelta(seconds=amount)
        elif "minute" in unit:
            delta = datetime.timedelta(minutes=amount)
        elif "hour" in unit:
            delta = datetime.timedelta(hours=amount)
        else:
            return None, None, None, None
        reminder_time = datetime.datetime.now() + delta
        return task, reminder_time, amount, unit
    return None, None, None, None

def reminder_loop():
    while True:
        now = datetime.datetime.now()
        for r in reminders[:]:
            if now >= r['time']:
                speak(f"Reminder: {r['task']}")
                reminders.remove(r)
        time.sleep(2)

def shutdown_everything():
    try:
        with open(SHUTDOWN_SIGNAL, "w") as f:
            f.write("shutdown")
        log("Shutdown signal created")
    except:
        pass

def handle_exit():
    global exit_flag
    speak("Goodbye sir.")
    exit_flag = True

def handle_shutdown():
    global exit_flag
    speak("Shutting down completely.")
    shutdown_everything()
    exit_flag = True

def register_hotkeys():
    keyboard.add_hotkey('alt+q', handle_exit)
    keyboard.add_hotkey('alt+w', handle_shutdown)

# Start background threads
threading.Thread(target=reminder_loop, daemon=True).start()
register_hotkeys()

speak("Hello sir, I am Jarvis and ready.")

while not exit_flag:
    cmd = take_command()
    if not cmd:
        continue

    if any(exit_word in cmd for exit_word in ["exit", "close", "offline"]):
        speak("Goodbye sir.")
        break

    elif "shutdown" in cmd:
        speak("Shutting down completely.")
        shutdown_everything()
        break

    elif "time" in cmd:
        now_time = datetime.datetime.now().strftime('%H:%M:%S')
        speak(f"It is {now_time}")

    elif "wikipedia" in cmd:
        speak("Sorry, Wikipedia support is off for now.")

    elif "jarvis" in cmd:
        speak("I am online Sir!")

    elif "youtube" in cmd:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif any(kw in cmd for kw in ["vs code", "open code"]):
        try:
            os.startfile(r"C:\\Users\\acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            speak("Opening Visual Studio Code")
        except:
            speak("Couldn't open VS Code")

    elif "remind me" in cmd:
        task, reminder_time, amount, unit = parse_reminder(cmd)
        if task and reminder_time:
            reminders.append({'task': task, 'time': reminder_time})
            speak(f"Reminder set in {amount} {unit} to {task}")
            log(f"Reminder added: {task} at {reminder_time}")
        else:
            speak("Sorry, I did not understand the reminder.")

    else:
        try:
            speak("Thinking...")
            response = ollama.chat(
                model="llama3",
                messages=[
                    {
                        "role": "system",
                        "content": "You are Jarvis, an AI assistant. Answer concisely and clearly."
                    },
                    {
                        "role": "user",
                        "content": cmd
                    }
                ],
                stream=True
            )
            partial = ""
            for chunk in response:
                delta = chunk['message']['content']
                partial += delta
                if any(p in delta for p in [".", "?", "!"]) or len(partial) > 150:
                    speak(partial.strip())
                    partial = ""
            if partial:
                speak(partial.strip())
        except Exception as e:
            speak("Sorry, I had an error talking to my AI.")
            log(f"Ollama error: {str(e)}")
