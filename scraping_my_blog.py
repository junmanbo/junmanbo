import requests
from bs4 import BeautifulSoup


def scrape_blog_updates():
    URL = "https://junmanbo.github.io"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    articles = soup.find("section", class_="article-list").find_all("article")[:5]
    posts = []
    for article in articles:
        title = article.find("h2", class_="article-title").text.strip()
        date = article.find("time", class_="article-time--published").text.strip()
        posts.append(f"* {title} - {date}")

    return "\n".join(posts)


print(scrape_blog_updates())
