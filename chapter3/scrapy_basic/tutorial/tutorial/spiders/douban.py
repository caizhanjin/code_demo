# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import DoubanItem


class DoubanSpider(scrapy.Spider):
    # 爬虫名
    name = 'douban'
    # 允许域名
    allowed_domains = ['movie.douban.com']
    # 入口url
    start_urls = ['https://movie.douban.com/top250']

    # 默认解析方法
    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for item in movie_list:
            douban_item = DoubanItem()
            douban_item["serial_number"] = item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item["movie_name"] = item.xpath(".//div[@class='item']//div[@class='info']//a//span[1]/text()").extract_first()
            contents = item.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//p[1]/text()").extract()
            content_s = ""
            for i_content in contents:
                content_s += "".join(i_content.split()).replace("...", " ")
            douban_item["introduce"] = content_s
            douban_item["evaluate"] = item.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//span[@class='rating_num']/text()").extract_first()
            douban_item["describe"] = item.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//p[@class='quote']//span/text()").extract_first()

            # yield到pipelines中去
            yield douban_item

        # 下一页解析
        next_link = movie_list.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse)
