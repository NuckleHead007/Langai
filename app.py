# Import required libraries
import os
import openai
import streamlit as st

# Set page title
st.title('Write a Message to Your Amour')

# Add a descriptive text
st.write('Some people say that French is a good language')

# Define a function to generate text using OpenAI API
def GPT_Completion(texts):
    """
    This function takes a string as input and uses OpenAI API to generate text based on the given prompt.

    Args:
        texts: The string to be used as a prompt for OpenAI API.

    Returns:
        The generated text as a string.
    """

    # Access OpenAI API using your personal API key
    openai.api_key = "insert_your_api_key"

    # Define parameters for generating text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=texts,
        temperature=0.6,  # Controls the randomness of the generated text
        top_p=1,         # Controls how much weight is given to the most likely completions
        max_tokens=300,  # Maximum number of tokens to generate
        frequency_penalty=0,  # Penalizes the model for generating repetitive sequences
        presence_penalty=0  # Penalizes the model for generating sequences that are already present in the prompt
    )

    # Return the first completion
    return response.choices[0].text

# Create a text input field for user input
input_bar = st.text_input('What would you like to communicate to your loved one?')

# Check if user has typed anything
if input_bar:

    # Generate text using the OpenAI API based on user input
    st.text(GPT_Completion(f"Generate a vocabulary quiz for intermediate-level learners on a specific topic. The quiz should include various question types, such as matching, multiple choice, and fill in the blank, and should test learners' knowledge of both spoken and written vocabulary with their solution: {input_bar}"))
