import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.thereporterethiopia.com/"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }
)

soup = BeautifulSoup(response.text, "html.parser")

data = []

for article in soup.find_all("h2"):
    link = article.find("a")

    if link:
        title = link.get_text(strip=True)
        href = link.get("href")

        data.append({
            "title": title,
            "url": href
        })

df = pd.DataFrame(data)

df.to_csv(
    "ethiopian_news.csv",
    index=False
)

print("saved:", len(df))