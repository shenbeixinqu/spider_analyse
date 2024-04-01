import requests
import csv
from lxml import etree
from fake_useragent import UserAgent


def create_csv_header():
    with open('./data/03_data.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        # 写入第一行头信息
        writer.writerow(['排名', "车系名称", "价格", "懂车系数", "日环比"])


def get_useragent():
    user_agent = UserAgent().random
    return user_agent


def get_date():
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "referer": "https://index.dongchedi.com/",
        "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": get_useragent()
    }
    cookies = {
        "ttwid": "1%7C4ugtU74YcWgJDCc1hEQgpzyuuz2c1j7iiRBM-HBIQwY%7C1687932797%7C3a2b4be3d5b4fed0b5ee5d772f6f81a3ad8dbb7995228b1b46052ccd669b7c5b",
        "Hm_lvt_3e79ab9e4da287b5752d8048743b95e6": "1687932797",
        "_ga": "GA1.2.1371508524.1687932798",
        "_ga_YB3EWSDTGF": "GS1.1.1687932797.1.0.1687932814.43.0.0",
        "tea_session": "27606ec4-f086-4c81-9191-c4ffc0a4e08e%2C1711957016835"
    }
    url = "https://index.dongchedi.com/rank"
    params = {
        "rank_type": "轿车",
        "date": "2024-03-01",
        "sub_rank_type": "全部轿车",
        "price": "全部价格"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    content = response.text
    html = etree.HTML(content)
    lis = html.xpath('//div[@class="arco-table-body"]/table/tbody/tr')
    results = []
    for li in lis:
        try:
            rank = li.xpath('./td[1]/div/span/img/@alt')[0]
        except:
            rank = li.xpath('./td[1]/div/span/p/text()')[0]
        name = li.xpath('./td[2]/div/span/div/p/a/text()')[0]
        price = li.xpath('./td[3]//p[@class="rank-table-price"]/span[1]/text()')[0]
        index = li.xpath('./td[4]//span[@class="fn-num-medium"]/text()')[0]
        radio = li.xpath('./td[5]/div/span/p/span/text()')[0]
        results.append([rank, name, price, index, radio])
    write_csv(results)


def write_csv(data):
    with open('./data/03_data.csv', 'a+', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for _ in data:
            writer.writerow(_)


if __name__ == '__main__':
    create_csv_header()
    get_date()
