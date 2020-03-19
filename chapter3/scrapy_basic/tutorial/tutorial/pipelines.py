# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from tutorial.settings import MONGO_SETTINGS


class TutorialPipeline(object):

    def __init__(self):
        client = pymongo.MongoClient(
            host=MONGO_SETTINGS["host"],
            port=MONGO_SETTINGS["port"],
        )
        mydb = client[MONGO_SETTINGS["db_name"]]

        self.post = mydb[MONGO_SETTINGS["db_collection"]]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)

        return item
