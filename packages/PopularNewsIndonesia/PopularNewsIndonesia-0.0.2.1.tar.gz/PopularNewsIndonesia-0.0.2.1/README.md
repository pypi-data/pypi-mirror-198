# popular-news-indonesia
app to show 5 popular news in Indonesia based from detik.com (one of biggest media in Indonesia)

## HOW IT WORK?
This package will scrape from [Detik](https://www.detik.com) to get top 5 popular news in Indonesia

This package use BeautifulSoup4 and requests.

# HOW TO USE?
import PopularNews

if __name__ == "__main__":
    result = PopularNews.data_extraction()
    PopularNews.data_displaying(result)