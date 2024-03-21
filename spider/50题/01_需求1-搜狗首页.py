import requests

url = "https://www.sogou.com"
response = requests.get(url=url)
# 获取页面数据
page_text = response.text
print(page_text)
# 将获取的页面数据存储到本地
with open("output/sougou.html", 'w', encoding="utf-8") as fp:
    fp.write(page_text)