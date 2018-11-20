from bs4 import BeautifulSoup
import requests

html = requests.get('http://www.nytimes.com').text
soup = BeautifulSoup(html,'lxml')

for article in soup.find_all("h2"):
	print(article.text)