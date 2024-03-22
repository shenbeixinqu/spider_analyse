from bs4 import BeautifulSoup
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
    """
    提取数据
    """
    soup = BeautifulSoup(html)
    # 排名
    ranks = soup.select("#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num")
    # 歌手 + 歌名
    names = soup.select("#rankWrap > div.pc_temp_songlist > ul > li > a")
    # 播放时间
    times = soup.select("#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span")
    #  zip 函数的结果是一个列表 [(排名，歌手歌名，播放时间)，(排名，歌手歌名，播放时间)。。。。。]
    for r, n, t in zip(ranks, names, times):
        r = r.get_text().replace('\n', '').replace('\t', '').replace('\r', '')
        n = n.get_text().replace('\n', '').replace('\t', '').replace('\r', '')
        t = t.get_text().replace('\n', '').replace('\t', '').replace('\r', '')
        data = {
            '排名': r,
            '歌名-歌手': n,
            '播放时间': t
        }
        print(data)


def main():
    """
        主接口
    """
    urls = ["https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank".format(str(i)) for i in range(1, 24)]
    for url in urls:
        html = get_html(url)
        get_infos(html)
        time.sleep(1)


if __name__ == "__main__":
    main()
