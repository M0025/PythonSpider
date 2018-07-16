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