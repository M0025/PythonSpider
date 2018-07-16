# Python数据分析

[本文链接][1]
标签： Python 数据分析

---

课程内容：
1. 数据获取   爬虫
2. 数据预处理和数据清洗
3. 数据分析  numpy scipy pandas
4. 数据可视化展示

## 一、Anaconda安装和使用
为使用urllib2，需要Python2环境。使用anaconda进行虚拟环境搭建，方便切换
### 1.Anaconda是什么？
是用来管理Python所用的包和环境的软件，可以创建多个虚拟环境，使处理多个项目变得简单。
附带了conda Python和150多个科学包及其依赖

### 2.Anaconda的安装
下载后傻瓜安装即可，可选自动添加环境变量。如没添加需要自己手动添加一下五个环境变量：

**D:\ProgramingTools\Anaconda**
D:\ProgramingTools\Anaconda\Library\bin
D:\ProgramingTools\Anaconda\Library\usr
D:\ProgramingTools\Anaconda\Library\mingw-w64
**D:\ProgramingTools\Anaconda\Scripts**
加粗为必须配置，其他不配也没太太问题。

### 3.管理环境

 1. 创建环境： conda create -n env_name python=3.5  #环境名 Python版本
 2. 列出所有环境：conda info -e
 3. 进入环境：activate my_env
 4. 环境中添加所需的包：conda install package_name
 5. 环境中删除所需要的包：conda remove package_name
 6. 删除环境：conda remove -n my_env --all

## 二、Python网络编程
### 1.HTTP 简单了解
#### 1.1 HTTP请求格式

当浏览器像Web服务器发出请求时，它向服务器传递了一个**数据块**，也就是请求信息，由三部分组成：

 - 请求方法、URL（url  统一资源定位符） 、协议/版本
 - 请求头（Request Header）
 - 请求正文（发送的数据）

#### 1.2 HTTP请求方式
**get** 是比较简单的http请求，直接以键值对的形式写在请求地址后面，信息量最大4k，数据量小，没有安全性的要求
**post** 所发送的数据经过编码放到请求体中，可以传递大量数据，数据量无上限，且有一定的安全性，常用与表单提交。

#### 1.3 浏览器开发者工具
F12键，可查看请求内容、请求方式、网站源码等等内容。非常强大。


### 2. urllib和urllib2模块使用
> 这俩模块已经过时，看看就行，不必走心。构建在Python2之上的旧时牛逼模块。

#### 2.1 urllib和urllib2模块介绍
urllib和urllib2，是功能强大的网络编程函数库，通过他们来访问网络上的文件，几乎可以把任何url所指向的东西用作程序输入。
以上两个模块与re（正则表达式）结合，可以下载web页面，提取页面上的数据信息，自动生成报告。

#### 2.2 urllib和urllib2两模块间比较

 - urllib2可以接受一个request类的实例来设置URL请求的headers，这样2就可伪装UserAgent字符串（伪装浏览器）；
 - urllib提供urlencode来get查询字符串的产生；urllib有一些像urlretrieve函数及quote等一系列urllib2没有的功能.
 

#### 2.3 使用urllib2访问指定的url并获取页面内容

通过try except来捕获错误，使代码不会出错就停运。
```python
# -*- coding: utf-8 -*- 
#使用urllib2 访问指定的url并获取页面内容
import urllib
import urllib2

def down_with_retry(url, num_retries = 2):
    print 'Downloading:', url
    try:
        html = urllib2.urlopen(url).read()
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
                return down_with_retry(url, num_retries -1)
    return html

down_with_retry("http://httpstat.us/500")
```
访问的url是固定的错误代码位置。

运行结果：
>Downloading: http://httpstat.us/500
We failed to reach a server.....
Reason: Internal Server Error
The Server conld't fulfull the request
Error Code: 500
Downloading: http://httpstat.us/500
We failed to reach a server.....
Reason: Internal Server Error
The Server conld't fulfull the request
Error Code: 500
Downloading: http://httpstat.us/500
We failed to reach a server.....
Reason: Internal Server Error
The Server conld't fulfull the request
Error Code: 500
Process finished with exit code 0

#### 2.4 urllib2 结合 re（正则）提取页面信息

案例：从天猫首页获取商品分类及对应的url访问地址
第一步：下载天猫首页，查看首页内容：
```python
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
```
第二步
用F12查看页面信息，和上一步print出来的一样。
第三步
使用正则表达式提取商品分类信息，并写到文件中。
```python
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
```

#### 2.5 urllib2 使用代理IP访问页面
```python
# -*- coding: utf-8 -*-
# urllib2 使用代理ip访问页面

import urllib2
import random


def get_html(url, headers, proxies, num_retries=2):
    print 'Downloading:', url
    req = urllib2.Request(url)
    req.add_header("User-Agent", random.choice(headers['User-Agent']))

    proxy_support = urllib2.ProxyHandler({'http':random.choice(proxies)})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    try:
        html = urllib2.urlopen(req).read()
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
                return get_html(url, num_retries -1)
    return html

headers = {
    "User-Agent":["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"]
}
proxies = ["220.189.249.80:80","124.248.32.43:80"]
html = get_html("http://www.tmall.com", headers, proxies)
html
```

结果：代理ip被封了，少侠重新来过吧。

>以上没什么卵用，都是Python2的内容，以下才是会用到的（基于Python3）：

### 3. Requests模块使用
#### 3.1 Requests模块介绍
Python语言编写的基于urllib的xxxxx库，反正就是个库。比urllib好用，所以大家现在都不用urllib了。
为人类编写的库，可能就是人看起来更容易些吧。
安装就是普通方式了，那三种，这回还可以加个conda 安装方式，但是好像没有pip好用。
[Requests模块参考资料][2]

#### 3.2 Requests模块常见API使用
使用dir + help 更多了解模块，对于其他模块也适用
```python
#使用dir+help探索requests模块
import requests
help(requests)
dir(requests)
help(requests.get)
help(requests.post)
```
输出结果即为帮助文档。

使用requests发送HTTP get 请求
```python
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
```
使用requests 模块实现 HTTP post请求
```python
# 使用requests 模块实现 HTTP post请求
import requests
payload = {"key1": "value1", "key2": "value2"}
r = requests.post("http://httpbin.org/post", data=payload)
print(r)
print("***********")
print(r.text)
```

### 4. Python爬虫简介
网络爬虫： 从互联网网页中获取信息数据的程序、过程

### 5. Python三种网页内容抓取方法
#### 5.1 Python三种网页抓取方法介绍

 - 正则表达式： 使用re模块，用正则表达式取匹配想要的网页内容，性能比较好，但是要求正则表达式掌握程度高
 - BeautifulSoup模块: 纯Python编写，可以解析网页，并且提供定位内容的便携接口，性能不是很好，但是使用简单
 - lxml模块：c语言实现，性能较好，使用简单，但安装比较困难。

#### 5.2 美丽的汤（emmmmm。。。）
```python
#从html中获取需要的标签数据
from bs4 import BeautifulSoup as bs

html = '''
<!DOCTYPE html>
<html lang="zh-CN">
	<div class="pl2">
        <a href="https://movie.douban.com/subject/26647117/"  class="">
            暴裂无声 / <span style="font-size:13px;">恶人 / 寻山</span>
        </a>
        <span style="font-size: 13px; padding-left: 3px; color: #00A65F;">[可播放]</span>
        <p class="pl">2017-07-27(FIRST青年影展) / 2018-04-04(中国大陆) / 宋洋 / 姜武 / 袁文康 / 谭卓 / 王梓尘 / 安琥 / 伊天锴 / 中国大陆 / 忻钰坤 / 120分钟 / 剧情 / 犯罪 / 悬疑 / 忻钰坤 Yukun Xin / 汉语普通话</p>
            <div class="star clearfix">
                <span class="allstar40"></span>
                <span class="rating_nums">8.2</span>
                <span class="pl">(156448人评价)</span>
            </div>
    </div>
</html>
'''

soup = bs(html, 'lxml')

title = soup.find_all("title")
print(title)

Divs = soup.find_all("div")
print(Divs)

title = soup.find("span")
print(title)
```
 


  [1]: https://www.zybuluo.com/M0025/note/1214374
  [2]: http://docs.python-requests.org/zh_CN/latest/user/quickstart.html