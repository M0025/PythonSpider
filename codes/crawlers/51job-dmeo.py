import requests
import re
import xlwt
'''
<div class="el">
    <p class="t1 ">
        <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
        <input class="checkbox" type="checkbox" name="delivery_jobid" value="103241689" jt="0" style="display:none">
        <span>
            <a target="_blank" title="Python开发工程师" href="https://jobs.51job.com/shanghai-xhq/103241689.html?s=01&amp;t=0" onmousedown="">
                Python开发工程师
            </a>
        </span>
    </p>
    <span class="t2"><a target="_blank" title="上海东篱信息科技有限公司" href="https://jobs.51job.com/all/co2437567.html">上海东篱信息科技有限公司</a></span>
    <span class="t3">上海-徐汇区</span>
    <span class="t4">0.7-1.4万/月</span>
    <span class="t5">07-17</span>
</div>
'''
for i in range(1, 3):
    url = "https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,{}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    response = requests.get(url.format(i))
    #获取网页内容 并转化gbk编码
    html = str(response.content, "gbk")   #text不行 解决乱码
# print(html)

    #匹配规则
    reg = re.compile(
    'class="t1 ">.*? <a target="_blank" title="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>'
    ,re.S)  # re.S匹配多行
    # .*? 去掉不要的信息 a标签之前，全掉，不加小括号就不会出现在结果中
    result = re.findall(reg, html)
    print("正在爬取第{}页".format(i))
    # 列表中有元组，遍历方式
    for jobName, company, place, salary, postDate in result:
        print("名称：{}，公司：{}，地址：{}，薪资：{}，发布日期：{}".format(jobName, company, place, salary, postDate))
        print("-------------------")
        wbk = xlwt.Workbook()  # 创建工作簿
        sheet = wbk.add_sheet('表01')  # 创建工作表
        sheet.write(0, 1, 'test text')  # 第一行第二列写入testtext'
        wbk.save('./test.xls')  # 保存Excel文件
        print("ok")



#找出总的页数
