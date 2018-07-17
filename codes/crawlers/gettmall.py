import requests
import re
import xlwt

#用requests爬取天猫首页

response = requests.get("http://www.tmall.com")
print(response.status_code)  #查看状态码
if response.status_code == 200:
    html = response.text
    print(html)
    # (.+?) 匹配任意字符（除了换行符）一个或多个。
    links = re.findall("<a href=\"(.+?)\">(.+?)</a>", html)

    #查看匹配结果
    print(links)
    for url, name in links:
        print("名称：{}，路径：{}".format(name, url))
        print("**************")

    #将结果写入到Excel中
    wbk = xlwt.Workbook()  # 创建工作簿
    sheet = wbk.add_sheet('天猫列表')  # 创建工作表
    for i in range(len(links[0])):  #列数
        for j in range(len(links)): #行数
            sheet.write(j, i, links[j][i])  # 第一行第二列写入testtext'
            wbk.save('./gettmall.xls')  # 保存Excel文件
    print("ok")