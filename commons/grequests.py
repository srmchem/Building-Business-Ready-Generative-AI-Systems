import subprocess
import os

def download(directory, filename):
    # The base URL of the image files in the GitHub repository
    base_url = 'https://raw.githubusercontent.com/Denis2054/Building-Business-Ready-Generative-AI-Systems/main/'

    # Complete URL for the file
    file_url = f"{base_url}{directory}/{filename}"

    # Add the private token (hardcoded)
    private_token = "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"

    # Use curl to download the file, including an Authorization header for the private token
    try:
        # Prepare the curl command with the Authorization header
        curl_command = (
            f'curl -H "Authorization: token {private_token}" -o {filename} {file_url}'
        )

        # Execute the curl command
        subprocess.run(curl_command, check=True, shell=True)
        print(f"Downloaded '{filename}' successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to download '{filename}'. Check the URL and your internet connection.")
