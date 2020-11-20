# CODE_DEMO

### chapter1 项目上线流程：将网站发布到互联网
必备条件：
+ 1台linux服务器：CentOS/ubuntu
+ 1款Web服务器：Nginx/Apache/Tomcat
+ 1个独立域名：域名解析时，注意添加www、@记录（通过二级域名，一个域名可以解析到多个服务器）
+ 使用国内服务器需进行备案

具体操作参考：[一篇搞定！Django+vue服务器部署](./chapter1/chapter1.md)
+ [Nginx/uwsgi配置文件示例](./chapter1/config.md)

### chapter2 上手Django/Tornado/vue
+ [django、flask、tornado对比](https://www.imooc.com/article/24759)： django大而全、flask小而精、tornado性能高

#### Django
+ [Django基础教程](https://code.ziqiangxuetang.com/django/django-queryset-advance.html)
+ [django+celery+redis框架搭建](https://www.jianshu.com/p/61e573611a06?tdsourcetag=s_pcqq_aiomsg)
+ 个人博客项目代码示例：[ZhanjinBlog后端api](https://github.com/caizhanjin/zhanjinblog_api)

#### Tornado
+ [Tornado基础知识](./chapter2/basics.md)
+ [使用Tornado构建**RESTful**微服务](./chapter2/RESTful.md)
+ [项目结构实践方案](https://github.com/caizhanjin/tornado_framework)（url路由分发、cx_Oracle再封装和引入、sqlalchemy ORM引入、loging配置引入、restful风格编写示例）
+ Tornado服务器部署

#### vue
+ [父子、兄弟参数传递](./chapter2/basics.md)
 
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
+ [《编写高质量Python代码的59个有效方法》](./chapter5/code_advise/code_advise.md)
+ [异步任务队列Celery使用](./chapter5/celery/celery.md)：进程管理和监控工具
+ [深入理解协程、线程、进程，GIL锁](./chapter5/gil/gil.md)：python高效秘诀
+ 性能测试：如何让cpu上升到100%
+ [单例模式](https://www.cnblogs.com/huchong/p/8244279.html#_lab2_1_3)
+ [asyncio异步编程](https://www.cnblogs.com/zhangyafei/p/13302982.html)
+ 上下文管理器
+ 队列queue

### chapter6 数据库
+ [sql命令](./chapter6/sql.md)
+ [数据设计深入理解](./chapter6/db_design.md)
+ [mysql安装和使用](./chapter6/mongodb.md)
+ [mongodb安装和使用](./chapter6/mongodb.md)
+ Redis缓存

### chapter7 命令备忘录
+ [git](./chapter7/git.md)
+ [pip/conda/yum/docker](./chapter7/packages.md)：虚拟环境管理/python安装
+ [linux](./chapter7/linux.md)：防火墙
+ [docker](./chapter7/docker.md)

### chapter8 分布式
+ [基于python实现RPC(socket编程)](./chapter8/rpc/rpc.md)
+ 使用RPC协议实现微服务

### chapter9 系统/代码设计
+ [logging日志模块标准调用](./chapter9/logging.md)
+ [基于vue自适应+响应式管理系统示例](./chapter9/data_borad/data_borad.md)
+ VUE+Centos+Github+Jenkins自动化运维
+ [管理系统操作系统通用设计方案(附日志操作类)](./chapter9/log_operation.md)
+ [秒杀/抽奖高并发代码实现(乐观锁 + 事务)](./chapter9/seckill/seckill.py)
+ [即时通讯方案：websocket + 心跳机制实现长连接 & redis缓存](./chapter9/chat/chat.md)
+ [websocket长连接压力测试](https://www.cnblogs.com/devtest/p/9966465.html)

### 其他

