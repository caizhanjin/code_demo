# 一个django sql绑定变量的用法

前一阵子解决了一个一直困扰着的问题，系统会突然得变异常慢，有时候必须重启才能用。就费尽心思地去找原因，发现变慢时，
数据库服务器CPU竟然飙到100%。原来是有个接口存在大量的并发，需要进行大量的读写操作，造成了数据库卡死，其他应用无法读写。
原因是，同事使用了ORM来插入，结果出来的语句全是硬解析，造成了性能上的严重浪费，解决方案：
1. 弃用ORM，改写原生sql，而且需要使用绑定变量写法。
2. 大批量数据插入时，考虑使用rides做缓存，再分批写入。

下面是django原生sql绑定变量写法示例：
``` 
# 使用序列器会产生硬解析语句，改写 2020/12/9
# stepSer = TestDataStepSerializer(data=stepData)
# 新方法绑定变量，先获取自增id(为了得到新增记录的id)
# 正式库自增序列
cursor = connection.cursor()
get_id_sql = """
SELECT "TDMS"."ISEQ$$_97253".nextval FROM dual
"""
cursor.execute(get_id_sql)
res = cursor.fetchone()
stepSer_id = res[0]

insert_sql = """
INSERT INTO "SUPPLIER_TESTDATASTEP"
("ID", "BATTERYBARCODE", "SUPPLIERTESTDATACYCLE_ID", "STEPID",
"STEPTYPE", "STEPTIME", "CAP",
"ENG", "STARTVOL", "ENDVOL",
"STARTTEMP", "ENDTEMP", "CREATEDTIME")
VALUES
(:arg0, :arg1, :arg2, :arg3, :arg4, :arg5, :arg6, :arg7, :arg8, :arg9, :arg10, :arg11,
to_date(:arg12, 'yyyy-MM-dd HH24:mi:ss'))
"""
cursor.execute(insert_sql, {
    "arg0": str(stepSer_id),
    "arg1": stepData['BatteryBarcode'], "arg2": str(stepData['SupplierTestDataCycle']),
    "arg3": str(stepData['StepId']),
    "arg4": stepData['StepType'], "arg5": str(stepData['StepTime']),
    "arg6": str(stepData['Cap']),
    "arg7": str(stepData['Eng']), "arg8": str(stepData['StartVol']),
    "arg9": str(stepData['EndVol']),
    "arg10": str(stepData['StartTemp']), "arg11": str(stepData['EndTemp']),
    "arg12": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
})
cursor.close()
```
