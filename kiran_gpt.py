import streamlit as st
import random
#import streamlit as st
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
api_key = "AIzaSyA4ACANQRcchCNDXamY0Neyp9Yo_2dvK8w"
google_palm = GooglePalm(google_api_key=api_key, temperature=0.7)

# Function to generate predictions
def generate_prediction(prompt):
    # Interaction with GooglePalm
    response = google_palm.predict(prompt)
    return response

# Streamlit App
def main():
    # User input
    prompt = st.text_area("Enter your prompt:")

    # Generate button with animation
    if st.button("Generate Response", key="generate_button"):
        if prompt:
            # Generate response using GooglePalm model
            response = generate_prediction(prompt)
            
            # Display response with colorful text
            st.markdown(f"<p style='color: {generate_random_color()}; font-size: 18px;'>Generated Response:</p>", unsafe_allow_html=True)
            st.write(response)
        else:
            st.warning("Please enter a prompt before submitting.")

if __name__ == "__main__":
    main()
