import win32com.client
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime
import os

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def say(text):
    print(f"Assistant: {text}")
    speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    r.dynamic_energy_threshold = True  # Automatically adjusts to room noise

    with sr.Microphone() as source:
        print("\n--- Listening ---")
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except Exception:
            return "none"


if __name__ == "__main__":
    say("System online. How can I help you today?")

    while True:
        query = takeCommand()

        if query == "none":
            continue

        if "wikipedia" in query:
            say("Searching Wikipedia...")
            topic = query.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(topic, sentences=2)
                say("According to Wikipedia...")
                say(results)
            except Exception:
                say("I couldn't find a clear page for that.")

        elif "What is your name" in query or "what is your name" in query:
            say("My name is JARVIS")

        elif "ai" in query:
            say("Checking with AI...")
            try:
                answer = ask_ai(query)
                say(answer)
            except Exception as e:
                print(e)
                say("AI connection error")

        elif "open notepad" in query:
            say("Opening Notepad for you.")
            os.system("notepad.exe")

        elif "open calculator" in query:
            say("Opening Calculator.")
            os.system("calc.exe")

        elif "open command prompt" in query or "open cmd" in query:
            say("Opening Command Prompt.")
            os.system("start cmd")

        elif "open paint" in query:
            say("Opening MS Paint.")
            os.system("mspaint.exe")

        elif "open vs code" in query or "open code" in query:
            say("Opening Visual Studio Code")
            os.system("code")

        elif "open whatsapp" in query:
            say("Opening Whatsapp for you.")
            webbrowser.open("https://web.whatsapp.com/")

        elif "open powerpoint" in query:
            say("Opening PowerPoint for you.")
            os.system("powerpoint.exe")

        elif "open pycharm" in query:
            say("Opening Pycharm for you.")
            os.system("pycharm.exe")

        elif "open python" in query:
            say("Opening Python For you.")
            os.system("python.exe")

        # --- FEATURE: WEB BROWSING ---
        elif "open youtube" in query:
            say("Opening Youtube")
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            say("Opening Google")
            webbrowser.open("https://google.com")

        # 1. SHUTDOWN WITH CONFIRMATION
        elif "shutdown the system" in query:
            say("Are you sure you want to shut down the computer?")
            confirmation = takeCommand()
            if "yes" in confirmation:
                say("Shutting down in 10 seconds. Save your work.")
                os.system("shutdown /s /t 10")  # /s is shutdown, /t 10 is 10 sec timer
            else:
                say("Shutdown cancelled.")

        # 2. RESTART
        elif "restart the system" in query:
            say("Are you sure you want to restart?")
            confirmation = takeCommand()
            if "yes" in confirmation:
                say("Restarting now.")
                os.system("shutdown /r /t 0")  # /r is restart, /t 0 is immediate
            else:
                say("Restart cancelled.")

        # 3. SLEEP MODE
        elif "sleep the system" in query:
            say("Putting the system to sleep.")
            # This command triggers the Windows suspension state
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        # 4. LOG OFF
        elif "log off" in query or "sign out" in query:
            say("Logging off your user account.")
            os.system("shutdown /l")

        # --- FEATURE: TIME ---
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            say(f"The time is {strTime}")

        # --- FEATURE: EXIT ---
        elif "exit" in query or "stop" in query:
            say("Goodbye!")
            break
