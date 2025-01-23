
import streamlit as st
from translate import Translator
import speech_recognition as sr
from gtts import gTTS
import os
import pygame

# Initialize pygame for playing audio
pygame.mixer.init()

# Language codes
language_codes = {
    "Hindi": "hi",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Chinese (Simplified)": "zh",
    "Japanese": "ja",
    "Korean": "ko",
    "Russian": "ru",
    "Arabic": "ar",
}

# Streamlit app
st.title("Speech to Translated Text with Audio")

# User selects input language
input_language = st.selectbox("Select the input language:", list(language_codes.keys()))

# Button to listen to speech
if st.button("Listen to Speech"):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Listening... Please speak into the microphone.")
        audio = r.listen(source)
        
        try:
            # Recognize speech using Google Web Speech API
            input_text = r.recognize_google(audio, language=language_codes[input_language])
            st.success(f"You said: {input_text}")
            
            # Translate speech to English
            translator = Translator(to_lang="en", from_lang=language_codes[input_language])
            translation = translator.translate(input_text)
            st.success(f"Translated text in English: {translation}")

            # Convert translated text to speech
            tts = gTTS(text=translation, lang='en')
            tts.save("translation.mp3")

            # Play the translated speech using pygame
            pygame.mixer.music.load("translation.mp3")
            pygame.mixer.music.play()

            # Wait for the audio to finish
            while pygame.mixer.music.get_busy():
                continue

        except sr.UnknownValueError:
            st.error("Sorry, could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results; {e}")
        except Exception as e:
            st.error(f"Error: {e}")
