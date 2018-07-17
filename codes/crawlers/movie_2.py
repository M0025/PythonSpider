import requests
from bs4 import BeautifulSoup as bs
import pymysql

#链接数据库
connect = pymysql.connect(host="localhost", user='root', password="123456", db="douban", charset="utf8")
cursor = connect.cursor()

baseUrl = "https://movie.douban.com/top250?start={}&filter="

for startIndex in range(0, 226, 25):
    firstPage = requests.get(baseUrl.format(startIndex)).text
    soup = bs(firstPage, 'lxml')
    infos = soup.find_all("div", attrs={"class": "info"})
    for info in infos:
        title = info.find('span', attrs={"class": "title"}).get_text()
        div_bd = info.find("div", attrs={"class": "bd"})
        items = div_bd.find("p").get_text().strip().split("\n")
        items_1 = items[0]
        director_actor = items_1.split("\xa0\xa0\xa0")
        director = director_actor[0][4:].rstrip("...").split("/")[0]
        try:
            actor = director_actor[1][4:].rstrip("...").rstrip("/").split("/")[0]  #去掉最后的斜杠
        except IndexError as e:
            actor = None
            print(e)

        year_area_genre = items[1].strip().split("\xa0/\xa0")
        year = year_area_genre[0]
        area = year_area_genre[1]
        genre = year_area_genre[2]

        sql = "insert into top250 values ('%s','%s','%s','%s','%s','%s')" % (title, director, actor, year, area, genre)
        cursor.execute(sql)  # 影响了多少行数据
        connect.commit()