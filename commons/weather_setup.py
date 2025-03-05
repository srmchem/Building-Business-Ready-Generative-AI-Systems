import os
from google.colab import userdata

# Function to initialize the Weather API key
def initialize_weather_api():
    # Access the secret by its name
    Weather_Key = userdata.get('Weather_Key')
    
    if not Weather_Key:
        raise ValueError("Weather_Key is not set in userdata!")
    
    # Set the API key in the environment and OpenAI
    os.environ['Weather_Key'] = Weather_Key
    print("Weather_Key initialized successfully.")
