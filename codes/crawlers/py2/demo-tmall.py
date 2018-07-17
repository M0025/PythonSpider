# -*- coding: utf-8 -*-
# urllib2 结合 re（正则）提取页面信息
import urllib2

#获取html页面。
def download(url,
             headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }, num_retries=2):
    print 'Downloading:', url
    #设置请求头，模拟浏览器访问。
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        html = None
        if hasattr(e, 'reason'):
            print "We failed to reach a server....."
            print "Reason:", e.reason
        if hasattr(e, 'code'):
            print "The Server conld't fulfull the request"
            print "Error Code:", e.code
            if num_retries > 0 and 500 <= e.code < 600:
                # retry:
                return download(url, num_retries -1)
    return html
# print download("https://www.tmall.com/")



#使用正则表达式提取商品分类信息，并写到文件中

headers = {
    "host": "www.tmall.com",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Accept":"image/webp,image/apng,image/*,*/*;q=0.8",
    "accept-language":"zh-CN,zh;q=0.9"
}

html = download('https://www.tmall.com', headers=headers)
html
import re
links = re.findall("<a href=\"(.+?)\">(.+?)</a>", html)
for link in links:
    print link

with open("./data/tmallnavigator.result", 'w') as file:
    for href, category in links:
        if href.startswith("&#x2F;&#x2F;"):
            href = href.replace("&#x2F;", "/").replace("&amp;", "&")
            file.write(category+"\thttps:"+href+"\n")











