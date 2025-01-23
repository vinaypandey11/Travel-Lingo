# Travel-Lingo: Multilingual Speech Translator 🌍

Travel-Lingo is an intuitive, real-time speech translation application designed to break language barriers. Built with a user-friendly interface and powerful speech recognition and translation features, this application helps users communicate seamlessly across multiple languages. Whether you're traveling to a foreign country or interacting with someone who speaks a different language, Travel-Lingo is here to bridge the gap!

---

## 📖 Project Description

**Travel-Lingo** is a speech-based language translation app that listens to your speech in one language, translates it into another, and plays the translated audio. It incorporates cutting-edge technologies in speech recognition and natural language processing to deliver accurate translations.

The idea behind **Travel-Lingo** is inspired by the increasing globalization and diversity of languages spoken worldwide. Language barriers can often hinder communication in various fields such as tourism, business, and education. This project aims to solve this problem by providing a reliable, real-time translator that supports multiple languages.

With **Travel-Lingo**, users can:
1. Speak in their native language.
2. Get the speech recognized, translated, and played in the desired language.
3. Enhance accessibility and improve communication efficiency, no matter the context.

---

## 🚀 Features

- **Speech Recognition**: Converts spoken input into text using Google Web Speech API.
- **Language Translation**: Translates the recognized speech into the desired language using `translate` Python library.
- **Text-to-Speech Conversion**: Outputs the translated text as audio using Google Text-to-Speech (`gTTS`).
- **Real-Time Feedback**: Provides feedback with visual animations while listening and speaking.
- **User-Friendly Interface**: Modern and responsive UI built with Streamlit.

---

## 🛠️ Technologies Used

- **Streamlit**: For creating the web application interface.
- **Google Text-to-Speech (gTTS)**: For converting translated text into speech.
- **SpeechRecognition**: For capturing and recognizing speech input.
- **Python**: Core programming language for the project.
- **Pygame**: For playing the generated audio files.

---

## 📂 Directory Structure

```
Travel-Lingo/
├── assets/                       # Contains logo and animation files
│   ├── travellingologo.png       # Application logo
│   ├── listening.gif             # Listening animation
│   ├── speaking.gif              # Speaking animation
├── app.py                        # Main Streamlit application file
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
```

---

## 🔧 Installation and Setup

Follow these steps to set up and run the Travel-Lingo project on your local machine:

### Prerequisites
- Python 3.7 or higher
- Internet connection (required for API-based features)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/vinaypandey11/travel-lingo.git
cd travel-lingo
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate       # On macOS/Linux
venv\Scripts\activate          # On Windows
```

### 3️⃣ Install Dependencies
Install the required libraries by running:
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application
Start the Streamlit application with the following command:
```bash
streamlit run app.py
```

### 5️⃣ Access the Application
Open your browser and navigate to:
```
http://localhost:8501
```

---

## 🌐 Usage Instructions

1. Launch the application using the steps above.
2. Select the **Input Language** from the dropdown menu.
3. Choose the **Translated Language**.
4. Click the **Listen to Speech** button and speak into your microphone.
5. Wait for the application to:
   - Recognize your speech
   - Translate it into the selected language
   - Play the translated speech output
6. The translated text will also appear on the screen for reference.

---

## 🌎 Supported Languages
The application currently supports the following languages:
- English, Hindi, Marathi, Gujarati, Sanskrit, Malayalam
- Spanish, French, German, Italian, Portuguese
- Chinese (Simplified), Japanese, Korean, Russian, Arabic

---

## 🧬 Idea and Vision

**Travel-Lingo** was designed to make travel, education, and intercultural communication more accessible. Its goal is to:
- Assist tourists in navigating foreign countries.
- Help people overcome language barriers during everyday conversations.
- Enable better communication in professional settings, such as business meetings or conferences.
- Enhance accessibility for individuals who may have limited knowledge of certain languages.

By leveraging modern natural language processing techniques, Travel-Lingo aims to foster inclusivity and make the world a more connected place.

---

## 🛡️ Known Issues and Limitations
- Requires an active internet connection for speech recognition and translation APIs.
- Performance depends on the accuracy of the `SpeechRecognition` library and Google Translate API.
- Complex sentences or idiomatic phrases may not translate perfectly.

---

## 🔍 Contributing

We welcome contributions to improve this project! Here's how you can contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

---

## 📧 Contact

Feel free to reach out if you have any questions or suggestions!
- **Email**: vinaypandey11122002@gmail.com
- **GitHub**: [vinaypandey11](https://github.com/vinaypandey11)

---

Happy translating with **Travel-Lingo**! 🌟


## Snapsots:
![1_page-0001](https://github.com/user-attachments/assets/1b45e2d8-4ee4-4bd3-9664-3ad17fac09dd)
![2_page-0001](https://github.com/user-attachments/assets/41a4a4f5-f1ef-4f44-b395-227853308e42)
