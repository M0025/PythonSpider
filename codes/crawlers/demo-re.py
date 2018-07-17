import re
pattern = re.compile('hello')
'''
从开始位置开始匹配
直至没有匹配提到相应字符
'''

result = re.match('hello')
print(result.group())

result2 = re.match((pattern,'hellop cfdf'))
print(result2.group())

result5 = pattern.match("abdeedhelloofff",5)
print(result5)