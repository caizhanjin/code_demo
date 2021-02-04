# 单例模式的几种实现方式
[参考/详细解释](https://www.cnblogs.com/huchong/p/8244279.html#_lab2_1_3)
### 1.使用模块
该方式是线程安全的。
**mysingleton.py**
``` 
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()
```
使用
``` 
from a import singleton
```

## 2.使用装饰器
``` 
def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton

@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x

a1 = A(2)
a2 = A(3)
```

## 3.基于__new__方法实现（推荐使用，方便）
为了保证线程安全需要在内部加入锁
``` 
import threading
class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass
        # 如果不加锁，这里有io操作，多个会出现多个实例，
        # 创建对象有延迟时，多线程“并发”就会创建多个对象，所以要加锁
        # 未加锁部分并发执行,加锁部分串行执行,速度降低,但是保证了数据安全

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)  
        return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1,obj2)

def task(arg):
    obj = Singleton()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()
```



