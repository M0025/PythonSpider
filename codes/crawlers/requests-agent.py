import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
#设置代理IP
proxies = {"http":"122.72.32.73:80",
           "https":"58.67.159.50:80"}
response = requests.get("http://www.tmal.com",
                        headers=headers,
                        proxies=proxies)

print(response.status_code)
print(response.text)
print(response.content)