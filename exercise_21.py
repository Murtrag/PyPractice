from bs4 import BeautifulSoup
import requests

html = requests.get('http://www.nytimes.com').text
soup = BeautifulSoup(html,'lxml')
file_name = input("type a file name(without extension): ")

resp = ""
for article in soup.find_all("h2"):
	resp+=article.text
	resp+="\n"
print(resp, file=open(file_name+".txt",'w'))