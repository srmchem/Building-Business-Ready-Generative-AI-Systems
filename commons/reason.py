import requests
from openai import OpenAI
import openai
from openai import OpenAI
# Initialize the OpenAI client
client = OpenAI()
import base64

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

def image_analysis(image_path_or_url, query_text, model="gpt-4o"):
    
    # Initialize the content list with the query text
    content = [{"type": "text", "text": query_text}]

    if image_path_or_url.startswith(("http://", "https://")):
        # It's a URL; add it to the content
        content.append({"type": "image_url", "image_url": {"url": image_path_or_url}})
    else:
        # It's a local file; read and encode the image data
        with open(image_path_or_url, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        # Create a data URL for the image
        data_url = f"data:image/png;base64,{image_data}"
        content.append({"type": "image_url", "image_url": {"url": data_url}})

    # Create the message object
    messages = [{"role": "user", "content": content}]

    # Define the parameters
    params = {
        "max_tokens": 300,
        "temperature": 0,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    }

    # Make the API call
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        **params  # Unpack the parameters dictionary
    )

    # Save the result to a file
    with open("image_text.txt", "w") as file:
        file.write(response.choices[0].message.content)
        
    # Return the response content
    return response.choices[0].message.content

# Implemented in Chapter05
def generate_image(prompt, model="dall-e-3", size="1024x1024", quality="standard", n=1):
    
    # Initialize the OpenAI client
    client = OpenAI()

    # Generate the image using the OpenAI API
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        quality=quality,
        n=n,
    )

    # Extract and return the image URL from the response
    return response.data[0].url

# Implemented in Chapter06
def ml_baseline(input, data):
    #Endpoint for the Bayes algorithm that will be implemented in Chapter 6
    if input=="":
      # Testing the endpoint in a CoT (Chain of Reasoning)
      text="The customers would like more activities during their trips especially on the ocean."
    return text

from ipywidgets import Output, VBox, Layout
import time

# Create an output widget for reasoning steps
reasoning_output = Output(layout=Layout(border="1px solid black", padding="10px", margin="10px", width="100%"))

def chain_of_thought_reasoning(initial_query):
    steps = []

    # Display the reasoning_output widget in the interface
    display(reasoning_output)

    # Step 1: Analysis of the customer database and prediction
    steps.append("Process: Performing machine learning analysis of the customer database. \n")
    with reasoning_output:
        reasoning_output.clear_output(wait=True)
        print(steps[-1])  # Print the current step
    time.sleep(2)  # Simulate processing time
    result_ml = ml_baseline("", "")
    steps.append(f"Machine learning analysis result: {result_ml}")

    # Step 2: Searching for activities that fits customer needs
    steps.append("Process: Searching for activities that fit the customer needs. \n")
    with reasoning_output:
        reasoning_output.clear_output(wait=True)
        print(steps[-1])
    time.sleep(2)
    umessage = (
        "What activities could you suggest to provide more activities and excitement in holiday trips."
        + result_ml
    )
    mrole = "system"
    mcontent = (
        "You are an assistant that explains your reasoning step by step before providing the answer. "
        "Use structured steps to break down the query."
    )
    user_role = "user"
    task_response = make_openai_api_call(umessage, mrole, mcontent, user_role)
    steps.append(f"Activity suggestions: {task_response}")

    # Step 3: Generating an image based on the ideation
    steps.append("Process: Generating an image based on the ideation. \n")
    with reasoning_output:
        reasoning_output.clear_output(wait=True)
        print(steps[-1])
    time.sleep(2)
    prompt = task_response
    image_url = generate_image(prompt)
    steps.append(f"Generated Image URL: {image_url}")
    save_path = "c_image.png"
    image_data = requests.get(image_url).content
    with open(save_path, "wb") as file:
        file.write(image_data)
    steps.append(f"Image saved as {save_path}")

    # Step 4: Providing an engaging story based on the generated image
    steps.append("Process: Providing an engaging story based on the generated image. \n")
    with reasoning_output:
        reasoning_output.clear_output(wait=True)
        print(steps[-1])
    time.sleep(2)
    query_text = "Providing an engaging story based on the generated image"
    response = image_analysis(image_url, query_text)
    steps.append(f"Story response: {response}")

    # Clear output and notify completion
    with reasoning_output:
        reasoning_output.clear_output(wait=True)
        print("All steps completed!")
    return steps

def react(initial_query):
    steps = []

    # Display the reasoning_output widget in the interface
    display(reasoning_output)

    # Step 1: Analysis of the customer database and prediction
    steps.append("Process: Performing machine learning analysis of the customer database. \n")
    with reasoning_output:
        reasoning_output.clear_output(wait=True)
        print(steps[-1])  # Print the current step
    time.sleep(2)  # Simulate processing time
    result_ml = machine_learning.ml_agent("", "")
    steps.append(f"Machine learning analysis result: {result_ml}")

    # Step 2: Searching for activities that fits customer needs
    steps.append("Process: Searching for activities that fit the customer needs. \n")
    with reasoning_output:
        reasoning_output.clear_output(wait=True)
        print(steps[-1])
    time.sleep(2)
    umessage = (
        "What activities could you suggest to provide more activities and excitement in holiday trips."
        + result_ml
    )
    mrole = "system"
    mcontent = (
        "You are an assistant that explains your reasoning step by step before providing the answer. "
        "Use structured steps to break down the query."
    )
    user_role = "user"
    task_response = make_openai_api_call(umessage, mrole, mcontent, user_role)
    steps.append(f"Activity suggestions: {task_response}")
    return steps

