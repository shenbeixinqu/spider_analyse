from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

url = "https://www.shicimingju.com/book/sanguoyanyi.html"

page = requests.get(url=url, headers=headers)
page.encoding = "UTF-8"
page_text = page.text


# 实例化BS 将页面源码加载到对象中
soup = BeautifulSoup(page_text, "lxml")

li_list = soup.select('.book-mulu > ul > li')
fp = open("./output/sanguoyanyi.txt", 'w', encoding="utf-8")

for li in li_list:
    title = li.a.string
    detail_url = 'https://www.shicimingju.com' + li.a['href']
    # 对详情页发起请求 解析章节内容
    detail_page_text = requests.get(url=detail_url, headers=headers).text
    # 解析出详情页的相关内容
    detail_soup = BeautifulSoup(detail_page_text, 'lxml')
    div_tag = detail_soup.find('div', class_="chapter_content")
    # 解析章节内容
    detail_content = div_tag.text
    print('detail_content', detail_content)
    fp.write(title + ":" + detail_content + "\n")
    print(title + ' 提取成功')
