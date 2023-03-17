import speech_recognition as sr
import os

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def speak_text_cmd(cmd):
    # Import the required module for text  
    # to speech conversion
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(cmd)


# Loop indefinitely for user to speak
while True:
    # Exception handling to handle exceptions at the runtime
    try:
        # use the microphone as source for input
        with sr.Microphone() as source:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source, duration=0.2)
            # listens for the user's input
            audio = r.listen(source)
            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()
            print(f"You said: {MyText}\n")

            # Check if the user said "exit"
            if "exit" in MyText:
                # Speak goodbye message
                speak_text_cmd("It was nice talking to you,GOODBYE!")
                # Exit the program
                break

            else:
                # Speak the text
                speak_text_cmd("You said: ")
                speak_text_cmd(MyText)
    except sr.RequestError as e:
        # API was unreachable or unresponsive
        print("API unavailable/unresponsive")
    except sr.UnknownValueError:
        # speech was unintelligible
        print("Unable to recognize speech")

