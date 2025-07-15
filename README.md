# 🧠 Jarvis – Voice-Controlled AI Assistant (Python + GPT)

> Iron Man–style desktop voice assistant built with Python, GPT (LLaMA3 via Ollama), and wake-word activation.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)

---

## 🎯 Project Overview

Jarvis is a smart, voice-activated desktop assistant that:
- Listens in the background for wake words: **"Jarvis"** or **"Hey Jarvis"**
- Speaks responses using `pyttsx3`
- Executes local commands like opening apps or setting reminders
- Responds to natural language using **LLaMA3 via Ollama**
- Runs entirely on your machine — no internet dependency
- Automatically starts on system boot
- Supports hotkeys for exit and shutdown

---

## 📁 File Structure

D:\Jarvis
├── .venv\ ← Python virtual environment
├── jarvis.pyw ← Main assistant logic
├── shutdown.txt ← Signal file to trigger shutdown
├── start_listener.vbs ← Auto-start listener on boot

├── listener
│   └── wake_word_listener.py ← Wake word listener script

├── logs
│   └── jarvis_log.txt ← Logs for commands & reminders
├── README.md ← This file

---

## 🔧 Features

### 🎙 Wake Word Listener
- Constantly listens for “Jarvis” or “Hey Jarvis”
- Greets based on time: morning / afternoon / evening
- Plays a beep sound and launches Jarvis when activated

### 🤖 Jarvis Assistant
- Text-to-speech responses with `pyttsx3`
- Handles commands:
  - `What time is it?`
  - `Open YouTube`
  - `Open VS Code`
  - `Remind me in 10 minutes to [task]`
- Streams smart AI replies using **LLaMA3 via Ollama**
- Gracefully shuts down on voice command

### 🎮 Hotkeys
- `Alt + Q` → Exit Jarvis only  
- `Alt + W` → Full shutdown (Jarvis + Listener)

---

## 🚀 Setup Instructions

### 1. Clone the Project

```bash
git clone https://github.com/Parmesh55/Jarvis-Voice-Assistant.git
cd Jarvis-Voice-Assistant
```

### 2. Set Up Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

> Optional: Install `pyaudio` manually if needed:
```bash
pip install pipwin
pipwin install pyaudio
```

---

### 4. Set Up Ollama

- Download and install Ollama: https://ollama.com
- Pull the model:
```bash
ollama run llama3
```

---

### 5. Enable Auto-Start

Place a shortcut to `start_listener.vbs` into:
```bash
%AppData%\Microsoft\Windows\Start Menu\Programs\Startup
```

---

## 🧪 Usage

- Boot your PC
- Listener starts silently and says:
  _"Good morning sir. Jarvis is online and ready."_
- Say: "Jarvis" or "Hey Jarvis"
- On beep, Jarvis starts and says: "Yes sir?"
- Speak a command like:
  - "What time is it?"
  - "Open YouTube"
  - "Remind me in 5 minutes to stretch"
  - "Shutdown"

---

## 📦 Requirements

```
pyttsx3
speechrecognition
ollama
psutil
keyboard
```

> Plus:
```bash
pip install pipwin
pipwin install pyaudio
```

---

## 🧑‍💻 Author

**Parmesh**  
GitHub: [Parmesh55](https://github.com/Parmesh55)  
Project Location: `D:\Jarvis`

---

## 📝 License

MIT License

Copyright (c) 2025 Parmesh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in  
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN  
THE SOFTWARE.
