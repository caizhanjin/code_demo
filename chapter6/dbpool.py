#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Author:   chenjh
# @DateTime: 2020-06-19 17:20
# @Software: PyCharm
# @File:     dbpool.py


import importlib

import cx_Oracle
from redis import ConnectionPool, StrictRedis

from django_redis import get_redis_connection

from aps.settings import DATABASES
from DBUtils.PooledDB import PooledDB
import pickle
import json

"""
    数据库连接池
"""

class OracleDBPool(object):
    """
        oracle 数据库连接池管理
    """

    def __init__(self):
        """
            初始化 数据库连接池
        """
        self.__db_type = 'oracle'
        config = {
            'user': DATABASES['default']['USER'],
            'password': DATABASES['default']['PASSWORD'],
            'dsn': "/".join(
                [":".join([DATABASES['default']['HOST'], DATABASES['default']['PORT']]), DATABASES['default']['NAME']])
            # 'dsn': DATABASES['default']['NAME']
        }
        db_creator = importlib.import_module("cx_Oracle")
        # mincached：池中的初始空闲连接数
        # maxcached：池中的最大空闲连接数
        # maxshared：允许的最大共享连接数
        # maxconnections：通常允许的最大连接数
        # maxusage：单个连接的最大重用次数
        self.__pool = PooledDB(db_creator, maxcached=20, maxconnections=100, maxusage=None, **config)

    def __call__(self, logger):
        self.__logger = logger
        return self

    @staticmethod
    def instance():
        """
            单例模式
        :return:
        """
        if not hasattr(OracleDBPool, "_instance"):
            OracleDBPool._instance = OracleDBPool()
        return OracleDBPool._instance


    def execute_query(self, sql, args=()):
        """
            查询语句
        """
        result = ()
        conn = self.__pool.connection()
        cur = conn.cursor()
        try:
            cur.execute(sql, args)
            result = self.dictfetchall(cur)
        except Exception as e:
            self.__logger.error(e)
            print('异常信息:' + str(e))
        cur.close()
        conn.close()
        return result

    def execute_iud(self, sql, args=()):
        """
            执行增删改语句
        """
        conn = self.__pool.connection()
        cur = conn.cursor()
        count = 0
        try:
            count = cur.execute(sql, args)
            conn.commit()
        except Exception as e:
            self.__logger.error(e)
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
        conn = self.__pool.connection()
        cur = conn.cursor()
        count = 0
        try:
            count = cur.executemany(sql, args)
            conn.commit()
        except Exception as e:
            self.__logger.error(e)
            print('异常信息:' + str(e))
            conn.rollback()
        cur.close()
        conn.close()
        return count

    def dictfetchall(self, cursor):
        "将游标返回的结果保存到一个字典对象中"
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





class SQLiteDBPool(object):
    """
        oracle 数据库连接池管理
    """

    def __init__(self):
        """
            初始化 数据库连接池
        """
        self.__db_type = 'sqlite'
        config = {
            'database': DATABASES['default']['NAME'],
            'check_same_thread': False
        }
        db_creator = importlib.import_module("sqlite3")
        # mincached：池中的初始空闲连接数
        # maxcached：池中的最大空闲连接数
        # maxshared：允许的最大共享连接数
        # maxconnections：通常允许的最大连接数
        # maxusage：单个连接的最大重用次数
        self.__pool = PooledDB(db_creator, maxcached=1, maxconnections=100, maxusage=None, **config)

    def __call__(self, logger):
        self.__logger = logger
        return self

    @staticmethod
    def instance():
        """
            单例模式
        :return:
        """
        if not hasattr(SQLiteDBPool, "_instance"):
            SQLiteDBPool._instance = SQLiteDBPool()
        return SQLiteDBPool._instance


    def execute_query(self, sql, args=()):
        """
            查询语句
        """
        result = ()
        conn = self.__pool.connection()
        cur = conn.cursor()
        try:
            cur.execute(sql, args)
            result = self.dictfetchall(cur)
        except Exception as e:
            self.__logger.error(e)
            print('异常信息:' + str(e))
        cur.close()
        conn.close()
        return result

    def execute_iud(self, sql, args=()):
        """
            执行增删改语句
        """
        conn = self.__pool.connection()
        cur = conn.cursor()
        count = 0
        try:
            count = cur.execute(sql, args)
            conn.commit()
        except Exception as e:
            self.__logger.error(e)
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
        conn = self.__pool.connection()
        cur = conn.cursor()
        count = 0
        try:
            count = cur.executemany(sql, args)
            conn.commit()
        except Exception as e:
            self.__logger.error(e)
            print('异常信息:' + str(e))
            conn.rollback()
        cur.close()
        conn.close()
        return count

    def dictfetchall(self, cursor):
        "将游标返回的结果保存到一个字典对象中"
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]



class RedisDBPool(object):
    """
        获取数据库连接池从redis中
    """

    def __init__(self):
        """
            设置redis连接池
        """
        self.redis = get_redis_connection('default')

    def __call__(self, logger):
        self.__logger = logger
        return self

    @staticmethod
    def instance():
        """
            单例模式
        :return:
        """
        if not hasattr(RedisDBPool, '_instance'):
            RedisDBPool._instance = RedisDBPool()
        return RedisDBPool._instance




redis_pool = RedisDBPool.instance()
oracle_pool = OracleDBPool.instance()
sqlite_pool = SQLiteDBPool.instance()