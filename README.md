# CODE_DEMO

### chapter1 项目上线流程：将网站发布到互联网
必备条件：
+ 1台linux服务器：CentOS/ubuntu
+ 1款Web服务器：Nginx/Apache/Tomcat
+ 1个独立域名：域名解析时，注意添加www、@记录（通过二级域名，一个域名可以解析到多个服务器）
+ 使用国内服务器需进行备案

具体操作参考：[一篇搞定！Django+vue服务器部署](./chapter1/chapter1.md)

### chapter2 上手Tornado
+ [Tornado基础知识](./chapter2/basics.md)
+ [使用Tornado构建**RESTful**微服务](./chapter2/RESTful.md)
+ [项目结构实践方案](https://github.com/caizhanjin/tornado_framework)（url路由分发、cx_Oracle再封装和引入、sqlalchemy ORM引入、loging配置引入、restful风格编写示例）
+ Tornado服务器部署
 
### chapter3 数据分析/挖掘相关
+ 科学计算包使用
    + [pandas](./chapter3/pandas.md) 

+ 数据采集
    + 现有工具：八爪鱼
    + [一个简单爬虫架构](chapter3/simple_spider/simple_spider.md)
    + [爬虫框架Scrapy入门与实践](chapter3/scrapy_basic/scrapy_basic.md)

+ 数据诊断/清洗工具示例：
    + [数据描述/统计指标基础和实现](./chapter3/data_dumps/data_dumps.py)：pandas/numpy/scipy基础使用
    + [整合数据诊断工具](./chapter3/data_dumps/wrap_up.py)
    + [工具性能和效率测试](./chapter3/data_dumps/wrap_up_with_time.py)

+ 算法 : 决策树/朴素贝叶斯分类/SVM/KNN/K-Means/EM聚类/关联规则挖掘/PageRank/AdaBoost

### chapter4 数据分析实战
+ [一个基于vue大数据展示页面示例](./chapter4/data_show_vue/data_show_vue.md)
+ [Python爬虫实战数据可视化分析](./chapter4/spider_and_show/spider_and_show.md)

### chapter5 Python编程
+ [深入面向对象](./chapter5/OO.md)：属性/方法定义，构造函数，单继承，多继承，多态，魔术方法，类装饰器，访问控制，常用基类
+ [collections模块/数据结构](./chapter5/collections.md)：常见数据结构使用深入
+ [logging日志模块标准调用](./chapter5/logging.md)
+ [《编写高质量Python代码的59个有效方法》](./chapter5/code_advise/code_advise.md)
+ [异步任务队列Celery使用](./chapter5/celery/celery.md)：进程管理和监控工具
+ [深入理解协程、线程、进程，GIL锁](./chapter5/gil/gil.md)：python高效秘诀
+ [单例模式](https://www.cnblogs.com/huchong/p/8244279.html#_lab2_1_3)

### chapter6 数据库
+ [sql命令](./chapter6/sql.md)
+ [数据设计深入理解](./chapter6/db_design.md)
+ [mysql安装和使用](./chapter6/mongodb.md)
+ [mongodb安装和使用](./chapter6/mongodb.md)

### chapter7 命令备忘录
+ [git](./chapter7/git.md)
+ [pip/conda/yum/docker](./chapter7/packages.md)：虚拟环境管理/python安装
+ [linux](./chapter7/linux.md)：防火墙
+ [web服务器](./chapter7/web_server.md)：nginx
+ [docker](./chapter7/docker.md)

### chapter8 分布式
+ [基于python实现RPC](./chapter8/rpc/rpc.md)

### chapter9 web编程
+ 基于vue自适应+响应式管理系统示例
+ VUE+Centos+Github+Jenkins自动化运维

### 其他
+ 微服务架构【腾讯云tsf】

