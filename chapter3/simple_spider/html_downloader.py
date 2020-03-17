# -*- coding:utf-8 -*-
"""
@Author: caizhanjin
@Time: 2020-03-17
@Detail: 
"""
import urllib.request


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()
