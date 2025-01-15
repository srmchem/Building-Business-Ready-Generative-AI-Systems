import requests
from IPython.display import display, Image

def chain_of_thought_reasoning(initial_query):
    steps = []

    # Step 1: Bayes analysis of the customer database
    steps.append("Step 1: Performing Bayes analysis of the customer database.")
    result_ml = machine_learning.bayes("", "")
    steps.append(f"Bayes analysis result: {result_ml}")

    # Step 2: Searching for activities that fit the customer needs
    steps.append("Step 2: Searching for activities that fit the customer needs.")
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
    task_response = openai_api.make_openai_api_call(umessage, mrole, mcontent, user_role)
    steps.append(f"Activity suggestions: {task_response}")

    # Step 3: Generating an image based on the ideation
    steps.append("Step 3: Generating an image based on the ideation.")
    prompt = task_response
    image_url = openai_api.generate_image(prompt)
    steps.append(f"Generated Image URL: {image_url}")
    # Save and display the generated image
    save_path = "c_image.png"
    image_data = requests.get(image_url).content
    with open(save_path, "wb") as file:
        file.write(image_data)
    steps.append(f"Image saved as {save_path}")
    display(Image(filename=save_path))

    # Step 4: Providing an engaging story based on the generated image
    steps.append("Step 4: Providing an engaging story based on the generated image.")
    query_text = "Providing an engaging story based on the generated image"
    response = image_analysis(image_url, query_text)
    steps.append(f"Story response: {response}")

    return steps