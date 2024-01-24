import streamlit as st
from langchain.llms import GooglePalm

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
    st.title("Kiran GPT")

    # User input
    prompt = st.text_area("Enter your prompt:")

    # Generate button
    if st.button("Generate Response"):
        if prompt:
            # Generate response using GooglePalm model
            response = generate_prediction(prompt)
            
            # Display response
            st.text("Generated Response:")
            st.write(response)
        else:
            st.warning("Please enter a prompt before submitting.")

if __name__ == "__main__":
    main()
