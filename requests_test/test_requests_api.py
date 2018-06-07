# -*- coding: utf-8 -*-
import requests

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}


def test_get():
    url = "https://manhua.dmzj.com/yiquanchaoren/25445.shtml#@page=1"
    # param = {"wd": "abc"}
    response = requests.get(url, headers=header)
    with open("G:\\comic\\onepunch.html", "w") as f:
        f.write(response.content)
    # print response.text
    # print response.content
    # print response.status_code
    # print response.url
    # print response.encoding
    # print response.headers


def test_post():
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    data = {
        "i": "abc",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1525921897969",
        "sign": "37d7c6ee5cbba4500c34865a794900e3",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    response = requests.post(url, data=data, headers=header)
    print response.text
    print response.json()
    print type(response.json())


def test_proxies():
    proxies = {
        "http": "180.101.205.253:8888",
        "https": "180.101.205.253:8888"
    }
    url = "http://www.baidu.com/s?"
    kw = {"wd": "大蟒蛇"}
    response = requests.get(url, params=kw, headers=header, proxies=proxies)
    print response.text


if __name__ == "__main__":
    test_get()
    # test_post()
    # test_proxies()

