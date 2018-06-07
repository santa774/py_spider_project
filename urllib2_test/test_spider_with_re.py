# -*- coding: utf-8 -*-
import urllib2
import urllib


class ComicSpider:

    def __init__(self, url):
        self.url = url  # http://ac.qq.com/ComicView/index/id/505430/cid/855
        self.comic_header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}
        pass

    def loadpage(self, startpage, endpage):
        for page in range(startpage, endpage):
            request = urllib2.Request(self.url + str(page), headers=self.comic_header)
            proxy_handler = urllib2.ProxyHandler({})
            opener = urllib2.build_opener(proxy_handler)
            urllib2.install_opener(opener)
            response = urllib2.urlopen(request)
            file_path = r"G:\\comic\\yiquanchaoren_" + str(page) + ".html"
            self.write2file(file_path, response.read())
            # print response.read()

    def write2file(self, file_path, file_context):
        # comic_file = open(file_path, 'w')
        # comic_file.write(file_context)
        # comic_file.close()
        with open(file_path, "w") as f:
            f.write(file_context)
        print "done"


if __name__ == "__main__":
    comic_spider = ComicSpider("https://manhua.dmzj.com/yiquanchaoren/25445.shtml#@page=")
    comic_spider.loadpage(1, 5)
