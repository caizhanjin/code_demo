# 一篇搞定！Django+vue服务器部署

### 安装git（拉取代码）
```
# 查看是否已经安装
rpm -qa|grep git

# 安装git
yum install git

# 拉取代码：参考工具git的使用
git config --global user.name "your name"         # 你的名字
git config --global user.email "your email ad"    # 你的邮箱
ssh-keygen -t rsa -C "git@email.com"              # 你的邮箱，获取ssh密钥
cat ~/.ssh/id_rsa.pub                             # 查询密钥，并在远端仓库添加ssh

git init 
git remote add origin "git ssh ad"                # 远端ssh地址
git pull origin master
git branch master                                 # 创建本地分支
git branch --set-upstream-to=origin/master master # 绑定分支
```

### 安装oracle客户端（不用oracle则省略）
```
# 下载Linux版本客户端
http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html

# 使用rpm，下载后得到：
 oracle-instantclient11.2-basic-11.2.0.4.0-1.x86_64.rpm
 oracle-instantclient11.2-sqlplus-11.2.0.4.0-1.x86_64.rpm

# 安装
rpm -ivh oracle-instantclient-*.rpm

# 设置环境变量：vim /etc/profile 中添加内容
export ORACLE_HOME=/usr/lib/oracle/11.2/client64
export ORACLE_BASE=/usr/lib/oracle/11.2
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:$LD_LIBRARY_PATH
export PATH=$ORACLE_HOME/bin:$PATH
export NLS_LANG="AMERICAN_AMERICA.AL32UTF8"
export NLS_DATE_FORMAT="YYYY-MM-DD HH24:MI:SS"
export NLS_TIMESTAMP_FORMAT="YYYY-MM-DD HH24:MI:SS"

# 如果是ubuntu可能会缺少libaio，需要安装
sudo apt-get install libaio1 libaio-dev

# 文件立即生效
source /etc/profile
```

### 安装Python3.7和pip3（后端运行环境）
该步为了配置后端环境。
前端提前在开发环境`npm run build`好。

```
# 安装Python3和Pip3依赖包（如果缺少什么，就继续安装什么）
yum -y install gcc gcc-c++ openssl-devel libffi-devel zlib-devel bzip2-devel ncurses-devel sqlite-devel  \
    readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel

# 下载安装Python3和Pip3
# 若无wget则：yum -y install wget
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
tar -zxf Python-3.7.0.tgz
cd Python-3.7.0

./configure --prefix=/usr/local/python3 --enable-optimizations
make && sudo make install

# 添加运行文件到PATH（并存python2）
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3

# 升级pip3到最新版本
pip3 install --upgrade pip

# 在 开发环境！！！ 生成项目依赖包
pip freeze > requirements.txt

# 安装项目依赖包
pip3 install -r requirements.txt
```

到该步项目，应该能跑起来了。到后端项目目录：
```
python manage.py runserver
```

### 安装和部署uwsgi
安装
```
# 会安装到/usr/local/python3/bin/下
pip3 install uwsgi
ln -s /usr/local/python3/bin/uwsgi /usr/bin/uwsgi
```

部署，在项目的根目录下创建文件夹uwsgi（也可以在其他位置，注意底下对应路径同步更新就行，这里为了方便同步代码），
在文件夹uwsgi下创建配置文件文件 uwsgi.ini，内容如下：
```
[uwsgi]
# 项目目录
chdir=/root/zhanjinblog/zhanjinblog_api
# 指定项目的application，djangoBS为项目名
module=djangoBS.wsgi:application
# 指定sock的文件路径
socket=/root/zhanjinblog/zhanjinblog_api/uwsgi/uwsgi.sock
# 进程个数
workers=5
pidfile=/root/zhanjinblog/zhanjinblog_api/uwsgi/uwsgi.pid
# 指定IP端口
http=:9090
# 指定静态文件
static-map=/static=static
#项目中wsgi.py文件的目录，相对于项目目录，djangoBS为项目名
wsgi-file=djangoBS/wsgi.py
# 启动uwsgi的用户名和用户组
uid=root
gid=root
# 启用主进程
master=true
# 自动移除unix Socket和pid文件当服务停止的时候
vacuum=true
# 序列化接受的内容，如果可能的话
thunder-lock=true
# 启用线程
enable-threads=true
# 设置自中断时间
harakiri=30
# 设置缓冲
post-buffering=4096
# 设置日志目录,设置后台启动
daemonize=/root/zhanjinblog/zhanjinblog_api/uwsgi/uwsgi.log
```

运行配置文件，托管django服务
```
uwsgi --ini uwsgi.ini
```

开放端口
```
systemctl status firewalld                        # 查看防火墙的状态
systemctl start firewalld                         # 开启防火墙（建议开启）
systemctl stop firewalld                          # 停止防火墙
firewall-cmd --list-all                           # 查看防火墙端口号情况
firewall-cmd --query-port=9090/tcp                # 查看端口是否开放
firewall-cmd --add-port=9090/tcp --permanent      # 开放端口
firewall-cmd --reload                             # 重载配置
```

这时，应该就能访问成功了：`http://ip:9090`

### 安装和部署Nginx
安装nginx
```
sudo su  # 如果不是root

# 安装EPEL，EPEL 仓库中有 Nginx 的安装包
yum install epel-release

# 安装 Nginx
yum install nginx

# 设置 Nginx 开机启动
sudo systemctl enable nginx

service nginx start
# 这时访问，可以看到欢迎页： http://ip
```
nginx常用命令：
```
service nginx start  # 启动
service nginx stop  # 停止
service nginx restart # 重启，修改配置一般需要重启
service nginx status # 查看状态
nginx -t # 检查配置文件是否有误
```
可能会出现问题以及解决方案
```
# 修改配置文件，位置：/etc/nginx/nginx.conf
user nginx;  >> user root; # 解决权限问题
# 以及注释以下内容，不然引用/etc/nginx/conf.d/*.conf配置文件时，80端口会失效
server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  _;
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;
        location / {
        }

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
}

# 防火墙：打开 80（HTTP）和 443（HTTPS）端口
firewall-cmd --list-all  # 查看防火墙
firewall-cmd --permanent --zone=public --add-service=http
firewall-cmd --permanent --zone=public --add-service=https
firewall-cmd --reload

# 如果出现80端口占用
# netstat -ntpl 查看端口
# kill 7777[进程号码] 杀死进程

# systemctl status nginx.service时可能会出现下面错误
# nginx Failed to read PID from file /run/nginx.pid: Invalid argument
mkdir -p /etc/systemd/system/nginx.service.d
printf "[Service]\nExecStartPost=/bin/sleep 0.1\n" > /etc/systemd/system/nginx.service.d/override.conf
systemctl daemon-reload
systemctl restart nginx.service

# 出现：403 Forbidden错误
# 执行 setenforce 0设置SELinux 成为permissive模式
```

开始配置vue服务器
```
# 复制前端文件到服务器
scp -r /e/TDMS/tdms_vue/dist/* root@192.168.99.101:/root/tdms/vue

# 用户自定义配置文件一般放在/etc/nginx/conf.d，主配置文件是 /etc/nginx/nginx.conf会自动引入
# 文件名必须符合 *.conf
# 配置文件示例：

server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  _;
      
        # 注意：如果启用子域名，打包文件时，静态文件需使用相对路径
        location /h5 {             
             alias /root/ecms/h5/unpackage/dist/build/h5;
             try_files $uri $uri/ /h5/index.html;
             index index.html;
        }

        location / {
                root /root/ecms/web;
                try_files $uri $uri/ @router;
                index index.html;
        } 

        location @router {
                rewrite ^.*$ /index.html last;
        }

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
}
```

### uwsgi结合nginx部署django后台
该步是最后一步了，前提是上面uwsgi和nginx先部署好。
然后在前面nginx的/etc/nginx/conf.d/*.conf中加上以下内容，
'service nginx restart'重启nginx即可。
```
server{
        listen 8000;
        server_name localhost;
        charset utf-8;

        access_log /var/log/nginx/access.log;
        error_page 404 /404.html;
        error_page 500 502 503 504 /50x.html;

        client_max_body_size 100M;

        location / {
                include uwsgi_params;
                uwsgi_connect_timeout 30;
                uwsgi_pass unix:/root/tdms/uwsgi/uwsgi.sock;
        }

        location /static/ {
                alias /root/tdms/tdms-python/tdms/static/;
        }
}
```