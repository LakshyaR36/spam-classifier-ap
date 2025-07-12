import streamlit as st
import pickle
import string
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from nltk.stem.porter import PorterStemmer
import string

nlp = spacy.load("en_core_web_sm")
ps = PorterStemmer()

def transform_text(text, stem=True):
    doc = nlp(text.lower())  # Lowercase and tokenize
    tokens = []

    for token in doc:
        if token.is_alpha and token.text not in STOP_WORDS and token.text not in string.punctuation:
            word = ps.stem(token.text) if stem else token.text
            tokens.append(word)

    return " ".join(tokens)
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))
st.title("Spam Classifier")
input_sms = st.text_input("Enter the message")
if st.button('predict'):
    transform_sms = transform_text(input_sms)
    vector_input = tfidf.transform([transform_sms])
    result = model.predict(vector_input)[0]
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")