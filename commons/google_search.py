from serpapi import GoogleSearch
import requests
from bs4 import BeautifulSoup

def google_search_and_summarize(serpapi_api_key, query):
    """
    Perform a Google search using SerpApi, extract the first link, fetch the content, and summarize it.
    
    Parameters:
    serpapi_api_key (str): Your SerpApi API key.
    query (str): The search query string.

    Returns:
    None: Prints the first link, the first 500 characters of extracted text, and a summary.
    """

    # Set up your parameters
    params = {
        "engine": "google",
        "q": query,
        "api_key": serpapi_api_key
    }

    # Step 1: Perform the Google Search and Extract First Link
    search = GoogleSearch(params)
    result = search.get_dict()
    organic_results = result.get("organic_results")

    if organic_results and len(organic_results) > 0:
        first_result = organic_results[0]
        first_link = first_result.get('link')
        print(f"First Link: {first_link}")

        # Step 2: Fetch the Content from the First Link
        try:
            response = requests.get(first_link)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Step 3: Extract Main Text Content
            paragraphs = soup.find_all('p')
            text_content = " ".join([p.get_text() for p in paragraphs])

            # Display the first 500 characters to avoid clutter
            print("\nExtracted Text (First 500 chars):\n", text_content[:500])

            # Step 4: Summarize the Text using a simple approach
            # Split text into sentences and get the first few
            sentences = text_content.split('. ')
            summary = ". ".join(sentences[:3]) + "."  # Take first 3 sentences
            print("\nSummary:\n", summary)

        except requests.RequestException as e:
            print(f"Failed to fetch the content from the link: {e}")
    else:
        print("No organic results found.")
