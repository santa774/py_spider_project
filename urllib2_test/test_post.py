# -*- coding:utf-8 -*-
import urllib2
import urllib

if __name__ == "__main__":
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
    data = urllib.urlencode(data)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    }
    request = urllib2.Request(url, data, header)
    response = urllib2.urlopen(request)
    print response.read()
