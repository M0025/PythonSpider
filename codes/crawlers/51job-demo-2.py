import re
import requests

url = "https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,{}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
#爬取第一页数据
firstPage = url.format(1)
response = requests.get(firstPage)

#处理中文编码 转化成gbk content字节码byte

html = str(response.content, "gbk")

# print(html)

#获取总页数
pattern = re.compile('<span class="td">共(.*?)页，到第</span>', re.S)
result = re.findall(pattern, html)
totalPage = int(result[0])
print("总页数：{}".format(totalPage))

for page in range(1, totalPage + 1):
    print("正在爬取第{}页数据".format(page))
    #组装当前页的页码
    currentUrl = url.format(page)
    # print(currentUrl[0:80])
    response = requests.get(currentUrl)
    html = str(response.content, "gbk")
    #匹配规则
    reg = re.compile(
    'class="t1 ">.*? <a target="_blank" title="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>'
    ,re.S)  # re.S匹配多行
    #获取一页中所有的职位信息
    onePage = re.findall(reg, html)
    # 列表中有元组，遍历方式
    for jobName, company, place, salary, postDate in onePage:
        print("名称：{}，公司：{}，地址：{}，薪资：{}，发布日期：{}".format(jobName, company, place, salary, postDate))
        print("-------------------")
