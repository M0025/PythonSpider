from urllib.request import quote,unquote
import requests
import json
import math


kw = input("请输入职位名称：")
startIndex = 0
baseUrl = "https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=801&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw={}&kt=3 "


def encode_url(url,startIndex,kw):
    return quote(url.format(startIndex,kw), safe=";/?:@&=+$,", encoding="utf-8")

encoded_url = encode_url(baseUrl,0,kw)
jobs = requests.get(encoded_url).text

# jobs_dict = json.loads(jobs)["data"]["results"]

count = json.loads(jobs)["data"]["numFound"]
pagesize = 60
totalPage = int(math.ceil(count/60))
#print(totalPage)
if totalPage == 0:
    print("未搜索到相关职位信息...")
    exit()
#商品专员
print("搜索到：{}页，{}个职位信息".format(totalPage,count))

for page in range(totalPage):
    startIndex = page*60
    encoded_url = encode_url(baseUrl,startIndex,kw)
    jobs = requests.get(encoded_url).text
    jobs_dict = json.loads(jobs)["data"]["results"]
    print("=================================第{}页=================================".format(page+1))
    for job in jobs_dict:
        # print(job)
        print("工作名称：{},工作地点：{},薪资：{}".format(job["jobName"],job["company"]["name"],job["salary"]))
        print("***********************")