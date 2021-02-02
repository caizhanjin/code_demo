# -*- coding:utf8 -*-
"""
@author :  caizhanjin
@create : 2020/3/21
@description : 
"""


class Node(object):
    """单链表的节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleList(object):
    """单链表
    is_empty() 链表是否为空
    length() 链表长度
    travel() 遍历整个链表
    add(item) 链表头部添加元素
    append(item) 链表尾部添加元素
    insert(pos, item) 指定位置添加元素
    remove(item) 删除节点
    search(item) 查找节点是否存在
    """

    def __init__(self, _node=None):
        self.__head = _node

    def is_entry(self):
        """判断是否为空"""
        return self.__head is None

    def length(self):
        """链表的长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next

    def add(self, item):
        """头部添加元素"""
        _node = Node(item)
        _node.next = self.__head
        self.__head = _node

    def append(self, item):
        """尾部添加元素"""
        _node = Node(item)

        if self.is_entry():
            self.__head = _node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = _node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next

            _node = Node(item)
            _node.next = pre.next
            pre.next = _node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == item:
                # 先判断子节点是否是头结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True, cur
            else:
                cur = cur.next

        return False, None


if __name__ == "__main__":
    node = Node(10)
    s2 = SingleList(node)

    s2.add(12)
    s2.append(14)
    s2.append(15)
    s2.travel()

    is_exit, node = s2.search(14)

    pass
