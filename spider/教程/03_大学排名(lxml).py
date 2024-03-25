import requests
from lxml import etree

def get_html(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = "utf-8"
        return response.text
    else:
        return


def get_info(html):
    html = etree.HTML(html)
    # 提取所有的大学标签信息
    ls = html.xpath('//table[@class="rk-table"]/tbody/tr')
    for info in ls:
        # 排名
        rank = info.xpath("./td[1]/div/text()")[0]
        rank = rank.strip()
        # 学校名
        name = info.xpath("./td[2]//a[@class='name-cn']/text()")[0]
        name = name.strip()
        # 省份
        province = info.xpath("./td[3]/text()")[0].strip()
        # 总分
        score = info.xpath("./td[5]/text()")[0].strip()

        data = {
            "排名": rank,
            "校名": name,
            "省份": province,
            "总分": score
        }
        print(data)


def main():
    url = "https://www.shanghairanking.cn/rankings/bcur/2023"
    html = get_html(url)
    get_info(html)


if __name__ == "__main__":
    main()

