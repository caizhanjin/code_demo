"""
该内容主要来自慕课网课程学习的笔记：https://www.imooc.com/learn/937

数据地址：
链接：https://pan.baidu.com/s/1c57lLs5shUyQLXWFYPYhbA
提取码：kmwc
复制这段内容后打开百度网盘手机App，操作更方便哦
"""
from scipy import stats

import pandas as pd
import numpy as np

# 读取数据
df = pd.read_csv(".\\csv\\train.csv")

label = df["TARGET"]
# 删除id和TARGET
df = df.drop(["ID", "TARGET"], axis=1)

"""
描述/统计 基本指标 实现：

长度/出现次数
均值
中位数
众数
最大值/最小值
分位点（特殊描述值）：从小到大排序，取某个位置的值。中位数就是50%出的分位点
频数：数值出现的次数/高频词统计
缺失值
"""
# 缺失值，用来剔除异常数据
# df.iloc[:, 0][~np.isin(df.iloc[:, 0], miss_set)]，剔除缺失值
miss_set = [np.nan, -999999, 9999999999]
np.sum(np.isin(df.iloc[:, 0], miss_set))  # 统计缺失值
df_miss = df.iloc[:, 0:3].apply(lambda x: np.sum(np.isin(x, miss_set)))

# 长度
# df.iloc[:,:] 可截取单元数据，前面是row，后面是column
# apply用法比较灵活，第一个参数是func，第二个是 axis
# 去重后的单列数据长度
row_length = len(df.iloc[:, 0].unique())
# 多列获取
count_un = df.iloc[:, 0:3].apply(lambda x: len(x.unique()))

# 出现次数
# df.iloc[:, 0] == 0 会在对应位置展示True/False
repeat_num = np.sum(df.iloc[:, 0] == 0)
# 计算多列所有o值出现次数
count_zero = df.iloc[:, 0:3].apply(lambda x: np.sum(x == 0))

# 均值
np.mean(df.iloc[:, 0])  # 没有去除缺失值，均值很低？所以需要剔除缺失值
# np.isin 判定a中的元素在b中是否出现过
np.isin(df.iloc[:, 0], miss_set)
np.mean(df.iloc[:, 0][~np.isin(df.iloc[:, 0], miss_set)])  # 剔除miss_set中元素，后再求均值
df_mean = df.iloc[:, 0:3].apply(lambda x: np.mean(x[~np.isin(x, miss_set)]))  # 多列

# 中位数
np.median(df.iloc[:, 0])  # 没有去除缺失值
np.median(df.iloc[:, 0][~np.isin(df.iloc[:, 0], miss_set)])
df_median = df.iloc[:, 0:3].apply(lambda x: np.median(x[~np.isin(x, miss_set)]))

# 众数
# stats.mode返回两个数组，第一个是众数，第二个是出现次数
df_more = df.iloc[:, 0:3].apply(lambda x: stats.mode(x[~np.isin(x, miss_set)])[0][0])
# 众数出现比例/频率
df_more_count = df.iloc[:, 0:3].apply(lambda x: stats.mode(x[~np.isin(x, miss_set)])[1][0])
df_more_percent = df_more_count/df.shape[0]

# 最大值/最小值
np.max(df.iloc[:, 0][~np.isin(df.iloc[:, 0], miss_set)])
df_max = df.iloc[:, 0:3].apply(lambda x: np.max(x[~np.isin(x, miss_set)]))

np.min(df.iloc[:, 0][~np.isin(df.iloc[:, 0], miss_set)])
df_min = df.iloc[:, 0:3].apply(lambda x: np.min(x[~np.isin(x, miss_set)]))

# 分位点
np.percentile(df.iloc[:, 0], (1, 25, 50, 75, 99))
np.percentile(df.iloc[:, 0][~np.isin(df.iloc[:, 0], miss_set)], (1, 25, 50, 75, 99))

json_quantile = {}
for i, name in enumerate(df.iloc[:, 0:3].columns):
    print(f"The {i} column : {name}")
    json_quantile[name] = np.percentile(df[name][~np.isin(df[name], miss_set)], (1, 25, 50, 75, 99))
df_quantile = pd.DataFrame(json_quantile)[df.iloc[:, 0:3].columns].T  # 转置

# 频数
# 取出现频率前五位的数
# value_counts() 查看某一行/列有多少不同值，并统计重复次数
df["ind_var1_0"].value_counts()
df["imp_sal_var16_ult1"].value_counts()

def fill_tre_top_s(x):
    """为不够5位的数组填充nan"""
    if len(x) <= 5:
        new_array = np.full(5, np.nan)
        new_array[0: len(x)] = x
        return new_array

json_fre_name = {}
json_fre_count = {}
for i, name in enumerate(df[["ind_var1_0", "imp_sal_var16_ult1"]].columns):
    # 获取频率前5数字
    index_name = df[name][~np.isin(df[name], miss_set)].value_counts().iloc[0:5, ].index.values
    index_name = fill_tre_top_s(index_name)
    json_fre_name[name] = index_name
    # 获取频率前5数字
    values_count = df[name][~np.isin(df[name], miss_set)].value_counts().iloc[0:5, ].values
    values_count = fill_tre_top_s(values_count)
    json_fre_count[name] = values_count

json_fre_name = pd.DataFrame(json_fre_name)[df[["ind_var1_0", "imp_sal_var16_ult1"]].columns].T
json_fre_count = pd.DataFrame(json_fre_count)[df[["ind_var1_0", "imp_sal_var16_ult1"]].columns].T
# 拼接 concat() axis=1指的是列拼接
df_fre = pd.concat([json_fre_name, json_fre_count], axis=1)


