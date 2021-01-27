# SQL命令行

## 获取分组分组最后一条数据(可以变换成取同时取多条用于比较)
``` 
# 方法一(效率最高)
SELECT * FROM test AS a 
WHERE typeindex = ( SELECT max( b.typeindex ) FROM test AS b WHERE a.TYPE = b.TYPE )

# 方法二(效率次之)
SELECT a.* FROM test a,
	( SELECT TYPE, max( typeindex ) typeindex FROM test GROUP BY TYPE ) b 
WHERE a.TYPE = b.TYPE AND a.typeindex = b.typeindex 
ORDER BY a.TYPE

# 方法三
SELECT C.*  FROM
(
    SELECT A.*,
        ROW_NUMBER () OVER (PARTITION BY A.SUPPLIERTESTDATASTEP_ID ORDER BY A.DPTTIME) RW 
    FROM 'S_00PCEHAN02L03HA1D0002045' WHERE B.RW =1
) C
```

## 批量插入
``` 
# oracle
INSERT ALL
INTO "REVIEW_REVIEWCONFIG" (name,config_value,config_unit,config_type,order_no,test_type,activate) 
VALUES ('平行样电压差异>',0.1,'V',9,10,4,1)
INTO "REVIEW_REVIEWCONFIG" (name,config_value,config_unit,config_type,order_no,test_type,activate) 
VALUES ('平行样容量差异>',10,'%',9,20,4,1)
SELECT 1 FROM DUAL

# MYSQL
INSERT INTO persons 
(id_p, lastname, firstName, city)
VALUES
(201, 'haha2', 'deng', 'GD'),
(202, 'haha3', 'deng', 'Beijing');
```

## 存储过程使用示例1
``` 
WITH 
    A1 AS (SELECT * FROM SUPPLIER_TESTDATASTEP),
    A2 AS (SELECT * FROM SUPPLIER_TESTDATASTEP),
    A3 AS (SELECT * FROM A1)
SELECT  * FROM A1 
    LEFT JOIN A2 ON A1.ID = A2.SUPPLIERTESTDATASTEP_ID
    LEFT JOIN A3 ON A1.ID = A3.SUPPLIERTESTDATASTEP_ID
ORDER BY A2.DPTTIME 
```

## 存储过程使用示例2
+ 表无主键时如何处理
+ 如何去重
+ 同时取出当前条和上一条数据，并用于比较
```
WITH TEMP1 AS (  -- 为电芯表添加序列号，原无主键，去重用
    SELECT ROW_NUMBER() OVER (ORDER BY A0.SUPPLIERTESTDATASTEP_ID, A0.DPTTIME) AS ROW_NUM, A0.* 
    FROM "S_00FCE3C00000049C00300074" A0 ORDER BY A0.SUPPLIERTESTDATASTEP_ID, A0.DPTTIME
)
SELECT 
    B1.*， (B2.RECORDTIME - B1.RECORDTIME) DIFF_TIME, 
FROM TEMP1 B1, TEMP1 B2 
WHERE 
    -- 查出上一条数据用于比较
    B1.ROW_NUM=B2.ROW_NUM-1 
    -- 该步是为了去重
    AND B1.ROW_NUM IN (SELECT MAX(B3.ROW_NUM) FROM TEMP1 B3 GROUP BY B3.SUPPLIERTESTDATASTEP_ID, B3.DPTTIME)
    AND (B2.RECORDTIME - B1.RECORDTIME) < 60000 
```

## case...when...else 使用示例
```
SELECT *,
    (case
        when item_type_name=1 then '短期测试'
        when item_type_name=2 then '循环'
        else '测试2'
    end) as item_type
FROM ANALYZE_DEVICEUTILIZATIONRATE
```

## 存在更新，不存在新增
``` 
方法1：
BEGIN 
    UPDATE USERS_JOB SET STATUS=1  WHERE DEPT_ID='4444';
    IF SQL % NOTFOUND THEN
        INSERT INTO USERS_JOB(JOB_ID, JOB_NAME) 
        VALUES ({user_job_id}, '{user_job}'); 
    END IF;
END;

方法2：
DECLARE num NUMBER;   
BEGIN 
    SELECT COUNT(*) INTO num FROM USERS_USERJOBRELATE WHERE JOB_ID='{user_job_id}' ;
    IF num < 1 THEN 
        INSERT INTO USERS_USERJOBRELATE(JOB_ID, USER_ID, STATUS)
        VALUES(2, 3, 4);
    END IF;
END;
```

