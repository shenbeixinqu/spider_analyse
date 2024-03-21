import requests
import json

url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"

word = input("请输入地区: ")

data = {
    "cname": word,
    "pid": "",
    "pageIndex": "1",
    "pageSize": "10"
}

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

kfc_text = requests.post(url=url, headers=headers, params=data).json()
print(kfc_text)

# 持久化存储
fileName = word + "_KFC.json"
fp = open("./output/" + fileName, 'w', encoding="utf-8")
json.dump(kfc_text, fp=fp, ensure_ascii=False)

print('over')