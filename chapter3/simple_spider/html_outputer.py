# -*- coding:utf-8 -*-
"""
@Author: caizhanjin
@Time: 2020-03-17
@Detail: 
"""
import csv


class HtmlOutputer(object):
    def __init__(self):
        self.data_list = []

    def collect_data(self, data):
        if data is None:
            return
        self.data_list.append(data)

    def output_html(self):
        if len(self.data_list) == 0:
            return
        array_list = [[item["title"], item["summary"], item["url"]] for item in self.data_list]
        with open("save_data.csv", "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(["title", "summary", "url"])
            writer.writerows(array_list)
