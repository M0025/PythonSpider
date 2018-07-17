import re

pattern = re.compile('jack')

pattern2 = re.compile("(jack)(mary)")
result = re.match(pattern2,'jackmarysdjfioejaodsifje')
print(result)
print(result.group(0))  #所有
print(result.group(1))  #第一组
print(result.group(2))  #第二组
#匹配索引值
print(result.span())

#match精确匹配，一模一样，有什么匹配什么