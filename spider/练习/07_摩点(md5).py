import requests
import time
from lxml import etree
from fake_useragent import UserAgent
from hashlib import md5

# https://zhongchu.modian.com


def user_agent():
    user_agent = UserAgent().random
    return user_agent


def basic_param():
    index_url = "https://apim.modian.com/recommend/feed_list"
    comment_url = "https://apim.modian.com/apis/mdcomment/get_reply_list_rt"
    headers = {
        "User-Agent": user_agent()
    }
    basic_dict = {
        "index_url": index_url,
        "comment_url": comment_url,
        "headers": headers
    }
    return basic_dict


def index_deal():
    """主页处理函数"""
    basic_dict = basic_param()
    mt, sign = get_data()
    print('mt', mt)
    print('sign', sign)
    # basic_dict['headers']['Sign'] = "6ff6a3146970c0ff791fe502b3d44c2d"
    # basic_dict['headers']['Mt'] = "1712111551"
    basic_dict['headers']['Sign'] = sign
    basic_dict['headers']['Mt'] = mt
    params = {
        "ad_position": "pc_home_onlineproject"
    }
    response = requests.get(url=basic_dict["index_url"], headers=basic_dict['headers'], params=params)
    print("response", response.text)
    html = etree.HTML(response.text)


def get_data():
    hosts = "apim.modian.com/apis/mdcomment/get_reply_list_rt"
    apimData = str(int(time.time()))
    appkey = "MzgxOTg3ZDMZTgxO"
    decodeURIComponent_query = "post_id=879365"
    decodeURIComponent_props = ""
    sign = md5((hosts + appkey + apimData + decodeURIComponent_query + md5(decodeURIComponent_props.encode()).hexdigest()).encode()).hexdigest()
    mt = apimData
    return mt, sign


def comment_deal():
    pass


if __name__ == '__main__':
    # comment_deal()
    # get_data()
    index_deal()




