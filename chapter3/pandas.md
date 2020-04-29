# pandas

## 取值
``` 
df['w']  #选择表格中的'w'列，使用类字典属性,返回的是Series类型
df.w    #选择表格中的'w'列，使用点属性,返回的是Series类型
df[['w']]  #选择表格中的'w'列，返回的是DataFrame属性

data[0:2]  #返回第1行到第2行的所有行，前闭后开，包括前不包括后
data[1:2]  #返回第2行，从0计，返回的是单行，通过有前后值的索引形式，
           #如果采用data[1]则报错

data.iloc[-1]   #选取DataFrame最后一行，返回的是Series
data.iloc[-1:]   #选取DataFrame最后一行，返回的是DataFrame

获取某一列第一个数据
df_min_item["voltage"].iloc[0]
```

## pandas 检索功能
``` 

```