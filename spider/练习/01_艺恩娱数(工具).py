import requests
import time
from fake_useragent import UserAgent


# 获取随机useragent
def get_useragent():
    user_agent = UserAgent().random
    return user_agent


def get_data(p):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://ys.endata.cn",
        "Referer": "https://ys.endata.cn/BoxOffice/Org",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "JSESSIONID": "924de965-1a7c-420d-acb7-8a05017fa958",
        "route": "4e39643a15b7003e568cadd862137cf3",
        "Hm_lvt_82932fc4fc199c08b9a83c4c9d02af11": "1711697792",
        "Hm_lpvt_82932fc4fc199c08b9a83c4c9d02af11": "1711697792",
        "SECKEY_ABVK": "9TdlauK2uKOfhwmYjhQ4VgplsxU8qfFenHitH47rfLo%3D",
        "BMAP_SECKEY": "dg2JOlioVVhdvgEJrezxAeqgtmPL21d8kb1PgxGHaEWHDLYo-A9SSUM5v7yEVKeRhnFPKRXQ8alGB6zFVYVcLe37n8OmqRYgqEpfDiyR4tmd03MgrAYSZq_ujtjZgCZKq8CbAG22VStmDj-5QO42pEgkVu01c4TSS1VOJPyR4tqyzhHAXOFslLxlvHwS6jHp"
    }
    url = "https://ys.endata.cn/enlib-api/api/cinema/getcinemaboxoffice_day_list.do"
    data = {
        "r": "0.04865721954060209",
        "bserviceprice": "0",
        "datetype": "Day",
        "date": "2024-03-28",
        "sdate": "2024-03-28",
        "edate": "2024-03-28",
        "citylevel": "",
        "lineid": "",
        "columnslist": "100,101,102,121,122,103,104,108,123,109",
        "pageindex": p,
        "pagesize": "20",
        "order": "102",
        "ordertype": "desc"
    }
    response = requests.post(url, headers=headers, data=data)
    datas = response.json()['data']['table1']
    results = []
    for data in datas:
        result = {
            "影院名称": data['CinemaName'],
            "省份": data['ProvinceName'],
            "城市": data['CityName'],
            "票房": data['BoxOffice'],
            "场次": data['ShowCount'],
            "人次(万)": data['AudienceCount'],
            "平均票价": data['AvgBoxOffice'],
            "天数": data['Irank'],
            "场均人次": data['AvgShowAudienceCount']
        }
        results.append(result)
    return results


def main():
    result_all = []
    for p in range(1, 2):
        print(f'>>>正在获取:{p}页')
        results = get_data(p)
        [result_all.append(result) for result in results]  # 将全部页数据保存于此
        time.sleep(3)


if __name__ == "__main__":
    main()
