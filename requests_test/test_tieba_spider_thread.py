# -*- coding: utf-8 -*-
import requests
from threading import Thread
from Queue import Queue
from lxml import etree
import time


class CrawlSpider(Thread):

    def __init__(self, thread_name, queue, tieba_name):
        super(CrawlSpider, self).__init__()
        self.thread_name = thread_name
        self.queue = queue
        self.tieba_name = tieba_name
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
        }

    def run(self):
        print "CrawlSpider running: " + self.thread_name
        self.load_tieba_page()
        print "CrawlSpider over: " + self.thread_name

    def load_tieba_page(self):
        proxies = {
            "http": "180.101.205.253:8888",
            "https": "180.101.205.253:8888"
        }
        url = "http://tieba.baidu.com/f?"
        while True:
            if self.queue.empty():
                break
            else:
                try:
                    page = int(self.queue.get())
                    page = (page - 1) * 50
                    param = {"kw": self.tieba_name, "pn": str(page)}

                    # 超时请求次数，防止死循环
                    timeout = 4
                    while timeout > 0:
                        timeout -= 1

                        try:
                            # requests方式请求数据
                            tieba_response = requests.get(url, params=param, headers=self.header)
                            html = tieba_response.content
                            # 以上获取的内容为贴吧一整页的html，包含了帖子的列表
                            # 获取每一个帖子的链接
                            xpath_result = etree.HTML(html)
                            tiezi_list = xpath_result.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')

                            for tiezi_url in tiezi_list:
                                url = "http://tieba.baidu.com" + tiezi_url
                                tiezi_response = requests.get(url, headers=self.header)
                                html = tiezi_response.content
                                # 以上获取的内容为帖子一整页的html
                                # 获取每一个帖子的图片链接
                                data_queue.put(html)
                            break
                        except Exception, e:
                            print "CrawlSpider: " + self.thread_name + ", Exception: " + e.message
                    if timeout < 0:
                        print "timeout: " + self.thread_name
                except:
                    pass


class ParseSpider(Thread):
    def __init__(self, thread_name, queue):
        super(ParseSpider, self).__init__()
        self.thread_name = thread_name
        self.queue = queue
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
        }

    def run(self):
        print "ParseSpider running: " + self.thread_name
        self.load_tiezi_page()
        print "ParseSpider over: " + self.thread_name

    def load_tiezi_page(self):
        global EXIT_PARSE_FLAG
        while not EXIT_PARSE_FLAG:
            try:
                html = self.queue.get(False)
                xpath_result = etree.HTML(html)
                tiezi_img_list = xpath_result.xpath('//img[@class="BDE_Image"]/@src')
                self.load_image(tiezi_img_list)
                self.queue.task_done()
            except:
                pass

    def load_image(self, tiezi_ima_list):
        for img_url in tiezi_ima_list:
            img_response = requests.get(img_url, headers=self.header)
            img_name = img_url[-7:]
            with open("G:\\tieba\\" + img_name, "wb") as f:
                f.write(img_response.content)


data_queue = Queue()
EXIT_PARSE_FLAG = False


def main(tieba_name, start_page, end_page):
    star_time = time.time()
    page_queue = Queue(50)
    for page in range(int(start_page), int(end_page)):
        page_queue.put(page)

    # 启动抓取线程
    crawl_list = []
    crawl_name_list = ["crawl_spider_1", "crawl_spider_2", "crawl_spider_3", "crawl_spider_4", "crawl_spider_5", "crawl_spider_6", "crawl_spider_7", "crawl_spider_8", "crawl_spider_9", "crawl_spider_10"]
    for thread_name in crawl_name_list:
        crawl_thread = CrawlSpider(thread_name, page_queue, tieba_name)
        crawl_thread.start()
        crawl_list.append(crawl_thread)

    # 启动解析线程
    parse_list = []
    parse_name_list = ["parse_spider_1", "parse_spider_2", "parse_spider_3", "parse_spider_4", "parse_spider_5", "parse_spider_6", "parse_spider_7", "parse_spider_8", "parse_spider_9", "parse_spider_10"]
    for thread_name in parse_name_list:
        parse_thread = ParseSpider(thread_name, data_queue)
        parse_thread.start()
        parse_list.append(parse_thread)

    # 等待任务队列被取空
    while not page_queue.empty():
        pass

    # 等待抓取线程全部执行完成
    for crawl in crawl_list:
        crawl.join()

    # 等待数据队列被取空
    while not data_queue.empty():
        pass

    global EXIT_PARSE_FLAG
    EXIT_PARSE_FLAG = True

    # 等待解析线程全部执行完成
    for parse in parse_list:
        parse.join()

    print "done"
    print "耗时：" + str(time.time() - star_time)


if __name__ == "__main__":
    tieba_name = raw_input("请输入要爬取的贴吧：")
    start_page = raw_input("请输入起始页：")
    end_page = raw_input("请输入结束页：")
    main(tieba_name, start_page, end_page)
