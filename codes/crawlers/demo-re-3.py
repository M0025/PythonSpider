import re
#re.I 不区分大小写 匹配前两个单词。
pattern = re.compile("([a-z]+) ([a-z]+)", re.I)
sentence = "this is a book"
result = re.match(pattern, sentence)
print(result.groups())