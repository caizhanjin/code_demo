# 爬虫框架Scrapy入门与实践
基于Twisted的异步处理框架，省去很多造轮子的麻烦。架构如下：
![scrapy框架](./scrapy.png)

[官方文档](https://scrapy-chs.readthedocs.io/zh_CN/latest/)

## 常用命令
``` 
# 创建项目
scrapy startproject tutorial

# 创建爬虫应用
scrapy startproject tutorial

# 运行爬虫，spiders文件夹下
scrapy crawl douban

# 运行爬虫并保存数据，spiders文件夹下
scrapy crawl douban -o test.csv
scrapy crawl douban -o test.json

```

## 代码运行
创建server.py，写入：
``` 
from scrapy import cmdline

cmdline.execute("scray crawl douban".split())
```
运行`python server.py`
