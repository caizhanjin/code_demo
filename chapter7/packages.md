
## pip
``` 
# 升级
pip install --upgrade pip

```
+ pip包编译安装
```
# 到https://pypi.org/中下载Source包scipy-1.4.1.tar.gz
# rz 导入
rz
# 解压
tar -xvjf scipy-1.4.1.tar.gz
# 进入压缩包
cd scipy-1.4.1
# 安装
python3 setup.py
# 添加命令别名-不是每个都需要
vim ~/.bashrc
# 写入 
alias scrapy='/usr/local/python3/bin/scrapy'

source ~/.bashrc
```

## 环境管理
+ 为了避免与现有环境冲突，可以创建自个用户，编译安装所需环境到该用户目录下，然后在用户.bashrc中添加别名
``` 
# 位置于安装包目录下，/home/root/python3为安装路径
./configure --prefix='/home/nginx/python3'

# 命令起别名：
vim ~/.bashrc
alias python3='/home/root/python3/bin/python3.6'
alias pip3='/home/root/python3/bin/pip3'

# 立刻失效
source ~/.bashrc
```


