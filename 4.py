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

# Streamlit app - Set background color
st.markdown(
    """
    <style>
    body {
        background-color: white;
    }
    .emoji-bubble {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 30px;
        background-color: #f0f0f0;
        margin-right: 15px;  /* Increased margin between emoji and text */
    }
    .chat-bubble {
        display: flex;
        align-items: center;
        margin-bottom: 20px;  /* Adding space between chat bubbles */
    }
    .left-bubble {
        background-color: #FEF538;
        padding: 10px;
        border-radius: 10px;
        color: black;
        width: fit-content;
        margin-left: -2px;  /* Adjusted margin for equal spacing */
    }
    .right-bubble {
        background-color: #00002E;
        padding: 10px;
        border-radius: 10px;
        color: white;
        width: fit-content;
        margin-right: 10px;
        margin-left: 10px;  /* Reduce space between text and robot */
    }
    .right-container {
        display: flex;
        align-items: center;
        justify-content: flex-end;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Function to display chat history
def display_chat():
    for chat in st.session_state['chat_history']:
        if chat['user']:
            # Left-aligned "You said" (input text) bubble with a separate emoji bubble
            st.markdown(f"""
                <div class='chat-bubble'>
                    <div class='emoji-bubble'>👨🏾</div>
                    <div class='left-bubble'>{chat['text']}</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            # Right-aligned translated text bubble with the robot emoji separated and placed on the right
            st.markdown(f"""
                <div class='right-container'>
                    <div class='right-bubble'>
                        Translated text in {chat['language']}: {chat['text']}
                    </div>
                    <div class='emoji-bubble'>🤖</div>
                </div>
            """, unsafe_allow_html=True)

# Streamlit title with logo
col1, col2 = st.columns([1, 8])  # Adjust column sizes as needed for closer alignment
with col1:
    st.image("C:/Users/DELL/OneDrive/Desktop/Clients/C1 - Sarthak/code/assets/travellingologo.png", width=100)  # Adjust width as needed
with col2:
    st.markdown("<h1 style='margin: 0; font-size: 3rem;'>Travel-Lingo</h1>", unsafe_allow_html=True)  # Adjust font size as needed

# Create two columns to align the language dropdowns side by side
col1, col2 = st.columns(2)

# User selects input language in the first column
with col1:
    input_language = st.selectbox("Select the input language:", list(language_codes.keys()))

# User selects translated language in the second column
with col2:
    translated_language = st.selectbox("Select the translated language:", list(language_codes.keys()))

# Button to listen to speech
if st.button("Listen to Speech"):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # Create a centered column
        center_column = st.columns(1)[0]
        with center_column:
            # Display the listening GIF centered
            st.image("C:/Users/DELL/OneDrive/Desktop/Clients/C1 - Sarthak/code/assets/listening2.gif", use_column_width=80)
        
        audio = r.listen(source)

        try:
            # Recognize speech using Google Web Speech API
            input_text = r.recognize_google(audio, language=language_codes[input_language])
            st.session_state['chat_history'].append({'text': f"You said: {input_text}", 'user': True})

            # Translate speech to the selected language
            translator = Translator(to_lang=language_codes[translated_language], from_lang=language_codes[input_language])
            translation = translator.translate(input_text)
            st.session_state['chat_history'].append({'text': translation, 'user': False, 'language': translated_language})

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

# Display chat history
display_chat()
