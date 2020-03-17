# -*- coding:utf-8 -*-
"""
@Author: caizhanjin
@Time: 2020-03-17
@Detail: 
"""
from chapter3.simple_spider import url_manager, html_outputer, html_parser, html_downloader


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()

                print(f"Craw num {count}: {new_url}")

                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 10:
                    break
                count += 1
            except Exception as error:
                print(f"num {count} Craw error: {error}")

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/%E9%87%8F%E5%8C%96"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
