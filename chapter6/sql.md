# SQL命令行

## 获取分组分组最后一条数据
``` 
# 方法一(效率最高)
SELECT
	* 
FROM
	test AS a 
WHERE
	typeindex = ( SELECT max( b.typeindex ) FROM test AS b WHERE a.TYPE = b.TYPE )

# 方法二(效率次之)
SELECT
	a.* 
FROM
	test a,
	( SELECT TYPE, max( typeindex ) typeindex FROM test GROUP BY TYPE ) b 
WHERE
	a.TYPE = b.TYPE 
	AND a.typeindex = b.typeindex 
ORDER BY
	a.TYPE

# 方法三
SELECT
	C.* 
FROM
(
    SELECT
        A.*,
        ROW_NUMBER () OVER (PARTITION BY A.SUPPLIERTESTDATASTEP_ID ORDER BY A.DPTTIME) RW 
    FROM
        'S_00PCEHAN02L03HA1D0002045'
    WHERE
        B.RW =1
) C
```

## 插入
``` 
# oracle
INSERT ALL
INTO "REVIEW_REVIEWCONFIG" (name,config_value,config_unit,config_type,order_no,test_type,activate) 
VALUES ('平行样电压差异>',0.1,'V',9,10,4,1)
INTO "REVIEW_REVIEWCONFIG" (name,config_value,config_unit,config_type,order_no,test_type,activate) 
VALUES ('平行样容量差异>',10,'%',9,20,4,1)
INTO "REVIEW_REVIEWCONFIG" (name,config_value,config_unit,config_type,order_no,test_type,activate) 
VALUES ('平行样电芯温度差异>',1,'℃',9,30,4,1)
INTO "REVIEW_REVIEWCONFIG" (name,config_value,config_unit,config_type,order_no,test_type,activate) 
VALUES ('平行样环境温度差异>',1,'℃',9,40,4,1)
SELECT 1 FROM DUAL

# MYSQL
INSERT INTO persons 
(id_p, lastname, firstName, city)
VALUES
(200, 'haha', 'deng', 'shenzhen'),
(201, 'haha2', 'deng', 'GD'),
(202, 'haha3', 'deng', 'Beijing');
```

## 存储过程：获取分组第一条和最后一条数据
``` 
WITH 
    A1 AS (
        SELECT
            A.ID,
            A.STEPID,
            A.STEPTYPE,
            A.CAP,
            A.ENG,
            A.STARTTEMP,
            A.ENDTEMP
        FROM
            SUPPLIER_TESTDATASTEP A
        WHERE
            A.BATTERYBARCODE = '00PCEHAN02L03HA1E0000924'
    ),
    
    A2 AS (
        SELECT
            * 
        FROM
            (
            SELECT
                M2.*,
                ROW_NUMBER () OVER ( PARTITION BY M2.SUPPLIERTESTDATASTEP_ID ORDER BY M2.DPTTIME ) M2_RW 
            FROM
                (SELECT
                    M1.SUPPLIERTESTDATASTEP_ID,
                    M1.VOLTAGE,
                    M1."CURRENT",
                    M1.DPTTIME 
                FROM
                    "S_00PCEHAN02L03HA1E0000924" M1 
                WHERE
                    M1.SUPPLIERTESTDATASTEP_ID IN ( SELECT A1.ID FROM A1 )) M2 
            ) M3 
        WHERE
            M3.M2_RW = 1
    ),
    
    A3 AS (
        SELECT
            * 
        FROM
            (
            SELECT
                N2.*,
                ROW_NUMBER () OVER ( PARTITION BY N2.SUPPLIERTESTDATASTEP_ID ORDER BY N2.DPTTIME DESC ) N2_RW 
            FROM
                (SELECT
                    N1.SUPPLIERTESTDATASTEP_ID,
                    N1.VOLTAGE,
                    N1."CURRENT",
                    N1.DPTTIME 
                FROM
                    "S_00PCEHAN02L03HA1E0000924" N1 
                WHERE
                    N1.SUPPLIERTESTDATASTEP_ID IN ( SELECT A1.ID FROM A1 )) N2 
            ) N3 
        WHERE
            N3.N2_RW = 1
    )

SELECT 
    A1.STEPID,
    A1.STEPTYPE,
    A1.CAP,
    A1.ENG,
    A1.STARTTEMP,
    A1.ENDTEMP,
    
    A2.VOLTAGE,
    A2."CURRENT",
    A2.DPTTIME,
    
    A3.VOLTAGE,
    A3."CURRENT",
    A3.DPTTIME
FROM A1 
    LEFT JOIN A2 ON A1.ID = A2.SUPPLIERTESTDATASTEP_ID
    LEFT JOIN A3 ON A1.ID = A3.SUPPLIERTESTDATASTEP_ID
ORDER BY A2.DPTTIME 
```