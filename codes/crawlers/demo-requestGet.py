# 使用requests发送http get 请求
import requests
r = requests.get("http://yangrong.blog.51cto.com/6945369/1339593")
print(r)
print(r.status_code)
print(r.reason)
print(r.cookies)
print(r.headers)
print(r.encoding)
print(r.text)
print("***********************")
r = requests.get("http://www.tmall.com")
print(r.encoding)
print(r.headers)
print(r.content)