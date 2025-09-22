# Named Entity Recognition App  

This is a simple **NER (Named Entity Recognition)** web app built with **Streamlit** and **spaCy**. You can enter any text query, and the app will extract entities (like names, places, dates, etc.) from it.  

## Features  
- Extract entities from text queries  
- Built using **spaCy**  
- User-friendly **Streamlit** interface  

## Installation & Run  

Clone the repository:  
git clone https://github.com/SA12352/ner-app.git  
cd ner-app  

Install dependencies:  
pip install -r requirements.txt  

Run the Streamlit app:  
streamlit run app.py  

Now open the app in your browser at:  
http://localhost:8501  

## Example  

**Input:** Barack Obama was born in Hawaii and became the 44th President of the USA.  

**Output:**  
- Barack Obama → PERSON  
- Hawaii → GPE  
- 44th → ORDINAL  
- USA → GPE  

---

⚡ Made with ❤️ using **Python, spaCy, and Streamlit**

