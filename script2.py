import speech_recognition as sr
import openai
import gtts
from playsound import playsound

# API key
openai.api_key = "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"

def grammar_correct(sentence):
    # Use OpenAI's Completion API to correct the grammar of the given sentence
    completions = openai.Completion.create(
        # Specify the engine to use
        engine="text-davinci-002",
        # Set the prompt for the completion API
        prompt=(f"Please correct the grammar of this sentence: {sentence}"),
        # Set the maximum number of words the completion should return
        max_tokens=1024,
        # Set the number of completions to return
        n=1,
        # Don't stop generating completions until the API returns one
        stop=None,
        # Set the temperature parameter to control the creativity of the completion
        temperature=0.5,
    )

    # Store the corrected sentence as a string in the "message" variable
    message = completions.choices[0].text
    # Return the corrected sentence
    return message


# Initialize the recognizer
r = sr.Recognizer()

# Listen to the microphone
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Convert the audio to text
voice_input = r.recognize_google(audio)

# Correct the grammar of the input
corrected_sentence = grammar_correct(voice_input)

print(f"Original sentence: {voice_input}")
print(f"Corrected sentence: {corrected_sentence}")

# Speak out the corrected sentence
tts = gtts.gTTS(corrected_sentence)
tts.save("corrected_sentence.mp3")

playsound("corrected_sentence.mp3")
