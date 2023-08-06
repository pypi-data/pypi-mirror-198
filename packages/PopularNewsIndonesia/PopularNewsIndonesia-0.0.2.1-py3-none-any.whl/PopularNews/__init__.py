import requests
from bs4 import BeautifulSoup


def data_extraction():
    content = requests.get("https://detik.com/")
    soup = BeautifulSoup(content.text, "html.parser")
    top5 = soup.find("div", {"class": "box cb-mostpop"})
    titles = []
    for article in top5.find_all("article"):
        title = article.find("h3", class_="media__title").find("a").text.strip()
        titles.append(title)

    urls = []
    for article in top5.find_all("article"):
        url = article.find("h3", class_="media__title").find("a")
        urls.append(url.get("href"))

    hasil = dict()
    hasil["Titles"] = titles
    hasil["Firsturl"] = urls
    return hasil


def data_displaying(result):

    print("Berita Terpopuler!")
    for i in range(0, 5):
        print(f'{i+1}. {result["Titles"][i]}')
        print(f'Link: {result["Firsturl"][1]}')


if __name__ == "__main__":
    result = data_extraction()
    data_displaying(result)