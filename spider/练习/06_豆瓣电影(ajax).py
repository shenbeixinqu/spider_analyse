import requests
import time
import csv
from fake_useragent import UserAgent


def create_csv_header():
    with open('./data/06_data.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        # 写入第一行头信息
        writer.writerow(['电影', "评分", "演员"])


def user_agent():
    agent = UserAgent().random
    return agent


def get_data(p):
    url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start={}&limit=20".format(p)
    headers = {
        "User-Agent": user_agent()
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        response.encoding = "utf-8"
        return response.json()
    else:
        return


def main():
    res_list = []
    for p in range(0, 200, 20):
        print(f'>>>正在获取:{p}页')
        time.sleep(2)
        results = get_data(p)
        for result in results:
            name = result["title"]
            score = result['rating'][0]
            actors = result['actors']
            actors = ','.join(actors)
            res_list.append([name, score, actors])
    write_csv(res_list)


def write_csv(data):
    with open('./data/06_data.csv', 'a+', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for _ in data:
            writer.writerow(_)


if __name__ == '__main__':
    create_csv_header()
    main()
