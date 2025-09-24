import os
os.environ["USE_TF"] = "0"   # Disable TensorFlow to avoid errors

import spacy
import pandas as pd
import streamlit as st
from spacy import displacy
from gtts import gTTS
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from transformers import pipeline

# Load SpaCy model
try:
    nlp = spacy.load("en_core_web_md")
except OSError:
    from spacy.cli import download
    download("en_core_web_md")
    nlp = spacy.load("en_core_web_md")

# Load HuggingFace NER pipeline (fallback, PyTorch only)
hf_ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")

# Function to extract entities using SpaCy
def extract_entities_spacy(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents], doc

# Function to extract entities using HuggingFace (fallback)
def extract_entities_hf(text):
    results = hf_ner(text)
    return [(r["word"], r["entity_group"]) for r in results]

# Function for text-to-speech
def speak_text(text, filename="output.mp3"):
    tts = gTTS(text=text, lang="en")
    tts.save(filename)
    return filename

# Function to save results as PDF
def save_pdf(entities, query, filename="entities.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    flowables = []

    flowables.append(Paragraph("Named Entity Recognition Report", styles["Heading1"]))
    flowables.append(Spacer(1, 12))
    flowables.append(Paragraph(f"Input Query: {query}", styles["Normal"]))
    flowables.append(Spacer(1, 12))

    if entities:
        data = [["Entity", "Label"]] + entities
        table = Table(data)
        flowables.append(table)
    else:
        flowables.append(Paragraph("No entities found.", styles["Normal"]))

    doc.build(flowables)
    return filename

# Streamlit App
def main():
    st.set_page_config(page_title="NER + Text-to-Speech", layout="wide")
    st.title("🔎 Universal Named Entity Recognition (NER) with Text-to-Speech")

    st.sidebar.header("📌 App Features")
    st.sidebar.markdown("""
    - Extract entities from **any text**  
    - Listen to detected entities (TTS)  
    - Visualize with SpaCy (if available)  
    - HuggingFace fallback for better accuracy  
    - Download results as PDF  
    """)

    query = st.text_area("Enter your text:", "Do you have the iPhone 15 in stock?")

    if st.button("Extract Entities"):
        if query.strip():
            # First try with SpaCy
            entities, doc = extract_entities_spacy(query)

            if not entities:
                # Fallback to HuggingFace
                entities = extract_entities_hf(query)
                doc = None
                st.info("ℹ️ SpaCy found nothing, results shown using HuggingFace model ✅")

            if entities:
                st.subheader("📌 Extracted Entities")
                df = pd.DataFrame(entities, columns=["Entity", "Label"])
                st.table(df)

                if doc:
                    html = displacy.render(doc, style="ent")
                    st.markdown(html, unsafe_allow_html=True)

                # TTS
                entity_texts = [f"{ent} ({label})" for ent, label in entities]
                speech_text = "I found the following entities: " + ", ".join(entity_texts)
                audio_file = speak_text(speech_text)
                st.audio(audio_file, format="audio/mp3")

                # PDF
                pdf_file = save_pdf(entities, query)
                with open(pdf_file, "rb") as f:
                    st.download_button("📥 Download Report as PDF", f, file_name="entities.pdf")

            else:
                st.warning("⚠️ No entities found even with fallback.")

        else:
            st.error("Please enter some text.")

if __name__ == "__main__":
