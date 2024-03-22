from lxml import etree
import requests

url = "https://bj.58.com/ershoufang/"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
page_text = requests.get(url=url, headers=headers).text

# xpath 解析
tree = etree.HTML(page_text)
fp = open("./output/58.txt", 'w', encoding="utf-8")

title = tree.xpath('.//section[@class="list"]//div[@class="property-content-title"]/h3/text()')
price = tree.xpath('.//section[@class="list"]//span[@class="property-price-total-num"]/text()')

for i in range(len(title)):
    print(title[i], price[i])
    fp.write(title[i] + ',' + price[i] + '\n')
