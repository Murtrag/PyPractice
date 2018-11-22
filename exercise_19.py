from bs4 import BeautifulSoup
from requests import get

web = get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture").text
soup = BeautifulSoup(web, "lxml")
main_article = soup.find("div", class_ = "article-main").get_text()
print(main_article)

#no idea how to switch next pages of this article on this crappy website...
