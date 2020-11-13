# git
## 情景使用
### 配置用户参数
```
git config --global user.name "your name"         # 你的名字
git config --global user.email "your email ad"    # 你的邮箱
ssh-keygen -t rsa -C "git@email.com"              # 你的邮箱，获取ssh密钥
cat ~/.ssh/id_rsa.pub                             # 查询密钥
```
获取得到公钥之后，在网页端添加ssh

### 空白项目关联(远端)
```
# 本地没有文件
echo  "# your title" >> README.md
git init 
git add .
git commit -m "first commit"
git remote add "git ssh ad"  # 远端ssh地址
git push -u origin master


# 本地已有文件/仓库
# [git init]
git remote add "git ssh ad"  # 远端ssh地址
git push -u origin master
```

### 已有文件项目关联(远端)
```
git init 
git remote add origin "git ssh ad"                # 远端ssh地址
git pull origin master
git branch master                                 # 创建本地分支
git branch --set-upstream-to=origin/master master # 绑定分支
```
### fork仓库与作者同步
思路，创建多个远端仓库，同步
```
git remote add upstream "git ssh ad"    # 添加作者remote地址
git fetch upstream                      # 同步最新代码
git merge upstream/master               # 合并本地代码
git push
```

### 删除远端文件夹并忽略
```
# 预览：-n参数不会删除文件，只是预览
git rm -r -n --cached 文件/文件夹名称 

# 确认后删除
git rm -r --cached 文件/文件夹名称

# 提交、推送到远端
git commit -m "提交说明"
git push origin master

# 修改本地 .gitignore 文件 并提交
git commit -m "提交说明"
git push origin master
```

## 基本命令
```
git clone http://...            克隆仓库到本地
git push origin master          推送到远程的origin/master分支上
git push origin lichen:lichen   将本地新建推送到远端并创建对应分支

git status                    了解当前状态
git checkout -- test.txt      丢弃工作区的修改
git reset HEAD test.txt       修改撤销掉（unstage），重新放回工作区
git diff test,txt             查看工作区和版本库里面文件的区别                  
git log                       查看提交日志
git log --pretty=oneline  

git reset --hard HEAD^        退回上一个版本
git reset --hard HEAD~100
git reset --hard [id]         回滚到具体某一个版本
git reflog                    版本历史记录，最近一个是当前的
git rm test.txt               删除一个文件


# 分支：
git branch                                      查看分支
git branch -a                                   查看所有分支，包括远端
git branch [name]                               创建分支
git checkout [name]                             切换分支
git chechout -b [name]                          创建并切换分支
git merge [name]                                合并某分支到当前分支
git merge --no-ff -m "[备注]" [branch name]     禁用Fast forward，合并
 
git branch -d [name]                            删除分支
git branch -D <name>                            强制删除[-d 删除失败时使用]

git log --graph --pretty=oneline --abbrev-commit 图解
git log --graph                                  查看分支合并情况
git rebase                                       把交叉转换成线，清晰
git stash                                        把当前的工作区的修改隐藏起来
git stash list                                   查看工作现场列表
git stash apply                                  恢复工作现场
git stash drop                                   删除工作现场
git stash pop                                    恢复并删除工作现场
git log -1                                       最后一次提交信息


# 协作：
git remote                                       查看远程仓库
git remote -v                                    查看远程仓库详细信息
git remote update origin --prune                 更新远程分支列表

git pull                                         获取最新的提交
git checkout -b branch-name origin/branch-name   在本地创建和远程分支对应的分支
git branch --set-upstream-to=origin/dev dev      建立本地分支和远程分支的关联 本地dev 和 远程origin/dev

git config --global alias.co checkout            给命令配置别名
```