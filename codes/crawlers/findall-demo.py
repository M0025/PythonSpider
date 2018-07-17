import re
# \d匹配一个或多个数字
# 后面接长度，表示子串
pattern = re.compile(("\d+"))
pattern2 = re.compile("[\d]{2}")

result = re.findall(pattern, "one1two2three3four4")
print(result)
result2 = re.findall(pattern2, "one111two2222three323four422")
print(result2)