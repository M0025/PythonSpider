# Python网络爬虫（2）
[本文链接][1]
标签： Python 

---

## 利用正则表达式及urllib2抓取数据
最初的方式
### 1. request
通过Python向服务器发出request   请求，得到其返回的信息。
### 2. urllib 和 urllib2
### 3. get 和 post
### 4. Headers的设置
### 5. 使用代理访问页面
### 6. 异常处理

## HTML基础
超文本标记语言，标记语言，没有逻辑。
### 样式选择器（css选择器）：

 - id选择器： #id_name， 
 - 类选择器：.cls_name,
 - 标签选择器：lable，选择标签名为lable的所有元素，用逗号隔开可以选择多个
 - 全部选择：*， 选择所有的元素

## 正则表达式
### 1. 概念：
正则表达式是一个特殊的字符匹配序列，体能帮助方便检测字符串是否与某种模式匹配。
### 2. Python Re 模块
Python自带的re模块，提供正则表达式的支持。
### 3. pattern的创建
eg. pattern = re.compile('hello')

### 6. 正则表达式通常通过特殊语法来表示。
（1) ^表示字符串开始， $ 表示字符串结尾
（2） 字母和数字表示他们自身。一个正则表达式模式中的字母和数字匹配同样的字符串。
常用：
.  匹配任意字符
\  转义
[...} 字符集 匹配字符集中的内容
预定义字符集：
\d 数字:[0-9]

示例：
```python
import re
pattern = re.compile('hello')
'''
从开始位置开始匹配
直至没有匹配提到相应字符
'''

result = re.match('hello')
print(result.group())

result2 = re.match((pattern,'hellop cfdf'))
print(result2.group())

result5 = pattern.match("abdeedhelloofff",5)
print(result5)
```


```python
import re
#re.I 不区分大小写 匹配前两个单词。
pattern = re.compile("([a-z]+) ([a-z]+)", re.I)
sentence = "this is a book"
result = re.match(pattern, sentence)
print(result.groups())
```


# 结合requests 和 BeautifulSoup 爬取豆瓣电影：

```python
import requests
from bs4 import BeautifulSoup as bs
import pymysql

#链接数据库
connect = pymysql.connect(host="localhost", user='root', password="123456", db="douban", charset="utf8")
cursor = connect.cursor()

#通过观察发现每页在url上体现的变化在“start=”后面的起始数据
baseUrl = "https://movie.douban.com/top250?start={}&filter="
#获取所有电影链接地址
for startIndex in range(0, 226, 25):
    # currentUrl = baseUrl.format(startIndex) 把起始位置按25步长遍历到250条
    # print()
    # requests.get() 获取页面信息
    firstPage = requests.get(baseUrl.format(startIndex)).text
    # print(firstPage)

# 加载本地已下载的第一页数据:
# 调试阶段避免访问网络过多
# file = open("douban_186.html", encoding='utf8')  #编码报错
    # 复制浏览器代码， 建立本地html文件
# firstPage = file.read()  #获取文件
# print()
#需求： 电影名title 导演 主演 上映日期 国家 剧情 评分

#获取所有的li 通过观察网页代码，发现所需信息都存在li标签中

    soup = bs(firstPage, 'lxml')   # 用lxml解析成soup对象
    # 找li -> 找item -> 最后找到info
    infos = soup.find_all("div", attrs={"class": "info"})   #找到class为info的div
    for info in infos:  #找到每一个div
        #查找第一个 class 为 title 的 span 标签
        #找标题
        title = info.find('span', attrs={"class": "title"}).get_text()
        # print(span_title.get_text())
        # print("------------")
        # 查找class = bd 的div标签
        div_bd = info.find("div", attrs={"class":"bd"})
        # print(div_bd)
        # info_p = div_bd.find("p").get_text()
        # #print(info_p.strip()) #去空格
        # print(info_p.strip().split("\n")) #用换行符将其拆分
        # 获取p标签的内容，去除空格，并且使用换行符进行分割，将其分割成有两个元素组成的列表
        items = div_bd.find("p").get_text().strip().split("\n")
        # print(items)
        #获取导演 和主演
        items_1 = items[0]
        # print(items_1)
        director_actor = items_1.split("\xa0\xa0\xa0")  #分割为两个元素的列表 分割后可以看到特殊符号
        # print(director_actor)
        director = director_actor[0][4:].rstrip("...").split("/")[0]  #去“导演”、rstrip去“。。。”，用/分割
        # print(director)
        # 如果没有主演，会报错，令主演为空 （186坑
        try:
            actor = director_actor[1][4:].rstrip("...").rstrip("/").split("/")[0]  #去掉最后的斜杠
        except IndexError as e:
            actor = None
            print(e)
        # print(actor)
        # print("导演：{}，主演：{}".format(director, actor))
        #获取 上映日期 国家 剧情类型
        year_area_genre = items[1].strip().split("\xa0/\xa0")
        # print(year_area_genre)
        year = year_area_genre[0]
        area = year_area_genre[1]
        genre = year_area_genre[2]
        # print("上映日期：{}，国家：{}，剧情：{}".format(year, area, genre))
        #将数据写进去
        # director  actor year  area genre
        sql = "insert into top250 values ('%s','%s','%s','%s','%s','%s')" %(title, director, actor, year, area, genre)
        # print(sql)
        # 235 插不进去 获取不到title 会变成cursor ？？
        try:
            cursor.execute(sql)  # 影响了多少行数据
            connect.commit()
        except pymysql.err.ProgrammingError as e:
            connect.commit()
        print('成功添加了{}条数据'.format(cursor.rowcount))
        print("电影名：{}，导演：{}，主演{}，年代：{}， 地区：{}， 剧情：{}".format(title, director, actor, year, area, genre))
```


  [1]: https://www.zybuluo.com/M0025/note/1215744