# -*- coding: utf-8 -*-
import urllib2
import urllib

url = "http://tieba.baidu.com/f?"


def tieba_spider(tieba_name, start_pg, end_pg):
    """
    :param tieba_name:
    :param start_pg:
    :param end_pg:
    :return:
    """
    # http://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=0
    for page in range(int(start_pg), int(end_pg) + 1):
        html_name = r"G:\\" + str(page) + ".html"

        page = (page - 1) * 50
        encode_data = {"kw": str(tieba_name), "ie": "utf-8", "pn": str(page)}
        request_param = urllib.urlencode(encode_data)
        newurl = url + request_param
        get_header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}
        request = urllib2.Request(newurl, headers=get_header)
        response = urllib2.urlopen(request)
        html = response.read()

        with open(html_name, 'w') as f:
            f.write(html)


if __name__ == "__main__":
    tieba_name = raw_input("请输入你要爬取的贴吧：")
    start_pg = int(raw_input("请输入起始页："))
    end_pg = int(raw_input("请输入结束页："))
    tieba_spider(tieba_name, start_pg, end_pg)
    # with open(r"G:\\1.html") as f:
    #     print(str.decode(f.read(), "utf-8"))
