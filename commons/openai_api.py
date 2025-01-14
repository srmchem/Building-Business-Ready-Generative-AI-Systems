from openai import OpenAI

# Implemented in Chapter01
def make_openai_api_call(input, mrole,mcontent,user_role):
    # Define parameters
    gmodel = "gpt-4o"

    # Create the messages object
    messages_obj = [
        {
            "role": mrole,
            "content": mcontent
        },
        {
            "role": user_role,
            "content": input
        }
    ]

    # Define all parameters in a dictionary
    params = {
        "temperature": 0,
        "max_tokens": 1024,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    # Initialize the OpenAI client
    client = OpenAI()

    # Make the API call
    response = client.chat.completions.create(
        model=gmodel,
        messages=messages_obj,
        **params  # Unpack the parameters dictionary
    )

    # Return the response
    return response.choices[0].message.content

# Implemented in Chapter05
def image_analysis(image_url, query_text, model="gpt-4o"):
    """
    Function to analyze an image using OpenAI API.
    
    Args:
        image_url (str): The URL of the image to analyze.
        query_text (str): The text-based query related to the image.
        model (str): The OpenAI model to use for the analysis. Defaults to "gpt-4o".
    
    Returns:
        str: The response from the OpenAI API regarding the image analysis.
    """
    # Define the messages object
    messages_obj = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query_text},
                {
                    "type": "image_url",
                    "image_url": {"url": image_url},
                },
            ],
        }
    ]

    # Define the parameters
    params = {
        "max_tokens": 300,
        "temperature": 0,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    }

    # Initialize the OpenAI client
    client = OpenAI()

    # Make the API call
    response = client.chat.completions.create(
        model=model,
        messages=messages_obj,
        **params  # Unpack the parameters dictionary
    )

    # Return the response
    return response.choices[0].message.content