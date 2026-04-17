import speech_recognition as sr
import pyttsx3
import subprocess
import sys
import os
import platform
import time
import random
import requests
import tempfile

os.environ["PYTHONWARNINGS"] = "ignore"

SYSTEM = platform.system()

ELEVENLABS_API_KEY = ""
ELEVENLABS_VOICE_ID = "EXAVITQu4vr4xnSDxMaL"

def _find_cmd(*candidates):
    import shutil
    for c in candidates:
        bin_name = c.split()[0]
        if shutil.which(bin_name):
            return c
    return None

def _linux(*candidates):
    return {"Linux": _find_cmd(*candidates) or candidates[0], "Windows": None, "Darwin": None}

APP_COMMANDS = {
    "brave": {
        "Linux":   _find_cmd("brave", "brave-browser", "brave-browser-stable", "brave-browser-beta") or "brave",
        "Windows": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        "Darwin":  "open -a 'Brave Browser'",
    },
    "chrome": {
        "Linux":   _find_cmd("google-chrome", "google-chrome-stable", "chromium", "chromium-browser") or "google-chrome",
        "Windows": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "Darwin":  "open -a 'Google Chrome'",
    },
    "chromium": {
        "Linux":   _find_cmd("chromium", "chromium-browser") or "chromium",
        "Windows": None,
        "Darwin":  "open -a Chromium",
    },
    "firefox": {
        "Linux":   _find_cmd("firefox", "firefox-esr") or "firefox",
        "Windows": r"C:\Program Files\Mozilla Firefox\firefox.exe",
        "Darwin":  "open -a Firefox",
    },
    "code": {
        "Linux":   _find_cmd("code", "code-oss", "vscodium", "codium") or "code",
        "Windows": "code",
        "Darwin":  "open -a 'Visual Studio Code'",
    },
    "vs code": {
        "Linux":   _find_cmd("code", "code-oss", "vscodium", "codium") or "code",
        "Windows": "code",
        "Darwin":  "open -a 'Visual Studio Code'",
    },
    "vscode": {
        "Linux":   _find_cmd("code", "code-oss", "vscodium", "codium") or "code",
        "Windows": "code",
        "Darwin":  "open -a 'Visual Studio Code'",
    },
    "calculator": {
        "Linux":   _find_cmd("gnome-calculator", "kcalc", "qalculate-gtk", "mate-calc", "galculator", "xcalc") or "gnome-calculator",
        "Windows": "calc",
        "Darwin":  "open -a Calculator",
    },
    "spotify": {
        "Linux":   _find_cmd("spotify", "spotifyd") or "spotify",
        "Windows": r"C:\Users\%USERNAME%\AppData\Roaming\Spotify\Spotify.exe",
        "Darwin":  "open -a Spotify",
    },
    "discord": {
        "Linux":   _find_cmd("discord", "Discord", "vesktop", "armcord", "webcord") or "discord",
        "Windows": r"C:\Users\%USERNAME%\AppData\Local\Discord\Update.exe --processStart Discord.exe",
        "Darwin":  "open -a Discord",
    },
    "steam": {
        "Linux":   _find_cmd("steam", "steam-native", "steam-runtime") or "steam",
        "Windows": r"C:\Program Files (x86)\Steam\steam.exe",
        "Darwin":  "open -a Steam",
    },
    "vlc": {
        "Linux":   _find_cmd("vlc", "cvlc") or "vlc",
        "Windows": r"C:\Program Files\VideoLAN\VLC\vlc.exe",
        "Darwin":  "open -a VLC",
    },
    "mpv": {
        "Linux":   _find_cmd("mpv") or "mpv",
        "Windows": "mpv",
        "Darwin":  "open -a mpv",
    },
    "terminal": {
        "Linux":   _find_cmd("kitty", "alacritty", "wezterm", "foot", "gnome-terminal", "konsole", "xfce4-terminal", "tilix", "urxvt", "xterm") or "xterm",
        "Windows": "cmd",
        "Darwin":  "open -a Terminal",
    },
    "files": {
        "Linux":   _find_cmd("thunar", "nautilus", "dolphin", "nemo", "pcmanfm", "caja", "ranger") or "thunar",
        "Windows": "explorer",
        "Darwin":  "open .",
    },
    "file manager": {
        "Linux":   _find_cmd("thunar", "nautilus", "dolphin", "nemo", "pcmanfm", "caja") or "thunar",
        "Windows": "explorer",
        "Darwin":  "open .",
    },
    "text editor": {
        "Linux":   _find_cmd("gedit", "mousepad", "kate", "geany", "xed", "pluma", "leafpad", "featherpad") or "gedit",
        "Windows": "notepad",
        "Darwin":  "open -a TextEdit",
    },
    "notepad": {
        "Linux":   _find_cmd("gedit", "mousepad", "kate", "geany", "xed", "pluma", "leafpad", "featherpad") or "gedit",
        "Windows": "notepad",
        "Darwin":  "open -a TextEdit",
    },
    "gimp": {
        "Linux":   _find_cmd("gimp") or "gimp",
        "Windows": r"C:\Program Files\GIMP 2\bin\gimp-2.10.exe",
        "Darwin":  "open -a GIMP",
    },
    "inkscape": {
        "Linux":   _find_cmd("inkscape") or "inkscape",
        "Windows": r"C:\Program Files\Inkscape\bin\inkscape.exe",
        "Darwin":  "open -a Inkscape",
    },
    "obs": {
        "Linux":   _find_cmd("obs", "obs-studio") or "obs",
        "Windows": r"C:\Program Files\obs-studio\bin\64bit\obs64.exe",
        "Darwin":  "open -a OBS",
    },
    "blender": {
        "Linux":   _find_cmd("blender") or "blender",
        "Windows": r"C:\Program Files\Blender Foundation\Blender\blender.exe",
        "Darwin":  "open -a Blender",
    },
    "telegram": {
        "Linux":   _find_cmd("telegram-desktop", "Telegram") or "telegram-desktop",
        "Windows": r"C:\Users\%USERNAME%\AppData\Roaming\Telegram Desktop\Telegram.exe",
        "Darwin":  "open -a Telegram",
    },
    "libreoffice": {
        "Linux":   _find_cmd("libreoffice", "soffice") or "libreoffice",
        "Windows": r"C:\Program Files\LibreOffice\program\soffice.exe",
        "Darwin":  "open -a LibreOffice",
    },
    "word": {
        "Linux":   _find_cmd("lowriter", "libreoffice --writer") or "lowriter",
        "Windows": "winword",
        "Darwin":  "open -a 'Microsoft Word'",
    },
    "excel": {
        "Linux":   _find_cmd("localc", "libreoffice --calc") or "localc",
        "Windows": "excel",
        "Darwin":  "open -a 'Microsoft Excel'",
    },
    "powerpoint": {
        "Linux":   _find_cmd("loimpress", "libreoffice --impress") or "loimpress",
        "Windows": "powerpnt",
        "Darwin":  "open -a 'Microsoft PowerPoint'",
    },
    "postman": {
        "Linux":   _find_cmd("postman") or "postman",
        "Windows": r"C:\Users\%USERNAME%\AppData\Local\Postman\Postman.exe",
        "Darwin":  "open -a Postman",
    },
    "virtualbox": {
        "Linux":   _find_cmd("virtualbox", "VirtualBox") or "virtualbox",
        "Windows": r"C:\Program Files\Oracle\VirtualBox\VirtualBox.exe",
        "Darwin":  "open -a VirtualBox",
    },
    "thunar": {
        "Linux":   _find_cmd("thunar") or "thunar",
        "Windows": None,
        "Darwin":  None,
    },
    "dolphin": {
        "Linux":   _find_cmd("dolphin") or "dolphin",
        "Windows": None,
        "Darwin":  None,
    },
    "nautilus": {
        "Linux":   _find_cmd("nautilus") or "nautilus",
        "Windows": None,
        "Darwin":  None,
    },
}

WAKE_WORD = "hey jarvis"
ASSISTANT_NAME = "Jarvis"
conversation_history = []

_pyttsx3_engine = pyttsx3.init()
_pyttsx3_engine.setProperty("rate", 175)
_pyttsx3_engine.setProperty("volume", 1.0)

_voices = _pyttsx3_engine.getProperty("voices")
for _v in _voices:
    if "english" in _v.name.lower() or "en" in _v.id.lower():
        _pyttsx3_engine.setProperty("voice", _v.id)
        break


def _speak_pyttsx3(text: str):
    _pyttsx3_engine.say(text)
    _pyttsx3_engine.runAndWait()


def _speak_elevenlabs(text: str) -> bool:
    if not ELEVENLABS_API_KEY:
        return False
    try:
        response = requests.post(
            f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}",
            headers={
                "xi-api-key": ELEVENLABS_API_KEY,
                "Content-Type": "application/json",
            },
            json={
                "text": text,
                "model_id": "eleven_turbo_v2",
                "voice_settings": {
                    "stability": 0.4,
                    "similarity_boost": 0.85,
                    "style": 0.3,
                    "use_speaker_boost": True,
                },
            },
            timeout=10,
        )
        if response.status_code != 200:
            print(f"[ElevenLabs] Error {response.status_code}: {response.text}")
            return False
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            f.write(response.content)
            tmp_path = f.name
        if SYSTEM == "Windows":
            os.system(f'start /wait wmplayer "{tmp_path}"')
        elif SYSTEM == "Darwin":
            os.system(f'afplay "{tmp_path}"')
        else:
            os.system(f'mpg123 -q "{tmp_path}" 2>/dev/null || ffplay -nodisp -autoexit -loglevel quiet "{tmp_path}" 2>/dev/null || aplay "{tmp_path}" 2>/dev/null')
        os.unlink(tmp_path)
        return True
    except Exception as e:
        print(f"[ElevenLabs] Failed: {e}")
        return False


def speak(text: str):
    print(f"\n[Jarvis] {text}\n")
    if not _speak_elevenlabs(text):
        _speak_pyttsx3(text)


def ask_claude(user_message: str) -> str:
    conversation_history.append({"role": "user", "content": user_message})
    system_prompt = (
        "You are Jarvis, a chill, witty, and friendly AI voice assistant. "
        "You talk like a real person — casual, warm, sometimes funny, never robotic or stiff. "
        "Keep answers SHORT, 1 to 3 sentences max, because they will be spoken out loud. "
        "No bullet points, no markdown, no lists — just natural speech. "
        "If someone greets you, greet them back like a friend would. "
        "If they ask how you are, respond genuinely. "
        "If they joke, play along. If they vent, be empathetic. "
        "If they ask what you can do, casually mention you can open and close apps, "
        "tell the time and date, control volume, and chat about anything. "
        "Be real. Be human. Be Jarvis."
    )
    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={"Content-Type": "application/json"},
            json={
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 150,
                "system": system_prompt,
                "messages": conversation_history,
            },
            timeout=10,
        )
        data = response.json()
        reply = data["content"][0]["text"].strip()
        conversation_history.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        print(f"[Claude Error] {e}")
        return random.choice([
            "Ha, my brain glitched for a sec. Say that again?",
            "I zoned out for a moment. What were you saying?",
            "Oof, I blanked. Run that by me again?",
        ])


def launch_app(app_key: str):
    if app_key not in APP_COMMANDS:
        speak(f"Hmm, I don't have {app_key} set up. You can add it to the config though.")
        return
    cmd = APP_COMMANDS[app_key].get(SYSTEM)
    if not cmd:
        speak(f"I can't launch {app_key} on your OS, sorry.")
        return
    speak(random.choice([
        f"On it, opening {app_key} now.",
        f"Sure thing, launching {app_key}.",
        f"Got it, firing up {app_key}.",
        f"Yep, opening {app_key} for you.",
        f"One sec, starting {app_key}.",
    ]))
    try:
        if SYSTEM == "Darwin":
            subprocess.Popen(cmd, shell=True)
        elif SYSTEM == "Windows":
            subprocess.Popen(os.path.expandvars(cmd), shell=True)
        else:
            subprocess.Popen(cmd if isinstance(cmd, list) else cmd.split(), start_new_session=True)
    except FileNotFoundError:
        speak(f"Couldn't find {app_key}. Make sure it's installed on your system.")
    except Exception as e:
        speak(f"Something went wrong opening {app_key}.")
        print(f"[Error] {e}")


def close_app(app_key: str):
    process_names = {
        "brave":      ["brave", "brave-browser", "brave.exe"],
        "chrome":     ["chrome", "google-chrome", "chrome.exe"],
        "firefox":    ["firefox", "firefox.exe"],
        "code":       ["code", "code.exe"],
        "spotify":    ["spotify", "spotify.exe"],
        "notepad":    ["notepad", "notepad.exe", "gedit"],
        "vlc":        ["vlc", "vlc.exe"],
        "Calculator": ["gnome-calculator", "calc.exe"],
        "discord":    ["discord", "discord.exe"],
        "steam":      ["steam", "steam.exe"],
    }
    names = process_names.get(app_key)
    if not names:
        speak(f"I'm not sure how to close {app_key}.")
        return
    speak(random.choice([
        f"Closing {app_key}, give me a sec.",
        f"Sure, shutting {app_key} down.",
        f"Killing {app_key} right now.",
    ]))
    for name in names:
        if SYSTEM == "Windows":
            subprocess.run(["taskkill", "/f", "/im", name], capture_output=True)
        else:
            subprocess.run(["pkill", "-f", name], capture_output=True)


def try_app_command(text: str) -> bool:
    action = None
    app_name = ""
    if any(text.startswith(w) for w in ["open ", "launch ", "start "]):
        action = "open"
        app_name = text.replace("open ", "").replace("launch ", "").replace("start ", "").strip()
    elif any(text.startswith(w) for w in ["close ", "kill ", "quit "]):
        action = "close"
        app_name = text.replace("close ", "").replace("kill ", "").replace("quit ", "").strip()
    if not action:
        return False
    for key in APP_COMMANDS:
        if key in app_name or app_name in key:
            launch_app(key) if action == "open" else close_app(key)
            return True
    speak(f"I don't have '{app_name}' in my list. Add it to the config if you want!")
    return True


def parse_command(text: str):
    text = text.lower().strip()
    print(f"[You] {text}")

    if any(w in text for w in ["goodbye", "bye", "see you", "peace out", "stop listening", "quit jarvis"]):
        speak(random.choice([
            "Alright, catch you later!",
            "Peace out! Holler if you need me.",
            "Later! Don't forget to hydrate.",
            "See ya! I'll be here when you need me.",
        ]))
        sys.exit(0)

    if "shutdown" in text and "computer" in text:
        speak("Alright, shutting your machine down. See ya on the other side.")
        os.system("shutdown /s /t 5" if SYSTEM == "Windows" else "shutdown -h now")
        return

    if "sleep" in text or "hibernate" in text:
        speak("Putting your computer to sleep. Sweet dreams.")
        if SYSTEM == "Windows":
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif SYSTEM == "Linux":
            os.system("systemctl suspend")
        elif SYSTEM == "Darwin":
            os.system("pmset sleepnow")
        return

    if "volume up" in text or "turn it up" in text or "louder" in text:
        speak("Cranking it up!")
        if SYSTEM == "Linux":
            os.system("amixer -D pulse sset Master 10%+")
        elif SYSTEM == "Darwin":
            os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) + 10)'")
        return

    if "volume down" in text or "turn it down" in text or "quieter" in text:
        speak("Toning it down.")
        if SYSTEM == "Linux":
            os.system("amixer -D pulse sset Master 10%-")
        elif SYSTEM == "Darwin":
            os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) - 10)'")
        return

    if "what time" in text or "tell me the time" in text:
        speak(f"It's {time.strftime('%I:%M %p')} right now.")
        return

    if "what day" in text or "what's the date" in text or "today's date" in text:
        speak(f"Today's {time.strftime('%A, %B %d, %Y')}.")
        return

    if try_app_command(text):
        return

    speak(ask_claude(text))


def listen_for_wake_word(recognizer, mic) -> bool:
    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            audio = recognizer.listen(source, timeout=6, phrase_time_limit=5)
        text = recognizer.recognize_google(audio).lower()
        print(f"[Passive] {text}")
        return WAKE_WORD in text
    except (sr.WaitTimeoutError, sr.UnknownValueError):
        return False
    except sr.RequestError:
        return False


def listen_for_command(recognizer, mic) -> str:
    speak(random.choice(["Yeah?", "Sup?", "What's good?", "I'm listening.", "Go ahead."]))
    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            print("[Listening for command...]")
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=10)
        return recognizer.recognize_google(audio)
    except sr.WaitTimeoutError:
        speak("You went quiet on me. Holler when you need something.")
        return ""
    except sr.UnknownValueError:
        speak("Didn't catch that. Say it again?")
        return ""
    except sr.RequestError:
        speak("Can't reach the speech service. Check your internet.")
        return ""


def main():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 50
    recognizer.dynamic_energy_threshold = False
    recognizer.dynamic_energy_adjustment_damping = 0.15
    recognizer.pause_threshold = 1.0
    recognizer.non_speaking_duration = 0.4
    recognizer.phrase_threshold = 0.1

    mic = sr.Microphone()

    print("[Jarvis] Calibrating mic...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

    if recognizer.energy_threshold > 1000:
        recognizer.energy_threshold = 150

    print(f"[Jarvis] Mic threshold: {recognizer.energy_threshold:.0f}")

    voice_mode = "ElevenLabs (realistic)" if ELEVENLABS_API_KEY else "pyttsx3 (built-in)"
    print(f"[Jarvis] Voice engine: {voice_mode}")

    speak(random.choice([
        "Yo, Jarvis here. Say 'Hey Jarvis' whenever you need me.",
        "What's up! I'm Jarvis. Just say 'Hey Jarvis' and I got you.",
        "Hey hey, Jarvis is online. Shout 'Hey Jarvis' to wake me up.",
        "Jarvis reporting for duty. Say 'Hey Jarvis' to get started.",
    ]))

    print(f"\n[Jarvis] Waiting for: '{WAKE_WORD}'\n")

    while True:
        if listen_for_wake_word(recognizer, mic):
            command = listen_for_command(recognizer, mic)
            if command:
                parse_command(command)


if __name__ == "__main__":
    main()