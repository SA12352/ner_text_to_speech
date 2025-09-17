# Task 2: Extracting Key Information (Named Entity Recognition)
# Requirements + Extra Feature (Text-to-Speech)

import spacy
from spacy import displacy
import pandas as pd
import streamlit as st
from gtts import gTTS
import os

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Function to extract entities
def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents], doc

# Function for text-to-speech
def speak_text(text, filename="output.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    return filename

# Streamlit App
def main():
    st.title("🔎 Named Entity Recognition (NER)")
    st.write("This app extracts key entities from customer queries and also speaks out the results.")

    # Input box
    query = st.text_area("Enter a customer query:", "Do you have the iPhone 15 in stock?")

    # Button to extract entities
    if st.button("Extract Entities"):
        if query.strip():
            entities, doc = extract_entities(query)

            if entities:
                st.subheader("📌 Extracted Entities")
                df = pd.DataFrame(entities, columns=["Entity", "Label"])
                st.table(df)

                # Visualization with displacy
                html = displacy.render(doc, style="ent")
                st.markdown(html, unsafe_allow_html=True)

                # Prepare text for speech
                entity_texts = [f"{ent} ({label})" for ent, label in entities]
                speech_text = "I found the following entities: " + ", ".join(entity_texts)

                # Generate speech
                audio_file = speak_text(speech_text)
                st.audio(audio_file, format="audio/mp3")

            else:
                st.warning("⚠️ No entities found.")
                audio_file = speak_text("No entities found in your query.")
                st.audio(audio_file, format="audio/mp3")
        else:
            st.error("Please enter a query first.")

if __name__ == "__main__":
    main()
