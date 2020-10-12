# Nginx/uwsgi配置文件示例

## uwsgi
``` 
[uwsgi]
chdir=/root/tdms/tdms_api/tdms
module=tdms.wsgi:application
socket=/root/tdms/uwsgi/uwsgi.sock
#workers=5
pidfile=/root/tdms/uwsgi/uwsgi.pid
http=:8000
processes=8
static-map=/static=/root/tdms/tdms_api/tdms/static
wsgi-file=tdms/wsgi.py
uid=root
gid=root
master=true
vacuum=true
thunder-lock=true
enable-threads=true
harakiri=600
http-timeout=600
socket-timeout=600
post-buffering=10240
daemonize=/root/tdms/uwsgi/uwsgi.log
virtualenv=/root/anaconda3/envs/tdms
```

## Nginx web
+ 示例1：
``` 
server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  _;

        location /BWC {
             alias /root/ecms/web/BWC;
             try_files $uri $uri/ /BWC/index.html;
             index index.html;
        }
      
        location /h5 {             
             alias /root/ecms/web/h5;
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
+ 示例2：
``` 
server {
	listen 443 ssl;
    server_name tdmsapi.sunwoda.com;
    access_log /var/log/nginx/access.log main;  # Nginx日志配置
    charset utf-8;  # Nginx编码
    gzip_types text/plain application/x-javascript text/css text/javascript application/x-httpd-php application/json text/json image/jpeg image/gif image/png application/octet-stream;
	# 支持压缩的类型
	large_client_header_buffers 4 16k;     # 读取大型客户端请求头的缓冲区的最大数量和大小
	client_body_buffer_size 128k;  #请求主体的缓冲区大小
	
	client_max_body_size 300m;
    error_page 404 /404.html;
	# 错误页面
    error_page 500 502 503 504 /50x.html;
	ssl_certificate  /etc/nginx/ssl/sunwoda.crt;
	ssl_certificate_key  /etc/nginx/ssl/sunwoda.key;
	ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
	ssl_session_timeout  5m;
	ssl_ciphers 'AES128+EECDH:AES128+EDH';
	#ssl_ciphers  HIGH:!aNULL:!MD5;
	ssl_prefer_server_ciphers  on;
	# 接入监控
	location /status{                                                                                                                                                                                 
		vhost_traffic_status_display;
		vhost_traffic_status_display_format html;
	 }

	# 指定项目路径uwsgi
    location ~* /tests|/oa|/cycle|/received|/receive|/blob|/review|/errors{
		proxy_pass http://10.210.88.44:8000;
		proxy_connect_timeout   600; #单位为秒		
		proxy_send_timeout      600;
		proxy_read_timeout      600;
		proxy_set_header Host $host;		
		proxy_set_header X-Real-IP $remote_addr;		
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;		
		proxy_http_version 1.1;		
		proxy_set_header Upgrade $http_upgrade;		
		proxy_set_header Connection "upgrade";
	}

	# 分发到其他服务器
    location ~* /admin|/api-auth|/login|/automatism|/abnormal|/analyze|/calibration|/flow{
		proxy_pass http://172.30.201.122:8000;
		proxy_connect_timeout   600; #单位为秒
		proxy_send_timeout      600;
		proxy_read_timeout      600;
		proxy_set_header Host $host;
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_http_version 1.1;
		proxy_set_header Upgrade $http_upgrade;
		proxy_set_header Connection "upgrade";
	}

	# 指定静态文件路径
    location /static/ {
        alias /appdata/tdms/tdms/static/;
        index index.html index.htm;
    }

	location /supplier {
        # 设置连接uWSGI超时时间
		include uwsgi_params;
		uwsgi_send_timeout 300;        # 指定向uWSGI传送请求的超时时间，完成握手后向uWSGI传送请求的超时时间。
        uwsgi_connect_timeout 300;   # 指定连接到后端uWSGI的超时时间。
		uwsgi_read_timeout 300;        # 指定接收uWSGI应答的超时时间，完成握手后接收uWSGI应答的超时时间。
		
        uwsgi_pass unix:/etc/uwsgi/supplier_uwsgi.sock;	
		uwsgi_ignore_client_abort on;  # 服务器不会主动断开与客户端的连接
	}
}
```

## Nginx api
``` 
# 容错机制
proxy_next_upstream error;
server {
        listen 9000;
        server_name 10.210.88.31;
        access_log  /root/ecms/nginx/access_log.log;
        error_log  /root/ecms/nginx/error_log.log;
        charset utf-8;
        gzip_types text/plain application/x-javascript text/css text/javascript application/x-httpd-php application/json text/json image/jpeg image/gif image/png application/octet-stream;
        client_max_body_size 120m;
        error_page 404 /404.html;
        error_page 500 502 503 504 /50x.html;

	# 帆软报表
	location ^~/WebReport {
	    proxy_pass http://10.210.88.31:8080/WebReport/;
	}

        location /static/ {
            alias /root/ecms/ecms_api/static/;
            index index.html index.htm;
        }

        location / {
            include uwsgi_params;
            uwsgi_send_timeout 600;
            uwsgi_connect_timeout 600;
            uwsgi_read_timeout 600;
	    uwsgi_pass unix:/root/ecms/uwsgi/uwsgi.sock;
       }
}
```


