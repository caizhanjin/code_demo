# linux

## 远程
``` 
scp 

# 
rz 导入
sz 导出
```

## .bashrc
bash在每次启动时都会加载.bashrc文件的内容。每个用户的home目录都有这个shell脚本，用来存储并加载你的终端配置和环境变量。
``` 
# 命令起别名：
alias rm='rm -i'
alias python3='/home/root/python3/bin/python3.6'
alias pip3='/home/root/python3/bin/pip3'

# 立刻失效
source ~/.bashrc
```

## 编译安装
``` 
# 位置于安装包目录下，/home/root/python3为安装路径
./configure --prefix='/home/root/python3'

```

