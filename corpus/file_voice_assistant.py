import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return ""

if __name__ == "__main__":
    speak("Hello! I am your voice assistant.")
    while True:
        command = listen()
        if "stop" in command.lower():
            speak("Goodbye!")
            break
        elif "hello" in command.lower():
            speak("Hello! How can I assist you today?")
        elif "your name" in command.lower():
            speak("I am a simple voice assistant.")
        else:
            speak("Sorry, I can't help with that.")
