import requests
from bs4 import BeautifulSoup
import json

def scrape_rohi_jokes():
    """
    Scrapes Pashto jokes from rohi.af, formats them, and saves them to a JSON file.
    """
    URL = "https://rohi.af/category/jokes"
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all articles which contain the jokes
    joke_articles = soup.select("article.post-item")
    
    scraped_jokes = []

    for article in joke_articles:
        # The joke setup is in the <a> tag inside <h2>
        setup_element = article.select_one("h2.post-title a")
        
        # The joke delivery is in the <p> tag inside the content div
        delivery_element = article.select_one("div.post-content p")

        if setup_element and delivery_element:
            setup = setup_element.get_text(strip=True)
            delivery = delivery_element.get_text(strip=True)
            
            # Basic cleaning and validation
            if setup and delivery:
                scraped_jokes.append({
                    "setup": setup,
                    "delivery": delivery
                })

    if not scraped_jokes:
        print("No jokes found. The website structure might have changed.")
        return

    # Save the jokes to a JSON file
    try:
        with open("pashto_jokes.json", "w", encoding="utf-8") as f:
            json.dump(scraped_jokes, f, ensure_ascii=False, indent=2)
        print(f"Successfully scraped {len(scraped_jokes)} jokes and saved to pashto_jokes.json")
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    scrape_rohi_jokes()