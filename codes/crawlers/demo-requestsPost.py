# 使用requests 模块实现 HTTP post请求
import requests
payload = {"key1": "value1", "key2": "value2"}
r = requests.post("http://httpbin.org/post", data=payload)
print(r)
print("***********")
print(r.text)