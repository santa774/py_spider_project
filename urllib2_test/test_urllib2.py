# -*- coding: utf-8 -*-
import urllib2
import urllib

url = "http://fanyi.youdao.com/"


def test_urlopen():
    response = urllib2.urlopen(url)
    print response.read()


def test_request():
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    print response.read()


def test_user_agent():
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}
    request = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(request)
    print response.read()


def test_add_header():
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}
    request = urllib2.Request(url, headers=header)
    request.add_header("Connection", "keep-alive")
    response = urllib2.urlopen(request)
    print response.read()


def test_get_header():
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}
    request = urllib2.Request(url, headers=header)
    request.add_header("Connection", "close")
    print request.get_header("Connection")


def test_urlencode():
    url = "http://www.baidu.com/"
    keyword = {"wd": "abc"}
    encode_kw = urllib.urlencode(keyword)
    url = url + "?" + encode_kw
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}
    request = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(request)
    print response.read()


if __name__ == "__main__":
    # test_urlopen()
    # test_request()
    # test_user_agent()
    # test_add_header()
    # test_get_header()
    test_urlencode()