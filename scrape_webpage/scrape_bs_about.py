import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://brainstation-23.com/about/"

# Set headers to mimic a web browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "https://www.google.com/",
    "Cache-Control": "max-age=0",
    "DNT": "1"
}

# Proxy settings (example proxy from Free Proxy List)
proxies = {
    "http": "http://27.147.155.44:58080",
    "https": "http://27.147.155.44:58080"
}

# Create a session
session = requests.Session()

# Send a GET request to the URL with headers and proxy
response = session.get(url, headers=headers, proxies=proxies)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Extract the page title
    title = soup.title.string
    print("Page Title:", title)

    # Example: Extract specific content
    # You can adjust the selector based on the content you want
    main_content = soup.find('div', class_='page-content')  # Replace with the actual class or ID
    if main_content:
        print("Main Content:")
        print(main_content.get_text(strip=True))
    else:
        print("Content not found.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
