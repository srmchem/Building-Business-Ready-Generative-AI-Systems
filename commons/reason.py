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
    gmodel = "gpt-4o" #model defined in this file in /commons to make a global change to all the notebooks in the repo when there is an OpenAI update

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

# Implemented in Chapter06
def make_openai_o1_call(user_text, mrole,mcontent,user_role):
  system_prompt=mrole
  client = OpenAI()
  response = client.chat.completions.create(
      model="o1",  # or your preferred model
      messages=[
          {"role": "system", "content": system_prompt},
          {"role": "user", "content": user_text}
      ],
  )
  return response

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



# Import the function from custom machine learning file
import os
import machine_learning
from machine_learning import ml_agent

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
    #result_ml = ml_baseline("", "")
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


# Import the function from custom machine learning file
import os
import machine_learning
from machine_learning import ml_agent

def react(initial_query):
    steps = []

    # Display the reasoning_output widget in the interface
    display(reasoning_output)

    # Step 1: Analysis of the customer database and prediction
    steps.append("Process: Analysis of the customer database. \n")
    with reasoning_output:
        reasoning_output.clear_output(wait=True)
        print(steps[-1])  # Print the current step
    time.sleep(2)  # Simulate processing time
    #result_ml = ml_baseline("", "")
    result_ml = machine_learning.ml_agent("", "")
    steps.append(f"Machine learning analysis result: {result_ml}")

    # Step 2: Extracting memory tags
    steps.append("Process: Searching for activities that fit the customer needs. \n")
    with reasoning_output:
        reasoning_output.clear_output(wait=True)
        print(steps[-1])
    time.sleep(2)
    um="""First clearly delineate each memory type in the following text that begins with a memory tag. 
Short-term memory tag that holds information temporarily for immediate tasks. 
Long-term memory tag that stores information over extended periods. 
Semantic memory tag that involves general world knowledge, such as facts and concepts. 
Episodic memory tag that pertains to personal experiences and specific events. 
Reality memory tag that relates to actual events that have occurred. 
Fiction memory tag that concerns imagined or dreamed events. 
Time memory tag that involves the temporal context of memories, such as past, present, or future. 
Then provide the list of memory tags in the text. Do not provide a single word of the text. Just the memory tags found in the text as a plain list.""" + result_ml

    umessage =um    
    mrole = "system"
    mcontent = (
        "You are a psychologist who extracts memory tags from a text and who only provides the list of memory types. "
        "Use your ability to be concise and provide the tags."
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
    prompt = "Create a picture of a vacation based on the memory tags extracted from this review " + result_ml+  " make a very realistic picture taken from a smartphone based on the memory tags with these memory tags: " + task_response
    image_url = generate_image(prompt)
    steps.append(f"Generated Image URL: {image_url}")
    save_path = "c_image.png"
    image_data = requests.get(image_url).content
    with open(save_path, "wb") as file:
        file.write(image_data)
    steps.append(f"Image saved as {save_path}")

    # Step 4: Providing an engaging story based on the generated image
    steps.append("Process: Provide a travel agency engaging short paragraph describing the trip a customer could make. Don't use markdown or bullet points. Just write a short summary to introduce the trip \n")
    with reasoning_output:
        reasoning_output.clear_output(wait=True)
        print(steps[-1])
    time.sleep(2)
    query_text = "Providing an engaging presentation of a trip based on the generated image"
    response = image_analysis(image_url, query_text)
    steps.append(f"Story response: {response}")

    # Clear output and notify completion
    with reasoning_output:
        reasoning_output.clear_output(wait=True)
        print("All steps completed!")
    return steps
