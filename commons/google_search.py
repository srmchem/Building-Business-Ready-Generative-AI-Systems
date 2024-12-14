from serpapi import GoogleSearch
import requests
from bs4 import BeautifulSoup

def fetch_and_summarize_content(url):
    """
    Fetches content from the given URL and summarizes it.
    
    Parameters:
    url (str): The URL to fetch content from.

    Returns:
    summary (str): The summary of the content, or None if fetching fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract main text content
        paragraphs = soup.find_all('p')
        text_content = " ".join([p.get_text() for p in paragraphs])

        # Display the first 500 characters for verification
        print("\nExtracted Text (First 500 chars):\n", text_content[:500])

        # Summarize the text using a simple approach
        sentences = text_content.split('. ')
        summary = ". ".join(sentences[:3]) + "."  # Take first 3 sentences
        return summary

    except requests.RequestException as e:
        print(f"Failed to fetch the content from the link: {e}")
        return None

def google_search_and_summarize(serpapi_api_key, query):
    """
    Perform a Google search using SerpApi, prioritize Wikipedia results(fallback), fetch readable content, and summarize it.
    
    Parameters:
    serpapi_api_key (str): Your SerpApi API key.
    query (str): The search query string.

    Returns:
    None: Prints the first valid link and the summary.
    """
    # Set up search parameters
    params = {
        "engine": "google",
        "q": query,
        "api_key": serpapi_api_key
    }

    search = GoogleSearch(params)
    result = search.get_dict()
    organic_results = result.get("organic_results", [])

    if not organic_results:
        print("No organic results found.")
        return

    # Step 1: Prioritize Wikipedia Links
    wiki_links = [r["link"] for r in organic_results if "wikipedia.org" in r.get("link", "")]
    other_links = [r["link"] for r in organic_results if "wikipedia.org" not in r.get("link", "")]

    # Combine prioritized Wikipedia links and others
    all_links = wiki_links + other_links

    # Step 2: Find the first readable link
    for link in all_links:
        print(f"Testing link: {link}")
        summary = fetch_and_summarize_content(link)
        if summary:
            print(f"\nValid Link: {link}")
            print("\nSummary:\n", summary)
            return

    print("No readable content found on the provided links.")
