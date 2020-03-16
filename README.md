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
+ 数据分析/诊断工具：
    + [数据描述/统计指标基础和实现](./chapter3/data_dumps/data_dumps.py)：pandas/numpy/scipy基础使用
    + [整合数据诊断工具](./chapter3/data_dumps/wrap_up.py)
    + [工具性能和效率测试](./chapter3/data_dumps/wrap_up_with_time.py)
+ 数据收集/清洗
+ 算法
    + 决策树
    + 朴素贝叶斯分类
    + SVM
    + KNN
    + K-Means
    + EM聚类
    + 关联规则挖掘
    + PageRank
    + AdaBoost
    
### chapter4 数据分析实战

### chapter5 Python编程
+ [深入面向对象](./chapter5/OO.md)：属性/方法定义，构造函数，单继承，多继承，多态，魔术方法，类装饰器，访问控制，常用基类
+ [collections模块/数据结构](./chapter5/collections.md)
+ [logging日志模块标准调用](./chapter5/logging.md)
+ 常见数据结构的使用
+ 编写高质量代码
+ 异步任务队列Celery使用

### 待启动
+ 大数据展示/实时监控系统页面展示
+ chapter6 编程思想/优化方向
    + 微服务架构【腾讯云tsf】
    + 解耦合/为什么需要封装api

