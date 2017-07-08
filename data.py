from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.twitch.tv/directory/all"
page = urlopen(url)
soup = BeautifulSoup(page)

html = soup.prettify("utf-8")
print(html)
