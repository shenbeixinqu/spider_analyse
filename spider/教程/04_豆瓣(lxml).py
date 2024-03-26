import requests
import time
from lxml import etree


def get_html(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return


def get_info(html):
    html = etree.HTML(html)
    infos = html.xpath("//tr[@class='item']")
    for info in infos:
        # 书名
        name = info.xpath('./td[2]/div[1]/a/text()')[0].strip()
        # 作者 出版社 出版时间 价格
        public_info = info.xpath('./td[2]/p[1]/text()')[0].strip()
        # 评分
        score = info.xpath('./td[2]/div[2]/span[2]/text()')[0].strip()
        # 评级人数
        comment_count = info.xpath('./td[2]/div[2]/span[3]/text()')[0].strip()

        data = {
            "书名": name,
            "出版信息": public_info,
            "评分": score,
            "评价人数": comment_count
        }
        print(data)


def main():
    urls = ["https://book.douban.com/top250?start={}".format(str(i)) for i in range(0, 226, 25)]
    for url in urls:
        html = get_html(url)
        get_info(html)
        time.sleep(1)


if __name__ == "__main__":
    main()