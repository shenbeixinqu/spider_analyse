import requests
import time
from lxml import etree
from hashlib import md5


indexurl = 'https://zhongchou.modian.com/all/top_time/all/' # 主页url
comment_url = 'https://apim.modian.com/apis/mdcomment/get_reply_list'   # 获取评论信息的接口
params = {
    'mapi_query_time': '0',
    'order_type': '2',
    'page': '1',
    'page_size': '20',
    'post_id': '257718',
    'pro_class': '101',
    'pro_id': None,
    'request_id': ''
}   # 构造请求评论所在url时需要传递的参数
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}   # 构造请求头


def indexDeal(indexurl, headers):
    """主页处理函数"""
    response = requests.get(indexurl, headers=headers)  # 访问主页
    tree = etree.HTML(response.content.decode())
    detail_url = tree.xpath('/html/body/div/div[2]/ul/li[2]/div/a/@href')[0]    # 解析出详情页的url，此处为古蜀华章，请根据实际情况修改
    pro_id = detail_url.split('/')[-1].split('.')[0]    # 经过两次分割提取出pro_id，当然也可以直接以切片的形式提取
    response_detail = requests.get(detail_url,headers=headers)  # 访问详情页
    tree_detail = etree.HTML(response_detail.content.decode())
    post_id = tree_detail.xpath('/html/body/div[3]/div/div[2]/input[2]/@value')[0]  # 从详情页提取post_id
    return pro_id, post_id


def getData(post_id, pro_id):
    hosts = 'apim.modian.com/apis/mdcomment/get_reply_list'
    apimData = str(int(time.time()))   # 在Python中时间戳精度为10的9次方，所以此处不用再除以1000，直接取整即可，不理解的话可以输出在终端查看
    appkey = 'MzgxOTg3ZDMZTgxO'
    decodeURIComponent_query = f'mapi_query_time=0&order_type=2&page=1&page_size=20&post_id={post_id}&pro_class=101&pro_id={pro_id}&request_id='
    decodeURIComponent_props = ''
    sign = md5(
        (hosts+appkey+apimData+decodeURIComponent_query+md5(decodeURIComponent_props.encode())
         .hexdigest())
            .encode()
    ).hexdigest()
    mt = apimData
    print(mt, sign)
    return mt, sign


def commentDeal(comment_url, headers, params):
    """获取评论"""
    pro_id, post_id = indexDeal(indexurl, headers)   # 获取pro_id
    mt, sign = getData(post_id, pro_id)
    headers['mt'] = mt    # 注意参数有时效所以测试的时候记得刷新页面重新获取
    headers['sign'] = sign
    params['pro_id'] = pro_id   # 将pro_id赋值到params中进行带参请求
    params['post_id'] = post_id # 将post_id赋值到params中
    response = requests.get(comment_url, params=params, headers=headers)
    print(response.content.decode())


if __name__ == '__main__':
    commentDeal(comment_url, headers, params)