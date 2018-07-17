import requests
from bs4 import BeautifulSoup as bs

html = requests.get("https://www.baidu.com").text

# print(html)
soup = bs(html, "html.parser")  #html.parser/lxml/html5lib
# print(soup.prettify())
print(soup.name)
