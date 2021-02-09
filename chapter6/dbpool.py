# -*- coding:utf8 -*-
"""
@author :  caizhanjin
@create : 2021/2/5
@description : 各类数据库连接池的实现
"""

import importlib
import threading
import time
import redis
from DBUtils.PooledDB import PooledDB
import cx_Oracle
from redis import ConnectionPool, StrictRedis

from django_redis import get_redis_connection

# from aps.settings import DATABASES
# from DBUtils.PooledDB import PooledDB
import pickle
import json


class OraclePool(object):
    """
    oracle数据库连接池管理
    """
    _instance_lock = threading.Lock()
    _pool = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(OraclePool, "_instance"):
            with OraclePool._instance_lock:
                if not hasattr(OraclePool, "_instance"):
                    OraclePool._instance = object.__new__(cls)

        return OraclePool._instance

    def get_connect(self):
        if self._pool is None:
            config = {
                'user': "",
                'password': "",
            }
            db_creator = importlib.import_module("cx_Oracle")

            self._pool = PooledDB(db_creator, maxcached=20, maxconnections=100, maxusage=None, **config)

        return self._pool.connection()

    def execute_query(self, sql, args=()):
        """
        查询语句
        """
        result = ()
        conn = self.get_connect()
        cur = conn.cursor()

        try:
            cur.execute(sql, args)
            result = self.dict_fetch_all(cur)
        except Exception as e:
            print('异常信息:' + str(e))

        cur.close()
        conn.close()
        return result

    def execute_iud(self, sql, args=()):
        """
        执行增删改语句
        """
        conn = self.get_connect()
        cur = conn.cursor()
        count = 0
        try:
            count = cur.execute(sql, args)
            conn.commit()
        except Exception as e:
            print('异常信息:' + str(e))
            conn.rollback()
        cur.close()
        conn.close()
        return count

    def execute_many_iud(self, sql, args):
        """
        批量执行增删改语句
        :param args:参数,内部元组或列表大小与sql语句中参数数量一致
        """
        conn = self.get_connect()
        cur = conn.cursor()
        count = 0
        try:
            count = cur.executemany(sql, args)
            conn.commit()
        except Exception as e:
            print('异常信息:' + str(e))
            conn.rollback()
        cur.close()
        conn.close()
        return count

    @staticmethod
    def dict_fetch_all(cursor):
        """
        将游标返回的结果保存到一个字典对象中
        """
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]

    def exchang_key(self, dicts):
        """
        更新数据库中所有表的 keyword 字段的值
        [
            {
             "TABLE_NAME_VALUE":"xxx",
             ":KEYWORD":"xxx",
             "KEY_VALUE":"xxx"
            }
        ]
        :param keyword:
        :param value:
        :return:
        """
        for item in dicts:
            sql = "update {TABLE_NAME_VALUE} set {KEYWORD} = {KEY_VALUE}".format(**item)
            self.execute_iud(sql)


# class SQLiteDBPool(object):
#     """
#         oracle 数据库连接池管理
#     """
#
#     def __init__(self):
#         """
#             初始化 数据库连接池
#         """
#         self.__db_type = 'sqlite'
#         config = {
#             'database': DATABASES['default']['NAME'],
#             'check_same_thread': False
#         }
#         db_creator = importlib.import_module("sqlite3")
#         # mincached：池中的初始空闲连接数
#         # maxcached：池中的最大空闲连接数
#         # maxshared：允许的最大共享连接数
#         # maxconnections：通常允许的最大连接数
#         # maxusage：单个连接的最大重用次数
#         self.__pool = PooledDB(db_creator, maxcached=1, maxconnections=100, maxusage=None, **config)
#
#     def __call__(self, logger):
#         self.__logger = logger
#         return self
#
#     @staticmethod
#     def instance():
#         """
#             单例模式
#         :return:
#         """
#         if not hasattr(SQLiteDBPool, "_instance"):
#             SQLiteDBPool._instance = SQLiteDBPool()
#         return SQLiteDBPool._instance
#
#
#     def execute_query(self, sql, args=()):
#         """
#             查询语句
#         """
#         result = ()
#         conn = self.__pool.connection()
#         cur = conn.cursor()
#         try:
#             cur.execute(sql, args)
#             result = self.dictfetchall(cur)
#         except Exception as e:
#             self.__logger.error(e)
#             print('异常信息:' + str(e))
#         cur.close()
#         conn.close()
#         return result
#
#     def execute_iud(self, sql, args=()):
#         """
#             执行增删改语句
#         """
#         conn = self.__pool.connection()
#         cur = conn.cursor()
#         count = 0
#         try:
#             count = cur.execute(sql, args)
#             conn.commit()
#         except Exception as e:
#             self.__logger.error(e)
#             print('异常信息:' + str(e))
#             conn.rollback()
#         cur.close()
#         conn.close()
#         return count
#
#     def execute_many_iud(self, sql, args):
#         """
#         批量执行增删改语句
#         :param args:参数,内部元组或列表大小与sql语句中参数数量一致
#         """
#         conn = self.__pool.connection()
#         cur = conn.cursor()
#         count = 0
#         try:
#             count = cur.executemany(sql, args)
#             conn.commit()
#         except Exception as e:
#             self.__logger.error(e)
#             print('异常信息:' + str(e))
#             conn.rollback()
#         cur.close()
#         conn.close()
#         return count
#
#     def dictfetchall(self, cursor):
#         "将游标返回的结果保存到一个字典对象中"
#         desc = cursor.description
#         return [
#             dict(zip([col[0] for col in desc], row))
#             for row in cursor.fetchall()
#         ]


class RedisPool(object):
    """
    rides连接池实现
    """
    _instance_lock = threading.Lock()
    _pool = None

    def __init__(self):
        # time.sleep(2)
        pass

    def get_connect(self):
        if self._pool is None:
            self._pool = ConnectionPool(
                host="127.0.0.1",
                port=6379,
                db=0,
                max_connections=5,
            )

        return redis.Redis(connection_pool=self._pool)

    def __new__(cls, *args, **kwargs):
        if not hasattr(RedisPool, "_instance"):
            with RedisPool._instance_lock:
                if not hasattr(RedisPool, "_instance"):
                    RedisPool._instance = object.__new__(cls)

        return RedisPool._instance


# redis_pool = RedisDBPool.instance()
# oracle_pool = OracleDBPool.instance()
# sqlite_pool = SQLiteDBPool.instance()

if __name__ == "__main__":

    # Redis测试
    def task(arg):
        redis_pool = RedisPool()
        connect = redis_pool.get_connect()
        print(redis_pool)
        print(connect)

    for i in range(10):
        t = threading.Thread(target=task, args=(i,))
        t.start()
        # time.sleep(2)


