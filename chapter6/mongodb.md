# mongodb安装和使用

## 安装
``` 
# 写入源
vim /etc/yum.repos.d/mongodb-org-3.6.repo

[mongodb-org-3.6]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.6/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.6.asc

# 加载、安装
yum clean all
yum -y install mongodb-org

# 修改配置，便于工具连接
vim /etc/mongod.conf
# >>
net:
  port: 27017
  bindIp: 0.0.0.0  # Listen to local interface only, comment to listen on all interfaces.

# 重启服务
service mongod restart
```

## 连接
使用NoSQL Manager。注意防火墙打开对应端口（默认：27017）

