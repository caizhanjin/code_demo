# 使用Tornado构建RESTful微服务

### 什么是RESTful？
Representational State Transfer 表征状态转移
资源（Resources），表现层（Representation），状态转化（State Transfer）

### RESTful风格
+ 资源（Resources）：使用URL指向的一个实体
+ 表现层（Representation）：资源的表现形式，比如图片、HTML文本等
+ 状态转化（State Transfer）：GET、POST、PUT、DELETE这些HTTP动词来操作资源，可与后端的增删改查对应

### 常用HTTP动词
GET 获取/POST 新建/PUT 更新/DELETE 删除
幂等性：GET/PUT/DELETE 是幂等操作。幂等指的是无论一次还是多次操作具有一样的副作用

### RESTful Api示例：
|HTTP方法|URL| 动作| 
|:---:|:---:|:---:|
|GET|http://[hostname]/api/users|检索用户列表|
|GET|http://[hostname]/api/users/[user_id]|检索单个用户|
|POST|http://[hostname]/api/users|创建新用户|
|PUT|http://[hostname]/api/users/[user_id]|更新用户信息|
|DELETE|http://[hostname]/api/users/[user_id]|删除用户|


### [代码示例](./demo1_restful/README.md)

