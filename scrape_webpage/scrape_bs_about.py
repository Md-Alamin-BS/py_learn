import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://brainstation-23.com/about/"

# Send a GET request to the URL
response = requests.get(url)

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
