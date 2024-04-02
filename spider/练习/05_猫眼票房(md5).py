import requests
import time
import random
import base64
import hashlib
from fake_useragent import UserAgent


def user_agent():
  user_agent = UserAgent().random
  return user_agent


def get_data():
    url = "https://piaofang.maoyan.com/dashboard-ajax/movie"
    useragents = user_agent()
    useragents = str(base64.b64encode(useragents.encode('utf-8')), 'utf-8')
    headers = {
        'User-Agent': useragents,
    }
    index = str(int(random.random() * 1000))
    print('index', index)
    times = str(int(time.time() * 1000))
    print('times', times)
    content = "method=GET&timeStamp={}&User-Agent={}&index={}&channelId=40009&sVersion=2&key=30b0a24e2cbb4fd082c27e882907266a".format(times, useragents, index)
    md5 = hashlib.md5()
    md5.update(content.encode('utf-8'))
    sign = md5.hexdigest()
    params = {
        'orderType': '0',
        'uuid': '181239113b48-00d6486f1b410b-14333270-15f900-181239113b5c8',
        # 时间戳
        'timeStamp': times,
        # base64加密
        'User-Agent': useragents,
        # 随机数 * 1000取整
        'index': index,
        'channelId': '40009',
        'sVersion': '2',
        # md5加密
        'signKey': sign
    }
    response = requests.get(url=url, headers=headers)
    data = response.json()
    movie_list = data['movieList']['list']
    results = []
    for movie in movie_list:
        result = {
            # 电影名称
            "name": movie['movieInfo']['movieName'],
            # 上映时间
            "release_time": movie['movieInfo']['releaseInfo'],
            # 上座率
            "seat": movie['avgSeatView'],
            # 场均人次
            "show": movie['avgShowView'],
            # 票房占比
            "rate": movie['boxRate'],
            # 总票房
            "sum": movie['sumBoxDesc'],
            # 排片场次
            "count": movie['showCount'],
            # 排片占比
            "countRate": movie['showCountRate']
        }
        print(result)
        results.append(result)


if __name__ == '__main__':
    get_data()
