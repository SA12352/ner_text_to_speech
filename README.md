# ner_text_to_speech
A Streamlit app that extracts named entities from customer queries using SpaCy and speaks the results using gTTS.
🔎 Named Entity Recognition (NER) with Text-to-Speech

This project extracts key entities (like Person, Location, Date, Organization) from customer queries using SpaCy and also speaks the results aloud using gTTS (Google Text-to-Speech).

📌 Features

Extracts entities from text (Person, Place, Date, etc.)

Displays entities in a table format

Highlights entities inside the sentence

Converts the extracted entities into speech (audio output)

Simple Streamlit-based web app

🛠️ Technologies Used

Python

Streamlit

SpaCy

gTTS

Pandas

⚡ Installation & Setup

Clone this repository:

git clone https://github.com/SA12352/ner_text_to_speech.git
cd ner_text_to_speech


Create virtual environment (optional but recommended):

python -m venv venv
venv\Scripts\activate   # For Windows
source venv/bin/activate  # For Mac/Linux


Install dependencies:

pip install -r requirements.txt


Download SpaCy English model:

python -m spacy download en_core_web_sm


Run the Streamlit app:

streamlit run app.py

🖥️ Usage Example

Input:

I want to meet Dr. Sarah in Islamabad next week.


Output:

Entity	Label
Sarah	PERSON
Islamabad	GPE
next week	DATE

The app will also speak:

I found the following entities: Sarah (Person), Islamabad (Location), next week (Date)

📜 License

This project is licensed under the MIT License – feel free to use and modify.
