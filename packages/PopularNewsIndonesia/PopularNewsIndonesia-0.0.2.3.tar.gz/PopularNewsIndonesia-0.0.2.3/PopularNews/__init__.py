import requests # Import requests package to send HTTP requests
from bs4 import BeautifulSoup # Import BeautifulSoup package to parse HTML

description = "This app show top 5 news in Indonesia based from detik.com"

# Create function named data_exctraction
def data_extraction():
    # Using request package to get html code and parser it with BeautifulSoup4
    content = requests.get("https://detik.com/")
    soup = BeautifulSoup(content.text, "html.parser")
    top5 = soup.find("div", {"class": "box cb-mostpop"})

    titles = [] # Create an empty list to store article titles
    for article in top5.find_all("article"):
        title = article.find("h3", class_="media__title").find("a").text.strip()
        titles.append(title)

    urls = [] # Create an empty list to store article URLs
    for article in top5.find_all("article"):
        url = article.find("h3", class_="media__title").find("a")
        urls.append(url.get("href"))

    # Create a dictionary with "titles" and "urls" lists as values, and return it
    hasil = dict()
    hasil["Titles"] = titles
    hasil["Urls"] = urls
    return hasil

# Create function named data_displaying
def data_displaying(result):
    print("Berita Terpopuler!")
    for i in range(0, 5): # Loop over the first 5 articles
        print(f'{i+1}. {result["Titles"][i]}')
        print(f'Link: {result["Urls"][1]}')

# will only execute if runs as a script
if __name__ == "__main__":
    print(description)
    result = data_extraction()
    data_displaying(result)

