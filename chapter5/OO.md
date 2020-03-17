# 深入面向对象

## 类属性定义和方法定义

```
class Programer(object):

    # 直接在类里定义，该类的对象都会具有该属性
    sex = "male"

    def __init__(self, name, age, height, weight):
        # 公开属性
        self.name = name
        self.age = age

        # 私有属性
        self._height = height  # 保护类型只能允许其本身与子类进行访问
        self.__weight = weight  # 私有类型(private)的变量, 只允许类本身进行访问，object._className__attrName（ 对象名._类名__私有属性名 ）访问属性

    def get_weight(self):
        return self.__weight

    # 定义类方法，和属性类似
    def add(self):
        pass

    def _minus(self):
        pass

    def __multiply(self):
        pass

    # 伪属性，负责把一个方法变成一个属性调用，方便加检查参数等逻辑，类似实现get,set方法
    #【默认是可读，可写加上@birth.setter】
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        self._width = new_width

    # @staticmethod class中静态方法，无需实例化也可调用，在类当中直接调用即可
    @staticmethod
    def log_msg(msg):
        print(msg)

    # @classmethod 能调用类属性，但不能调用实例属性，写法和正常的类方法一致
    # 比静态方法多的是能调用类属性
    @classmethod
    def say_hi(cls):
        cls.log_msg("Hi.")

```

+ 子类调用父类的方法
```
# 某一方法
super(ReturnStockView, self).create(self, request, *args, **kwargs)

# 所有，在__init__中
    def __init__(self, cta_engine, strategy_name, vt_symbol, setting):
        """"""
        super().__init__(cta_engine, strategy_name, vt_symbol, setting)
        self.bg = BarGenerator(self.on_bar)
        self.am = ArrayManager()
```

## 析构函数
## 魔术方法
## 常用基类
+ object 基类：不继承其他类时继承
+ ABC : 抽象类 https://www.jianshu.com/p/09c41c512cc4
+ Enum : 枚举类 https://www.jianshu.com/p/29fd0aa370fd

