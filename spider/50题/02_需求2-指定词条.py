import requests

url = "https://www.sogou.com/web"
kw = "gpt"
params = {
    'query': kw
}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
response = requests.get(url=url, params=params, headers=headers)

page_text = response.text
print(page_text)

with open("output/sougou_gpt.html", 'w', encoding='utf-8') as fp:
    fp.write(page_text)