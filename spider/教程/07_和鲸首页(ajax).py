import requests
import json
from fake_useragent import UserAgent


def get_html(url):
    headers = {
        "User-Agent": UserAgent().random
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return


def get_info(html):
    json_text = json.loads(html)
    json_text = json_text["data"]
    for item in json_text:
        author = item['User']['Name']
        title = item['Title']
        describe = item['ShortDescription']
        tags = []
        for tag in item['Tags']:
            tags.append(tag['Name'])
        create_time = item['CreateDate']
        views = item['ViewsCount']
        votes = item['VotesCount']
        fork = item['ForksCount']

        print({
            "作者": author,
            "标题": title,
            "简介": describe,
            "标签": tags,
            "发布时间": create_time,
            "浏览数": views,
            "fork数": fork,
            "收藏数": votes
        })

if __name__ == "__main__":
    url = "https://www.heywhale.com/api/labs?perPage=12&page={}&Collapsed=false&sort=-SortWeight"
    urls = [url.format(str(i)) for i in range(1, 6)]
    for url in urls:
        html = get_html(url)
        if html == None:
            print('请求失败', url)
            continue
        get_info(html)
