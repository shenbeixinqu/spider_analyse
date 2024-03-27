import requests
import re


def get_html(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        response.encoding = "utf-8"
        return response.text
    else:
        return


def get_info(html):
    pat = '<dd><a href ="/book/502/\d+.html">(.*?)</a></dd>'
    titles = re.findall(pat, html, re.S)
    for title in titles:
        print(title)


if __name__ == "__main__":
    url = "https://www.bqgka.com/book/502/"
    html = get_html(url)
    get_info(html)
