
import fuzzer   
import spacy
import newmodel
import streamlit as st
from fuzzer import fuzzy_search  # Assuming 'fuzzer' is a module and 'fuzzy_search' is a function within it

# Load spaCy model
nlp = spacy.load("en_core_web_trf")

text = ""
message = st.text_area("Type your message here:", height=100)
submit_button = st.button("Submit")

if submit_button:
    if message:
        text = message
        st.write("Message submitted successfully.")
    else:
        st.write("Please enter a message.")

    # Extract text using newmodel
    result = newmodel.extract(nlp, text)
    if result:
        for word in result:
            # Assuming "ASCII.csv" is in the same directory as the script
            temp, ind, type = fuzzy_search("Ascii.csv", word)
            st.write(f"The word {word} is found at index {ind} and the canonical name is {temp} and is in the {type} table")
    else:
        st.write("No locations found in the input text.")
