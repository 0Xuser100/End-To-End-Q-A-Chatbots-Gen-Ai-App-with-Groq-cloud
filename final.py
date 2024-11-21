import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set up Groq API key
groq_api_key = os.getenv("GROQ_API_KEY")

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user's queries."),
        ("user", "Question: {question}")
    ]
)

# Function to generate a response using the selected Groq model
def generate_response(question, model_name, temperature):
    try:
        # Initialize the ChatGroq model with the specified model name and API key
        model = ChatGroq(model=model_name, groq_api_key=groq_api_key, temperature=temperature)
        output_parser = StrOutputParser()
        chain = prompt | model | output_parser
        # Generate the response
        answer = chain.invoke({'question': question})
        return answer
    except Exception as e:
        # Handle potential errors gracefully
        return f"Error generating response: {str(e)}"

# Streamlit app title
st.title("Enhanced Q&A Chatbot With Groq Models")

# Sidebar for model and parameters
model_name = st.sidebar.selectbox("Select a Groq model", [
    "gemma2-9b-it",
    "mixtral-8x7b-32768",
    "llama-3.2-90b-text-preview"
])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
#max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# Main interface for user input
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

# Generate and display the response
if user_input:
    response = generate_response(user_input, model_name, temperature)
    st.write(response)
else:
    st.write("Please provide a question for the assistant.")
