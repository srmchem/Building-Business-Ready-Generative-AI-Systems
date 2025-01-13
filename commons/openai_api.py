from openai import OpenAI
import json
from IPython.display import Markdown, display

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


def summarize_conversation(file_path):
    """
    Reads a conversation history JSON file, formats it, and generates a detailed
    summary with a list of actions from the JSON text. The summary is displayed in Markdown.

    Parameters:
        file_path (str): Path to the JSON file containing conversation history.

    Returns:
        None: The summary is displayed as Markdown output.
    """
    # Step 1: Read the conversation history from the JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        dialog = file.read()
    conversation_history_json = json.loads(dialog)

    # Step 2: Construct dialog string from the JSON conversation history
    def construct_dialog(conversation_history_json):
        dialog = ""
        for user, messages in conversation_history_json.items():
            dialog += f"\n{user}:\n"
            for message in messages:
                role = message["role"]
                content = message["content"]
                dialog += f"- {role}: {content}\n"
        return dialog

    formatted_dialog = construct_dialog(conversation_history_json)

    # Step 3: Prepare the task for the summary
    mrole = "system"
    mcontent = "Your task is to read this JSON formatted text and summarize it."
    user_role = "user"
    task = f"Read this JSON formatted text and make a very detailed summary of it with a list of actions:\n{formatted_dialog}"

    # Step 4: Call the `make_openai_api_call` function
    task_response = make_openai_api_call(task, mrole, mcontent, user_role)

    # Step 5: Display the task response as Markdown
    display(Markdown(task_response))
