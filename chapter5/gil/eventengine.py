import queue
import threading
import time
import random


def producer(name, que):
    while True:
        if que.qsize() < 3:
            que.put('baozi')
            print('%s 做了一个包子' % name)
        else:
            print('还有三个包子')
        time.sleep(random.randrange(3))


def consumer(name, que):
    while True:
        try:
            que.get_nowait()
            print('%s 拿到一个包子' % name)
        except Exception:
            print('没有包子了')
        time.sleep(random.randrange(2))


if __name__ == "__main__":
    q = queue.Queue()
    p1 = threading.Thread(target=producer, args=['chef1', q])
    p2 = threading.Thread(target=producer, args=['chef2', q])
    p3 = threading.Thread(target=producer, args=['chef3', q])
    p1.start()
    p2.start()
    p3.start()

    c1 = threading.Thread(target=consumer, args=['大明', q])
    c2 = threading.Thread(target=consumer, args=['小红', q])
    c1.start()
    c2.start()

    consumer("小偷1", q)
    consumer("并没有机会偷包子的小偷2。。。。。。。。。。。。。。。。。", q)

# 多线程可以独立运行， 事件队列是线程之间传递信息的一种方式。
# 使用事件队列在线程之间传递信息的好处是并发（高效率）和解耦。
"""
会发现：
1. chef1、chef2、chef3 会一直生产包子  说明，p1、p2、p3并行
2. 大明、小红、小偷1/小偷2 均有机会拿到包子  说明，c1、c2，和小偷1或小偷2其中一个并行
3. 小偷1、小偷2谁先在前，谁就有机会拿到包子  说明，小偷1、小偷2不是并行，主线程和子线程会并行
"""
