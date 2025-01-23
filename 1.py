import streamlit as st
from translate import Translator

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
st.title("Language Translator to English")

 # User selects input language
input_language = st.selectbox("Select the input language:", list(language_codes.keys()))

 # Text input
input_text = st.text_area("Enter text to translate:")

if st.button("Translate"):
     if input_text:
         try:
             # Initialize translator
             translator = Translator(to_lang="en", from_lang=language_codes[input_language])
             translation = translator.translate(input_text)
             st.success(f"Translated text in English: {translation}")
         except Exception as e:
             st.error(f"Error translating text: {e}")
     else:
         st.warning("Please enter some text to translate.")

         
"""

import streamlit as st
from translate import Translator
import speech_recognition as sr

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
st.title("Speech to Translated Text")

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
        
        except sr.UnknownValueError:
            st.error("Sorry, could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results; {e}")
        except Exception as e:
            st.error(f"Error: {e}") 

"""
