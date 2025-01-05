import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time

# Initialize the speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, the service is down.")
        return ""

# Main function for the voice assistant
def voice_assistant():
    speak("Hello! How can I assist you today?")
    while True:
        text = recognize_speech()
        
        if "hello" in text:
            speak("Hello! How can I assist you today?")
        
        elif "time" in text:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}")
        
        elif "search" in text:
            query = text.split("search")[-1].strip()
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query} on Google.")
        
        elif "remind me" in text:
            reminder = text.split("remind me")[-1].strip()
            speak(f"Reminder set for {reminder}")
            time.sleep(10)  # Example: Wait for 10 seconds
            speak(f"Reminder: {reminder}")
        
        elif "exit" in text:
            speak("Goodbye!")
            break
        
        else:
            speak("Sorry, I did not understand that command.")

# Run the voice assistant
if __name__ == "__main__":
    voice_assistant()