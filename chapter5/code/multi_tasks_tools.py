# -*- coding:utf8 -*-
"""
@author :  caizhanjin
@create : 2020/3/21
@description : 并发处理任务工具类
"""
import math
import multiprocessing
import random
import threading
import time
import queue


def split_lists(wait_list, split_number):
    """
    切分有序任务列表，典型用例均匀分布耗时任务
    """
    list_length = len(wait_list)
    cycle_number = math.ceil(list_length / split_number)
    split_list = [[] for i in range(split_number)]
    for cycle in range(cycle_number):
        for i in range(split_number):
            key = cycle * split_number + i
            if key == list_length:
                break
            split_list[i].append(wait_list[cycle * split_number + i])

    return split_list


def multi_processing_tools(task_func, args_list):
    """多进程工具，会和任务一样的进程数"""
    cpu_counts = multiprocessing.cpu_count()
    processing_list = []
    for args in args_list:
        processing_list.append(
            multiprocessing.Process(target=task_func, args=args)
        )

    # 启动任务
    print(f"工作站CPU核数为：{cpu_counts}，开启了 {len(args_list)} 个进程工作...")
    [i.start() for i in processing_list]
    return processing_list


def multi_processing_pools(tasks_list, processing_number=None):
    """多进程工具，使用进程池，启动指定数量的进程数：优先推进该方法"""
    cpu_counts = multiprocessing.cpu_count()
    pools_number = processing_number if processing_number else cpu_counts
    pools = multiprocessing.Pool(processes=pools_number)

    processing_list = []
    for (task_func, args) in tasks_list:
        processing_list.append(
            pools.apply_async(task_func, args=args)
        )

    # 启动任务
    print(f"工作站CPU核数为：{cpu_counts}，开启了 {pools_number} 个进程工作...")
    [i.get() for i in processing_list]
    return processing_list


def multi_threading_tools(task_func, args_list):
    """
    多线程工具：大量IO等待类任务时使用
    """
    threading_list = []
    for args in args_list:
        threading_list.append(
            threading.Thread(target=task_func, args=args)
        )

    # 启动任务
    [i.start() for i in threading_list]

    return threading_list


def producer(name, que):
    """生产者"""
    while True:
        if que.qsize() < 3:
            que.put([1, 2, 4])
            print('%s 做了一个包子' % name)
        else:
            print('还有三个包子')
        time.sleep(random.randrange(3))


def consumer(name, que):
    """消费者"""
    while True:
        data = que.get()
        print(f"{name} 拿到包子")


def dead_loop(name):
    print(f"{name} 开启...")
    while True:
        pass


if __name__ == '__main__':
    # 切分任务，分配指定数量工作时使用
    # tasks_orderList = [
    #     1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2,
    #     3, 4, 5,
    #     1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2,
    #     3, 4, 5, 9
    # ]
    # result = split_lists(tasks_orderList, 5)

    """测试多线程"""
    queue_cursor = queue.Queue()
    result1 = ["小红"]
    args_list1 = [(i, queue_cursor) for i in result1]
    result2 = ["消费者1", "消费者2", "消费者3", "消费者4"]
    args_list2 = [(i, queue_cursor) for i in result2]
    multi_threading_tools(producer, args_list1)
    multi_threading_tools(consumer, args_list2)

    """
    测试多进程
    # 注意队列queue.Queue据有线程锁，只能用于多线程
    # 多进程使用multiprocessing.Queue或multiprocessing.Manager[进程池使用]
    """
    # 使用进程池 通讯用 multiprocessing.Manager：该方法无需守护进程
    manager = multiprocessing.Manager()
    queue_cursor = manager.Queue()
    result1 = ["小红", "小明"]
    task_list1 = [
        (producer, (i, queue_cursor))
        for i in result1
    ]
    result2 = ["消费者1", "消费者2", "消费者3", "消费者4"]
    task_list2 = [
        (consumer, (i, queue_cursor))
        for i in result2
    ]
    all_task = task_list1 + task_list2
    multi_processing_pools(all_task, 5)

    # 根据任务数量配置进程数 通讯用 multiprocessing.Queue：该方法需要使用守护进程
    queue_cursor = multiprocessing.Queue()
    result1 = ["小红", "小明"]
    args_list1 = [(i, queue_cursor) for i in result1]
    result2 = ["消费者1", "消费者2", "消费者3", "消费者4"]
    args_list2 = [(i, queue_cursor) for i in result2]
    multi_processing_tools(producer, args_list1)
    multi_processing_tools(consumer, args_list2)
    # 守护进程，防止主程序关闭，中断所有进程
    while True:
        time.sleep(5)

    """测试：100%占满CPU"""
    task_list = [
        (dead_loop, (f"进程{i + 1}", ))
        for i in range(10)
    ]
    multi_processing_pools(task_list)
