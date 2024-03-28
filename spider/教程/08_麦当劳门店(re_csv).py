import requests
import re
import csv
from fake_useragent import UserAgent


def create_csv_header():
    with open('./data/08_data.csv', 'a', encoding='utf-8', newline="") as f:
        # 创建写入对象
        writer = csv.writer(f)
        # 写入第一行头信息
        writer.writerow(['city', 'shop_name'])


def get_html(url):
    headers = {
        "User-Agent": UserAgent().random
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        response.encoding = "utf-8"
        return response.text
    else:
        return


def get_info(html):
    pat1 = "<span>城市</span>(.*?)</td>"
    pat2 = "<span>门店名称</span>(.*?)</td>"
    citys = re.findall(pat1, html, re.S)
    names = re.findall(pat2, html, re.S)
    citys = [city.strip() for city in citys]
    names = [name.strip() for name in names]
    infos = zip(citys, names)
    return infos


def write_csv(data):
    with open('./data/08_data.csv', 'a+', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for _ in data:
            writer.writerow(_)


if __name__ == "__main__":
    url = "https://www.mcdonalds.com.cn/index/Quality/publicinfo/deliveryinfo?page={}"
    urls = [url.format(str(i)) for i in range(1, 557)]
    create_csv_header()
    for index, url in enumerate(urls):
        html = get_html(url)
        data = get_info(html)
        write_csv(data)
        print(f'进度: {index + 1} / { len(urls) }')
