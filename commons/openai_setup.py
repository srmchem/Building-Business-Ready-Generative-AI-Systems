# Import libraries
import openai
import os
from google.colab import userdata

# Function to initialize the OpenAI API key
def initialize_openai_api():
    # Access the secret by its name
    API_KEY = userdata.get('API_KEY')
    
    if not API_KEY:
        raise ValueError("API_KEY is not set in userdata!")
    
    # Set the API key in the environment and OpenAI
    os.environ['OPENAI_API_KEY'] = API_KEY
    openai.api_key = os.getenv("OPENAI_API_KEY")
    print("OpenAI API key initialized successfully.")

