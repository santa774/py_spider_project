# -*- coding: utf-8 -*-
import urllib2
import urllib

url = "http://www.youdao.com/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}


def test_handler():
    """
        作用：测试handler的用法
    """
    http_handler = urllib2.HTTPHandler(debuglevel=1)
    opener = urllib2.build_opener(http_handler)
    request = urllib2.Request(url, headers=header)
    response = opener.open(request)
    print response.read()


def test_proxy_handler(switch):
    """
        作用：测试代理handler 的用法
    """
    if switch:
        proxy_handler = urllib2.ProxyHandler({"http": "180.101.205.253:8888"})
    else:
        proxy_handler = urllib2.ProxyHandler({})

    opener = urllib2.build_opener(proxy_handler)
    # 注册全局的opener
    urllib2.install_opener(opener)
    request = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(request)
    if switch:
        html = response.read().decode("utf-8")
    else:
        html = response.read()
    print html


if __name__ == "__main__":
    # test_handler()
    test_proxy_handler(True)
