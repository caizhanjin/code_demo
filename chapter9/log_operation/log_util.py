"""
author：caizhanjin
date：2020/9/27
detail：log操作类
"""
import os
import time
from datetime import datetime

from utils.format_data import ReturnDataApi
import cx_Oracle
from django.conf import settings

DATABASES = settings.DATABASES["default"]
ECMS_CONN_STR = f"{DATABASES['USER']}/{DATABASES['PASSWORD']}@{DATABASES['HOST']}:{DATABASES['PORT']}/{DATABASES['NAME']}"
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


def is_valid_date(date_str):
    """判断是否是一个有效的日期字符串"""
    try:
        date_str = date_str.split(" ")[0]
        time.strptime(date_str, "%Y-%m-%d")
        return True
    except:
        return False


class LogOperation(object):
    """
    日志操作类

    管理系统中需要记录操作日志的地方：
    1. insert：在insert后，记录新增的数据
    2. update：记录update前后的数据
    3. delete：在delete前，记录删除前的数据

    日志操作类LogOperation主要方法：
    insert(table_name, table_id, operate_user_id)----新增
    update_before(table_name, table_id, operate_user_id)----更新前
    update_after(table_name, table_id, log_id)----更新后
    delete(table_name, table_id, operate_user_id)----删除
    recover_delete(log_id)----恢复删除
    select_log_info(log_id)----获取某log详情

    调用示例：
    from log.log_util import LogOperation
    log_operation = LogOperation()
    result, log_id, error_msg = log_operation.insert(
        table_name="ACTIVITY_DISCOUNTRECORD",
        table_id="1261",
        operate_user_id=1
    )

    @result：结果，True成功 False失败
    @log_id：对应的logID
    @error_msg：结果失败时，错误提示
    """

    def __init__(self):
        self.connection = None
        self.table_info_dict = {}

    def insert(self, table_name, table_id, operate_user_id, primary_name="id"):
        result, new_log_id, error_msg = self._insert(table_name, table_id, operate_user_id, primary_name, 1)

        return result, new_log_id, error_msg

    def update_before(self, table_name, table_id, operate_user_id, primary_name="id"):
        result, new_log_id, error_msg = self._insert(table_name, table_id, operate_user_id, primary_name, 2)

        return result, new_log_id, error_msg

    def update_after(self, table_name, table_id, log_id, primary_name="id"):
        cursor = self.get_cursor()
        try:
            table_info = self.get_table_info(table_name)

            # 查询当前记录数据
            key_value_list = self.get_row_value(table_info, table_name, primary_name, table_id)

            now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            update_sql_all = "BEGIN "
            index = 0
            for key in table_info["keys_list"]:
                key_name = "" if not key[0] else key[0]
                key_value = "" if not key_value_list[index] else key_value_list[index]

                update_sql_item = F"""
                UPDATE LOG_CONTENT SET 
                    CURRENT_VALUE='{key_value}',
                    UPDATE_TIME=to_date('{now_time}','yyyy-mm-dd hh24:mi:ss')
                WHERE OPERATE_ID='{log_id}' AND KEY_NAME='{key_name}';
                """
                index += 1
                update_sql_all += update_sql_item

            update_sql_all += "END;"
            cursor.execute(update_sql_all)

            self.connection.commit()
            cursor.close()
            return True, log_id, ""

        except Exception as error:
            cursor.close()
            return False, log_id, str(error)

    def delete(self, table_name, table_id, operate_user_id, primary_name="id"):
        result, new_log_id, error_msg = self._insert(table_name, table_id, operate_user_id, primary_name, 3)

        return result, new_log_id, error_msg

    def recover_delete(self, log_id, operate_user_id):
        """恢复删除（恢复操作只有删除类型有）"""
        now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor = self.get_cursor()
        try:
            log_info = self.get_log_info(log_id)
            if log_info["operate_type"] != 3:
                raise LookupError(f"Operate type is not delete!")
            if log_info["status"] != 1:
                raise LookupError(f"Operate status is not restorative state!")

            # 恢复原表数据
            insert_sql = f"""
            INSERT INTO {log_info['table_name']}({log_info['key_name_str']})
            VALUES ({log_info['key_value_str']})
            """
            cursor.execute(insert_sql)

            # 更新log状态
            update_sql = f"""
            UPDATE LOG_OPERATION SET 
                STATUS='2',
                UPDATE_USER={operate_user_id},
                UPDATE_TIME=to_date('{now_time}','yyyy-mm-dd hh24:mi:ss')
            WHERE ID='{log_id}'
            """
            cursor.execute(update_sql)

            self.connection.commit()
            cursor.close()
            return True, log_id, ""

        except Exception as error:
            cursor.close()
            return False, log_id, str(error) + "/数据是逻辑删除，无法从这恢复"

    def select_all(self):
        pass

    def select_table_logs(self, table_name):
        pass

    def select_log_info(self, log_id):

        return self.get_log_info(log_id)

    def _insert(self, table_name, table_id, operate_user_id, primary_name, operate_type):
        """新增新操作纪录(通用)"""
        cursor = self.get_cursor()
        try:
            table_info = self.get_table_info(table_name)

            # 查询当前记录数据
            key_value_list = self.get_row_value(table_info, table_name, primary_name, table_id)

            # 操作日志记录表添加记录
            now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            insert_sql = f"""
            INSERT INTO LOG_OPERATION(
                OPERATE_TYPE, 
                TABLE_NAME, TABLE_REMARK, PRIMARY_ID, 
                OPERATE_USER_ID,
                STATUS, CREATE_TIME, UPDATE_TIME
            )
            VALUES (
                '{operate_type}', 
                '{table_info['table_name']}', '{table_info['table_comments']}', '{table_id}',
                '{operate_user_id}',
                1, to_date('{now_time}','yyyy-mm-dd hh24:mi:ss'), 
                to_date('{now_time}','yyyy-mm-dd hh24:mi:ss')
            )
            """
            cursor.execute(insert_sql)

            # 获取新增的结果
            select_sql = f"""
            SELECT ID, TABLE_NAME, PRIMARY_ID, CREATE_TIME FROM LOG_OPERATION 
            WHERE TABLE_NAME='{table_info['table_name']}' AND PRIMARY_ID='{table_id}'
                AND CREATE_TIME=to_date('{now_time}','yyyy-mm-dd hh24:mi:ss')
            """
            cursor.execute(select_sql)
            result = cursor.fetchall()
            new_log_id = result[0][0]

            # 日志内容表添加内容
            insert_sql_all = "BEGIN "
            index = 0
            for key in table_info["keys_list"]:
                key_name = "" if not key[0] else key[0]
                key_remark = "" if not key[1] else key[1]
                key_value = "" if not key_value_list[index] else key_value_list[index]

                insert_sql_item = F"""
                INSERT INTO LOG_CONTENT(
                    OPERATE_ID, 
                    KEY_NAME, KEY_REMARK, 
                    VALUE,
                    STATUS, CREATE_TIME, UPDATE_TIME
                )
                VALUES (
                    '{new_log_id}', 
                    '{key_name}', '{key_remark}',
                    '{key_value}',
                    1, to_date('{now_time}','yyyy-mm-dd hh24:mi:ss'), 
                    to_date('{now_time}','yyyy-mm-dd hh24:mi:ss')
                );
                """
                index += 1
                insert_sql_all += insert_sql_item

            insert_sql_all += "END;"
            cursor.execute(insert_sql_all)

            self.connection.commit()
            cursor.close()
            return True, new_log_id, ""

        except Exception as error:
            cursor.close()
            return False, "", str(error)

    def get_log_info(self, log_id):
        """获取log详情"""
        cursor = self.get_cursor()

        select_sql = f"""
        SELECT 
            OPERATE_TYPE, TABLE_NAME, TABLE_REMARK, PRIMARY_ID, STATUS
        FROM LOG_OPERATION WHERE ID='{log_id}'
        """
        cursor.execute(select_sql)
        result = cursor.fetchall()
        if len(result) == 0:
            raise LookupError(f"log row is not exit!")
        _log_info = result[0]

        select_sql = f"""
        SELECT 
            KEY_NAME, KEY_REMARK, VALUE, CURRENT_VALUE
        FROM LOG_CONTENT WHERE OPERATE_ID='{log_id}' ORDER BY ID
        """
        cursor.execute(select_sql)
        result = cursor.fetchall()

        result_dict = []
        key_name_list = []
        key_value_list = []
        for row in result:
            key_value = "" if not row[2] else row[2]
            result_dict.append({
                "key_name": row[0],
                "key_remark": "" if not row[1] else row[1],
                "value": key_value,
                "current_value": "" if not row[3] else row[3],
            })
            key_name_list.append(row[0])
            if is_valid_date(key_value):
                key_value = key_value.split(".")[0]
                key_value = f"to_date('{key_value}','yyyy-mm-dd hh24:mi:ss')"
            else:
                key_value = "'" + str(key_value) + "'"
            key_value_list.append(key_value)

        log_info = {
            "operate_type": _log_info[0],
            "table_name": _log_info[1],
            "table_remark": _log_info[2],
            "primary_id": _log_info[3],
            "status": _log_info[4],
            "key_value_list": result_dict,
            "key_name_list": key_name_list,
            "key_name_str": ",".join(key_name_list),
            "key_value_str": ",".join(key_value_list),
        }

        cursor.close()
        return log_info

    def get_row_value(self, table_info, table_name, primary_name, table_id):
        """获取当前记录值"""
        cursor = self.get_cursor()

        select_sql = f"""
        SELECT {table_info['keys_str']} FROM {table_name} WHERE {primary_name}='{table_id}'
        """
        cursor.execute(select_sql)
        result = cursor.fetchall()

        cursor.close()
        if len(result) == 0:
            raise LookupError(f"Primary key {table_id} data is not exit!")

        return result[0]

    def get_table_info(self, table_name):
        """获取表详情和字段列表"""
        cursor = self.get_cursor()

        if self.table_info_dict.get(table_name):
            table_info = self.table_info_dict.get(table_name)

        else:
            table_info = {}

            # 获取表注释&判断表是否存在
            select_sql = f"""
            SELECT TABLE_NAME, COMMENTS FROM USER_TAB_COMMENTS WHERE TABLE_NAME='{table_name}'
            """
            cursor.execute(select_sql)
            result = cursor.fetchall()

            if len(result) == 0:
                raise LookupError(f"Table {table_name} is not exit!")

            table_info["table_name"] = result[0][0]
            table_info["table_comments"] = "" if not result[0][1] else result[0][1]

            # 获取键名和注释
            select_sql = f"""
            SELECT COLUMN_NAME, COMMENTS FROM USER_COL_COMMENTS WHERE TABLE_NAME='{table_name}' ORDER BY COLUMN_NAME
            """
            cursor.execute(select_sql)
            result = cursor.fetchall()
            result = sorted(result, key=lambda i: len(i[0]))

            keys_list = [i[0] for i in result]
            keys_str = ", ".join(keys_list)

            table_info["keys_list"] = result
            table_info["keys_str"] = keys_str

            self.table_info_dict[table_name] = table_info

            cursor.close()

        return table_info

    def get_connection(self):
        if not self.connection:
            self.connection = cx_Oracle.connect(ECMS_CONN_STR)
        return self.connection

    def get_cursor(self):
        connection = self.get_connection()
        return connection.cursor()

    def __del__(self):
        if self.connection:
            self.connection.close()


def test_log(req):
    log_operation = LogOperation()
    # result, log_id, error_msg = log_operation.update_before(
    #     table_name="ACTIVITY_DISCOUNTRECORD",
    #     table_id="1261",
    #     operate_user_id=1
    # )
    # result, log_id, error_msg = log_operation.update_after(
    #     table_name="ACTIVITY_DISCOUNTRECORD",
    #     table_id="1261",
    #     log_id="42"
    # )
    result, log_id, error_msg = log_operation.recover_delete(
        log_id="42",
        operate_user_id=1
    )

    return ReturnDataApi(data=log_id, msg=error_msg)
