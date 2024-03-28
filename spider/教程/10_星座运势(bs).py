import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def get_html(url):
    count = 0
    while True:
        headers = {
            "User-Agent": UserAgent().random
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = "utf-8"
            return response.text
        else:
            count += 1
            if count == 3:  # 超过3次请求失败则跳过
                return
            else:
                continue


def get_infos(html):
    soup = BeautifulSoup(html, 'lxml')
    luck = soup.find_all('p', class_="txt")[1].text.strip()
    return luck


def write_txt(_, info):
    """
    写入txt文件
    :param _: 星座名
    :param info: 星座运势
    :return:
    """
    with open('./data/10_luck_bs.txt', 'a+', encoding='utf-8') as f:
        info = info.strip()
        f.write(_ + '\n')
        f.write(info + '\n\n')


if __name__ == "__main__":
    # 构造url
    constellation_name = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo',
                          'Virgo', 'Libra', 'Scorpio', 'Sagittarius',
                          'Capricorn', 'Aquarius', 'Pisces']
    for _ in constellation_name:
        url = "https://www.d1xz.net/astro/{}".format(_)
        response = get_html(url)
        if response == None:
            None
        info = get_infos(response)
        write_txt(_, info)
        print(_, "爬取完毕", info)
