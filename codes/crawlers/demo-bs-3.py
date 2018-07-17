from bs4 import BeautifulSoup as bs

html = '<a href="http://example.com/ ">\nI linked to <i>example.com </i>\n</a>'
a = bs(html, "lxml")
print(a.prettify())  #结构优化
link = a.find("a")
print(link.string)  # 标签里还套了标签，不是可访问的字符串了
print(link.get_text())  #只获得文字，不包含标签

#区分嵌套标签的内容
#获取a中的所有内容并返回列表 stripped 切片
text = [text for text in a.stripped_strings]
# for text in a.stripped_strings:
print(text)

