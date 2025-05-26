# pip3 install pyttsx3

import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Text you want to say
text = "Hello! I'm learning text to speech with Python."

# Say the text
engine.say(text)

# Run the speech engine
engine.runAndWait()
