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
