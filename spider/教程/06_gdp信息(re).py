import requests
import re
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


def gdp_info(html):
    pat = '<p>(\d+.*?)</p>'
    infos = re.findall(pat, html, re.S)

    datas = []
    for info in infos:
        # 人数
        pat1 = '.*?(\d+)万'
        people = re.findall(pat1, info)
        # gdp
        pat2 = '(\d+)亿元'
        gdp = re.findall(pat2, info)
        # 城市
        pat3 = '\d+\.(.*?)\d+亿元'
        city = re.findall(pat3, info)
        city = city[0].split('（')[0] + "市"
        try:
            datas.append((city, gdp[0], people[0]))
        except:
            pass
    return datas


if __name__ == "__main__":
    url = "http://caifuhao.eastmoney.com/news/20190201115604564011000"
    html = get_html(url)
    data = gdp_info(html)
    print(data)

    url = 'https://www.internorga.com/en/fair/exhibitors-products?' \
          'type=1603899437&' \
          'tx_hmcplatform_api%5BobjectType%5D=CORPORATION&' \
          'tx_hmcplatform_api%5Bpage%5D={}&' \
          'tx_hmcplatform_api%5Blimit%5D=30'
