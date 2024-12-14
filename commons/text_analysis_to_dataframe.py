import re
import pandas as pd

def create_analysis_dataframe(response, user_content):
    """
    Creates a pandas DataFrame for text analysis results.

    Args:
        response (str): The response string from the sentiment analysis API.
        user_content (str): The original user input text.

    Returns:
        pandas.DataFrame: A DataFrame containing the analysis results.
    """
    try:
        # Use regex to extract the score from the response
        # Updated regex to handle potential variations in formatting
        match = re.search(r"Analysis score:\s*([+-]?\d+(?:\.\d+)?)", response)  
        if match:
            score_str = match.group(1).strip()  # Extract and strip any extra whitespace
            try:
                score = float(score_str)  # Convert the extracted score to float
            except ValueError:
                raise ValueError(f"Unable to convert score to float: '{score_str}'")

            # Create a dictionary to store the analysis results
            analysis_data = {
                "Text Provided": [user_content],
                "Sentiment": [response],
                "Score": [score]
            }
            # Create the DataFrame from the dictionary
            df = pd.DataFrame(analysis_data)
            return df
        else:
            raise ValueError("Analysis score not found in the response.")
    except ValueError as e:
        raise ValueError(f"Error during analysis: {e}") # Raise a more informative error