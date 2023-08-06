import requests
from bs4 import BeautifulSoup
"""
Method = Funtion
Field/Attribute = Variable
Contructor = The method that is called the first time the object is created. Use to declare variables in this class
"""

class Scraper:
    def __init__(self, url, description):  #Constructor
        self.description = description
        self.result = None
        self.url = url

    def data_extraction(self):
        pass

    def data_displaying(self):
        pass

    def run(self):
        self.data_extraction()
        self.data_displaying()

class NewsScraper(Scraper):
    def __init__(self, url):
        super(NewsScraper, self).__init__( url, "Will Show Top 5 News In Indonesia")

    def data_extraction(self):
        content = requests.get(self.url)
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
        hasil["Urls"] = urls
        return hasil

    def data_displaying(self):
        print("Berita Terpopuler!")
        result = self.data_extraction()
        for i in range(0, 5):
            print(f'{i+1}. {result["Titles"][i]}')
            print(f'Link: {result["Urls"][1]}')

class ArticleScraper(Scraper):
    def __init__(self, url):
        super(ArticleScraper, self).__init__(url, "\nNot Yet Released!!Stay Tuned!!")

if __name__ == "__main__":
    DetikNewsScraper = NewsScraper("https://detik.com/")
    print(DetikNewsScraper.description)
    DetikNewsScraper.run()

    MediumArticleScraper = ArticleScraper("https://medium.com/")
    print(MediumArticleScraper.description)
    MediumArticleScraper.run()
