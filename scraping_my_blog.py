import requests
from bs4 import BeautifulSoup


def scrape_blog_updates():
    URL = "https://junmanbo.github.io"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # 'article-list' 클래스를 가진 섹션에서 게시물 찾기
    articles = soup.find("section", class_="article-list").find_all("article")

    # 상위 5개의 게시물만 가져오기.
    for article in articles[:5]:
        title = article.find("h2", class_="article-title").text.strip()  # 제목
        link = article.find("a")["href"]  # 링크
        date = article.find("time", class_="article-time--published").text.strip()  # 날짜

        print(f"Title: {title}\nLink: {link}\nDate: {date}\n---")


# 웹 스크래핑 함수 실행
scrape_blog_updates()
