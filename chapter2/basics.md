# Tornado相关知识

### 优点
+ 微框架、高性能
+ 异步支持

### 缺点
+ 轮子少，不像Django、Flask等框架有大量插件支持
+ 缺少最佳实践，使用的公司不多，学习资料少

### 适合场景
构建微服务：不适合复杂的CMS（内容管理系统）应用【django更加适用】，适合构建网站或者App后端微服务

### 学习资料
+ [官方文档](https://tornado-zh-cn.readthedocs.io/zh_CN/latest/guide/intro.html)
+ [《Introduction to Tornado》](https://blog.csdn.net/miss1181248983/article/details/96731648)

### 安装使用
```
# pip3 install tornado

# python

>>> import tornado
>>> tornado.version
'6.0.3'
```
