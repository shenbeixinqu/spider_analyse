import requests
import json

url = "https://fanyi.baidu.com/sug"

kw = input("enter a word:")
params = {
    "kw": kw
}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

response = requests.post(url=url, params=params, headers=headers)

# 获取json数据
dic_json = response.json()
print(dic_json)

# 将获取到的json数据存储到本地

fp = open('./output/apple.json', 'w', encoding='utf-8')
json.dump(dic_json, fp=fp, ensure_ascii=False)
