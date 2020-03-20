# 深入理解协程、线程、进程，GIL锁

## 理解
+ GIL锁：全局解释器锁，能保证同一时刻只有一个获得GIL的线程在运行，所以，python解析性语言只能利用单核多线程，多线程并发不是实际意义上的并发；
+ IO密集型：涉及到网络、磁盘IO(本地读写)等，如Web应用，CPU消耗很少，任务的大部分时间都在等待IO操作完成；
+ 计算密集型：需要做大量计算，消耗大量CPU资源；


结论：python 多线程不能充分利用多核cpu，在计算密集型代码多线程来回切换损耗资源，效率会变慢，但是在IO密集型中表现很好；

+ 多线程 >> IO密集型：Web应用、磁盘IO(本地读写)、爬虫
+ 多进程 >> 计算密集型：

## 多线程实现
[拓展](https://www.imooc.com/article/16198)
+ [理解多线程"并行"理解例子](./eventengine.py)
+ 基本实现
``` 
# 第一种方式，实例化 Thread
from threading import Thread
import time

def task(name):
    print("subthread is running....")
    time.sleep(random.randrange(2))

# t = Thread(target=task, kwargs={name='zhanjin',})
t1 = Thread(target=task, args=('zhanjin',))
t2 = Thread(target=task, args=('zhanjin',))

t1.start()
t2.start()

print('main is over....')

# 第二种方式，继承Thread类
from threading import Thread

class MyThread(Thread):
    def run(self):
        print("subthread is running....")

    def __init__(self, parameter1):
        Thread.__init__(self)
        self.parameter1 = parameter1

t = MyThread(parameter1)
t.start()
```

+ 线程之间传递信息：事件队列queue
``` 
import queue

q = queue.Queue()

q.put((1, 'a'))  # 存储
int_data, str_data = q.get()  # 提取，一次只提一条数据

```

## 多进程实现
+ 基本实现
``` 
from multiprocessing import Process
import os
import time

def run_proc(name):
    time.sleep(3)
    print ('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print ('Parent process %s.' % os.getpid())
    processes = []
    for i in range(5):
        p = Process(target=run_proc, args=('test',))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    print ('Process end.')
```

+ 使用pool进程池

[例子](./progress.py)
``` 
import multiprocessing

def run_func(test):
    pass


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    results = []
    for file_name in all_files:
        res = pool.apply_async(task, args=(x,))

    pool.close()
    pool.join()
```
