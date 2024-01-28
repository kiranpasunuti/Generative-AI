import streamlit as st
import random
from langchain.llms import GooglePalm

# Function to generate random colors
def generate_random_color():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Set background color and page style
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background: {generate_random_color()};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Set title with bold and colorful letters
st.markdown("<h1 style='text-align: center; color: #ff6600;'><strong>Kiran GPT</strong></h1>", unsafe_allow_html=True)

# Initialize GooglePalm model
api_key = "YOUR_API_KEY"
google_palm = GooglePalm(google_api_key=api_key, temperature=0.7)

# Function to generate predictions
def generate_prediction(prompt):
    # Interaction with GooglePalm
    response = google_palm.predict(prompt)
    if not response:
        return "My Owner Kiran did not train me for this content."
    return response

# Streamlit App
def main():
    # User input section
    prompt = st.text_input("You:")

    if st.button("Add Prompt"):
        response = generate_prediction(prompt)
        st.text_area("Kiran GPT:", value=response, height=150)

    if st.button("Clear"):
        st.text_input("You:", value="")
        st.text_area("Kiran GPT:", value="")

if __name__ == "__main__":
    main()
