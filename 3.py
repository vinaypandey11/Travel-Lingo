
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
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Sanskrit": "sa",
    "Malayalam": "ml",
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
st.title("Travel-Lingo")

# User selects input language
input_language = st.selectbox("Select the input language:", list(language_codes.keys()))

# User selects translated language
translated_language = st.selectbox("Select the translated language:", list(language_codes.keys()))

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
            
            # Translate speech to the selected language
            translator = Translator(to_lang=language_codes[translated_language], from_lang=language_codes[input_language])
            translation = translator.translate(input_text)
            st.success(f"Translated text in {translated_language}: {translation}")

            # Convert translated text to speech
            tts = gTTS(text=translation, lang=language_codes[translated_language])
            mp3_filename = "translation.mp3"
            tts.save(mp3_filename)

            # Play the translated speech using pygame
            pygame.mixer.music.load(mp3_filename)
            pygame.mixer.music.play()

            # Wait for the audio to finish
            while pygame.mixer.music.get_busy():
                continue

            # Clean up the mp3 file after playback
            pygame.mixer.quit()
            os.remove(mp3_filename)

        except sr.UnknownValueError:
            st.error("Sorry, could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results; {e}")
        except Exception as e:
            st.error(f"Error: {e}")


#mobile access: http://192.168.202.160:8501
#streamlit run "C:\Users\DELL\OneDrive\Desktop\Clients\C1 - Sarthak\code\3.py" --server.address=0.0.0.0 --server.port=8501
#>> 