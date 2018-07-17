import requests
# r = requests.get("http://blog.51cto.com/yangrong/1339593")
#
# with open("test.html", "w", encoding="utf-8") as file:
#     file.write((r.text))

payload = {"key1": "value1", "key2": "value2"}
requests.post("http://httpbin.org", data=payload)
print()