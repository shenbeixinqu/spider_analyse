"""
Time:     2022/11/14 16:30
Author:   blue
Version:  V 0.1
File:     懂车帝.py
Describe: https://index.dongchedi.com/rank
"""
import time
import requests
import datetime


def get_data(rank_type, date):
    cookies = {
        'MONITOR_WEB_ID': '67957f17-5168-4b82-8725-fc165cb6fdb4',
        'tea_session': '62a48417-bc26-4ac5-946a-7afb81f3a11a%2C1668414173947',
    }

    headers = {
        'authority': 'index.dongchedi.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'MONITOR_WEB_ID=67957f17-5168-4b82-8725-fc165cb6fdb4; tea_session=62a48417-bc26-4ac5-946a-7afb81f3a11a%2C1668414173947',
        'referer': 'https://index.dongchedi.com/rank?rank_type=%E5%93%81%E7%89%8C&date=2022-11-13&price=%E5%85%A8%E9%83%A8%E4%BB%B7%E6%A0%BC',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    params = {
        'rank_type': rank_type,
        'date': date,
        'sub_rank_type': '全部新能源',
        'price': '全部价格',
        'province': '全国',
    }

    response = requests.get('https://index.dongchedi.com/dzx_index/rank/list', params=params, cookies=cookies,
                            headers=headers).json()

    datas = response['data']['form_data']['data']
    for data in datas[:100]:
        result = {
            'id': data['id'],
            '品牌名称': data['name'],
            '价格': data['price'],
            '懂车指数': data['index_value'],
            '日环比': data['index_hb'],
            '汽车图标': data['url'],
            '榜单类型': rank_type,
            '日期': date,
        }
        print(result)


def main():
    time_1 = datetime.date(2022, 11, 13)  # 指定结束日期
    time_2 = datetime.date(2022, 1, 1)  # 指定起始日期
    n = (time_1 - time_2).days + 1
    for d in range(n):
        yesterday = (time_1 - datetime.timedelta(days=d)).strftime('%Y-%m-%d')
        date = yesterday
        print(f'>> 正在获取 {date} 的数据')
        get_data('新能源榜单', date)
        time.sleep(0.5)


if __name__ == '__main__':
    pass