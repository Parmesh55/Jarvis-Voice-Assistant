import speech_recognition as sr
import subprocess
import time
import winsound
import os
import psutil
import pyttsx3
from datetime import datetime

LOGFILE = "D:/Jarvis/logs/jarvis_log.txt"
PYTHON_EXE = r"D:\\Jarvis\\.venv\\Scripts\\pythonw.exe"
JARVIS_SCRIPT = r"D:\\Jarvis\\jarvis.pyw"
WAKE_WORDS = ["jarvis", "hey jarvis"]
SHUTDOWN_SIGNAL = "D:/Jarvis/shutdown.txt"

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {msg}\n")

def greet_once():
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    hour = datetime.now().hour
    greet = (
        "Good morning sir" if hour < 12 else
        "Good afternoon sir" if hour < 18 else
        "Good evening sir"
    )
    engine.say(greet)
    engine.say("Jarvis is online and ready")
    engine.runAndWait()
    log("Greeted once on boot")

def is_jarvis_running():
    for p in psutil.process_iter(['name', 'cmdline']):
        try:
            if (
                "pythonw.exe" in p.info.get("name", "").lower() and
                "jarvis.pyw" in " ".join(p.info.get("cmdline", [])).lower()
            ):
                return True
        except:
            continue
    return False

def listen_loop():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic)
        greet_once()
        log("Listener started")

        while True:
            if os.path.exists(SHUTDOWN_SIGNAL):
                log("Shutdown signal detected. Exiting listener.")
                os.remove(SHUTDOWN_SIGNAL)
                break

            try:
                if is_jarvis_running():
                    time.sleep(2)
                    continue
                audio = r.listen(mic, timeout=5, phrase_time_limit=4)
                said = r.recognize_google(audio).lower()
                log(f"Heard: {said}")
                if any(w in said for w in WAKE_WORDS):
                    winsound.Beep(1000, 150)
                    subprocess.Popen([PYTHON_EXE, JARVIS_SCRIPT], close_fds=True)
                    log("Jarvis launched")
                    time.sleep(5)
            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                continue
            except Exception as e:
                log(f"Recognition error: {e}")

if __name__ == "__main__":
    listen_loop()
