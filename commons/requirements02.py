# Attempt to import google-search-results and install if it fails
try:
    from serpapi import GoogleSearch
    print("google-search-results library is already installed.")
except ImportError:
    import subprocess
    import sys
    try:
        print("google-search-results library not found. Installing it now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "google-search-results"])
        from serpapi import GoogleSearch
        print("google-search-results library installed and imported successfully.")
    except Exception as e:
        print(f"Failed to install google-search-results library. Error: {e}")