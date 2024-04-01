import requests
import csv
from fake_useragent import UserAgent
from lxml import etree


def create_csv_header():
    with open('./data/04_data.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        # 写入第一行头信息
        writer.writerow(['标题', "小区名称", "小区信息", "上传时间", "总价(万)", "单价(元/平)"])


def user_agent():
    user_agent = UserAgent().random
    return user_agent


def get_data():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Referer": "https://sy.ke.com/ershoufang/l1/",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": user_agent(),
        "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "lianjia_uuid": "08c21043-45e0-4c46-8b5b-bcd933134967",
        "crosSdkDT2019DeviceId": "-vjlefq--lum24z-3v4iin9xdiwjn7r-nh88c1i5s",
        "lianjia_ssid": "d6386f60-ab35-4670-b7fe-10521225ce56",
        "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%2218b378a72bc581-094798eaf17ad9-26031e51-1440000-18b378a72bd10be%22%2C%22%24device_id%22%3A%2218b378a72bc581-094798eaf17ad9-26031e51-1440000-18b378a72bd10be%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22http%3A%2F%2Fwww.hwj.com%2F%22%2C%22%24latest_referrer_host%22%3A%22www.hwj.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D",
        "select_city": "210100",
        "Hm_lvt_9152f8221cb6243a53c83b956842be8a": "1711961708",
        "Hm_lpvt_9152f8221cb6243a53c83b956842be8a": "1711961750",
        "srcid": "eyJ0Ijoie1wiZGF0YVwiOlwiZDQwNjkyNTYyYWJhM2NmZTkxZmViZjBlMzhiMjRjN2IwNjc4YjdkZTc4ZDNkZWY4NWI3ZGM5MjA1ZjQ4MmQ1NTkxNWQ5ZDNlMTYyNjJlZjBlOTg2OWMxMWNkZDFhODkxYzMxOTBlOTkwNTBiYzYwZTBmZWE3MDkxYjc3YmM3MDg3YThmZjRiMjU1OTU2YTg3NDRiZmQ5ZDE0ODA3ZDc3ZGU5ZWQ3M2UzYmZiZTQyNDNjNDZkNTRlZmUzY2NkNDlhMWMyMjMyZDlmMjU0NmM2ZjY5NTllOWQ0ODBkMzlmNzliYmM0Y2ZhOTA1OWNjMDNjNTY0MzM1OWFlOGVkMmUyYlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJjMTEzZWVkYVwifSIsInIiOiJodHRwczovL3N5LmtlLmNvbS9lcnNob3VmYW5nLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9"
    }
    url = "https://sy.ke.com/ershoufang/"
    response = requests.get(url, headers=headers, cookies=cookies)
    content = response.text
    html = etree.HTML(content)
    lis = html.xpath('//ul[@class="sellListContent"]//li[@class="clear"]')
    for li in lis:
        # 标题
        name = li.xpath('.//div[@class="title"]/a/text()')[0].strip()
        # 小区名称
        position = li.xpath('.//div[@class="flood"]/div/a/text()')[0].strip()
        # 小区信息
        info = li.xpath('.//div[@class="houseInfo"]/text()')[0].strip()
        # 上传时间
        follow = li.xpath('.//div[@class="followInfo"/text()')[0].strip()
        # 总价
        total = li.xpath('.//div[@class="priceInfo"]/div[1]/span/text()')[0].strip()
        # 单价
        unit = li.xpath('.//div[@class="priceInfo"]/div[2]/span/text()')[0].replace('元/平', '')


if __name__ == '__main__':
    get_data()

