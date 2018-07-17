from bs4 import BeautifulSoup as bs

html ='''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie " class="sister" id="link1">Jaxk</a>,
<a href="http://example.com/lacie " class="sister" id="link2">Alice</a> and
<a href="http://example.com/tillie " class="sister" id="link3">Mary</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''

# 补齐缺失标签
soup = bs(html, "html.parser") #beautifulsoup对象
# print(soup.prettify())
# print(type(soup.a))   #tag 标签

# #获取标签的属性
# print(soup.a['id'])
# print(soup.a.get('id'))
# print(soup.a.get('class'))

# #获取标签内的文字
# print(soup.a.string)
# print(soup.b.string)

# .find方法只匹配第一个符合规则的标签
# .find_all 匹配所有符合规则的tag标签
# secondLink = soup.find("a", attrs={"id": "link2"})  #第一个参数：标签名, 第二个 属性值
# links = soup.find_all("a", attrs={"class": "sister"})
# print(secondLink.string)
# print(links)
# print(links[1].string)
# print(type(links))  # 列表，结果集

p = soup.find("p")
# #在p标签内查找b标签
# b = p.find("b")
# print(b)
# # 获取父标签
# xTag = p.parent
# print(xTag.name)
#获取所有父标签
for parent in p.parents:
    print(parent.name)