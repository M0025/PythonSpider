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