# Import libraries
import openai
import os
from google.colab import userdata

# Function to initialize the Pinecone API key
def initialize_pinecone_api():
    # Access the secret by its name
    API_KEY = userdata.get('PINECONE_API_KEY')
    
    if not API_KEY:
        raise ValueError("PINECONE_API_KEY is not set in userdata!")
    
    # Set the API key in the environment and OpenAI
    os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
    openai.api_key = os.getenv("PINECONE_API_KEY")
    print("PINECONE_API_KEY initialized successfully.")
