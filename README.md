# CODE_DEMO

### chapter0 系统/代码设计【实战】
+ [秒杀/抽奖高并发代码实现(乐观锁 + 事务)](./chapter0/seckill/seckill.py)
+ [管理系统操作系统通用设计方案(附日志操作类)](./chapter0/log_operation.md)
+ [即时通讯方案：websocket + 心跳机制实现长连接 & redis缓存](./chapter0/chat/chat.md)
+ [websocket长连接压力测试](https://www.cnblogs.com/devtest/p/9966465.html)
+ [logging日志模块标准调用](./chapter0/logging.md)
+ VUE+Centos+Github+Jenkins自动化运维
+ [基于vue自适应+响应式管理系统示例](./chapter0/data_borad/data_borad.md)

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
+ [django数据库连接池的使用](https://github.com/altairbow/django-db-connection-pool)、[为什么使用连接池](https://www.cnblogs.com/sharpest/p/6240475.html)
#### Django
+ [Django基础教程](https://code.ziqiangxuetang.com/django/django-queryset-advance.html)
+ [Django利用celery编写异步代码](https://www.jianshu.com/p/61e573611a06?tdsourcetag=s_pcqq_aiomsg)
+ 个人博客项目代码示例：[ZhanjinBlog后端api](https://github.com/caizhanjin/zhanjinblog_api)
+ [一个django sql绑定变量的用法](./chapter2/django_sql.md)：解决高并发时ORM性能上的大坑

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
+ [实战！！！多进程、多线程、进程池以及以上情况的通讯工具类\让cpu上升到100%](./chapter5/code/multi_tasks_tools.py)
+ [单例模式](https://www.cnblogs.com/huchong/p/8244279.html#_lab2_1_3)
+ [asyncio异步编程](https://www.cnblogs.com/zhangyafei/p/13302982.html)
+ 上下文管理器
+ [性能测试工具Locust](https://debugtalk.com/post/head-first-locust-user-guide/)
+ python动态特性：动态修改执行中的代码，locals字典，eval执行代码， 
+ [23种设计模式学习](https://www.cnblogs.com/leokale-zz/p/12336503.html)
+ [python数据结构](https://blog.csdn.net/weixin_42223833/article/details/86683352)
    + 顺序表：将元素顺序地存放在一块连续的存储区里，list就是一种元素个数可变的线性表
    + [单向列表](./chapter5/data_structure/single_list.py)：只有一个方向，当前节点指向链表中的下一个节点，而最后一个节点的链接域则指向一个空值
+ [python排序算法](https://www.cnblogs.com/fwl8888/p/9315730.html)

### chapter6 数据库
+ [不同场景sql示例](./chapter6/sql.md)
+ [数据设计深入理解](./chapter6/db_design.md)
+ [mysql安装和使用](./chapter6/mongodb.md)
+ [mongodb安装和使用](./chapter6/mongodb.md)
+ Redis缓存
+ 连接池之Redis连接池
+ [orm之peewee使用](https://www.cnblogs.com/miaojiyao/articles/5217757.html)
+ 高并发下数据解决方案
    + [淘宝服务端高并发分布式架构演进之路](https://segmentfault.com/a/1190000018626163)
    + [数据库结构的设计1](https://www.cnblogs.com/llcdbk/p/8183509.html)
    + [数据库结构的设计2](https://blog.csdn.net/qq_36236890/article/details/82390412)
    
### chapter7 命令备忘录
+ [git](./chapter7/git.md)
+ [pip/conda/yum/docker](./chapter7/packages.md)：虚拟环境管理/python安装
+ [linux](./chapter7/linux.md)：防火墙
+ [docker](./chapter7/docker.md)

### chapter8 分布式
+ [基于python实现RPC(socket编程)](./chapter8/rpc/rpc.md)
+ 使用RPC协议实现微服务



### 其他

