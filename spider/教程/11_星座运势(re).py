import re
import requests
import time


def get_html(url):
    """
        获得html
    """
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return


def get_infos(html):
    pat1 = '</p><p class="txt">(.*?)</p><ul'
    response = re.findall(pat1, html, re.S)[0]
    return response


def write_txt(_, info):
    """
    写入txt文件
    :param _: 星座名
    :param info: 星座运势
    :return:
    """
    with open('./data/11_luck_re.txt', 'a+', encoding='utf-8') as f:
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

