import requests
import datetime
import time
import csv
from fake_useragent import UserAgent
from lxml import etree


def create_csv_header():
    with open('./data/02_data.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        # 写入第一行头信息
        writer.writerow(['类型', "爬取日期", "排名", "书名", "评论数", "推荐数", "作者", "出版时间", "出版社", "折扣价", "原价"])


def get_useragent():
    user_agent = UserAgent().random
    return user_agent


def get_data():
    user_agent = get_useragent()
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "$Cookie": "ddscreen=2; dest_area=country_id%3D9000%26province_id%3D111%26city_id%20%3D0%26district_id%3D0%26town_id%3D0; __permanent_id=20240401093807005351712344762998016; __visit_id=20240401093807023166481939861108796; __out_refer=1711935487%7C\\u0021%7Cwww.google.com%7C\\u0021%7C; sessionID=pc_bce85742cd89a8f6fdbec9870e5b4ff1fe4ecfcab4d85fc8f7c1a167caddddea; USERNUM=RnBZ3FNtowZlJX1bc5uvnQ==; login.dangdang.com=.ASPXAUTH=hHMFlg9sCVpxsBihNG9wQQctgo/aSn0+iacXrTk9xLlqw+QW8ZXv1Q==; dangdang.com=email=MmE1MmY5NGQ4ZmFiODQyNEBkZG1vYmlsZV91c2VyLmNvbQ==&nickname=&display_id=5278365386834&customerid=/2NXm1xDF/AnU598LTxMFw==&viptype=UtVwUqJj7sA=&show_name=155****0951; ddoy=email=2a52f94d8fab8424@ddmobile_user.com&nickname=&validatedflag=2&uname=&utype=1&.ALFG=off&.ALTM=1711935584723; LOGIN_TIME=1711935642313; __rpm=p_25332849.023.3.1711935652203%7Cp_25268377...1711935662553; __trace_id=20240401094211608613531696132559897",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": user_agent,
        "If-Modified-Since": "Thu, 22 Jun 2017 08:10:56 GMT",
        "If-None-Match": "f88a80a6cc3acf58cd27f6b1e764a5b7",
        "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    types = {
        "图书畅销榜": "bestsellers",
        "新书热卖榜": "newhotsales"
    }
    top_type = {
        "近24小时": "24hours-0-0-1",
        "近7日": "recent7-0-0-1",
        "近30日": "recent30-0-0-1",
        "2023年": "year-2023-0-1",
        "2022年": "year-2022-0-1",
        "2021年": "year-2021-0-1",
    }
    today = datetime.date.today().strftime("%Y-%m-%d")
    results = []
    for type_name, type_key in types.items():
        for top_name, top_key in top_type.items():
            for page in range(1, 2):
                time.sleep(1)
                url = "http://bang.dangdang.com/books/{}/01.00.00.00.00.00-{}-{}".format(type_key, top_key, page)
                response = requests.get(url=url, headers=headers)
                response.encoding = 'GBK'
                content = response.text
                html = etree.HTML(content)
                lis = html.xpath('//ul[@class="bang_list clearfix bang_list_mode"]/li')
                for li in lis:
                    result = {
                        "类型": top_name,
                        "爬取日期": today,
                        "排名": li.xpath("./div[1]/text()")[0].replace('.', ''),
                        "书名": li.xpath("./div[@class='name']/a/text()")[0],
                        "评论数": li.xpath("./div[@class='star']/a/text()")[0].replace('条评论', ''),
                        "推荐数": li.xpath("./div[@class='star']/span[@class='tuijian']/text()")[0].replace("推荐", ""),
                        "作者": li.xpath("./div[5]/a[1]/text()")[0],
                        "出版时间": li.xpath("./div[6]/span/text()")[0],
                        "出版社": li.xpath("./div[6]/a/text()")[0],
                        "折扣价": li.xpath("./div[7]/p/span[1]/text()")[0],
                        "原价": li.xpath("./div[7]/p/span[2]/text()")[0],
                    }
                    rank = li.xpath("./div[1]/text()")[0].replace('.', '')
                    name = li.xpath("./div[@class='name']/a/text()")[0]
                    comment = li.xpath("./div[@class='star']/a/text()")[0].replace('条评论', '')
                    recommend = li.xpath("./div[@class='star']/span[@class='tuijian']/text()")[0].replace("推荐", "")
                    author = li.xpath("./div[5]/a[1]/text()")[0]
                    publish_time = li.xpath("./div[6]/span/text()")[0]
                    publish = li.xpath("./div[6]/a/text()")[0]
                    discount = li.xpath("./div[7]/p/span[1]/text()")[0]
                    original = li.xpath("./div[7]/p/span[2]/text()")[0]
                    # results.append(result)
                    results.append([top_name, today, rank, name, comment, recommend, author, publish_time, publish, discount, original])
    write_csv(results)


def write_csv(data):
    with open('./data/02_data.csv', 'a+', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for _ in data:
            writer.writerow(_)


if __name__ == "__main__":
    create_csv_header()
    get_data()
