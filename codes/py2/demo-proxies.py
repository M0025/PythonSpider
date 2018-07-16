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