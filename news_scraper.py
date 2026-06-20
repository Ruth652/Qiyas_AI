import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.thereporterethiopia.com/"

response = requests.get(
    url,
    headers={
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

headlines = []

for article in soup.find_all("h2"):

    link = article.find("a")

    if link:

        title = link.get_text(strip=True)
        article_url = link.get("href")

        headlines.append(
            {
                "title": title,
                "url": article_url
            }
        )


print("Collected:", len(headlines))

df = pd.DataFrame(headlines)

df.to_csv(
    "ethiopian_news.csv",
    index=False
)

print(df.head())