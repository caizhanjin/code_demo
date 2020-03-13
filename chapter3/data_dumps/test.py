# -*- coding:utf-8 -*-
import pandas as pd
import time
from wrap_up_with_time import eda_analysis
# from wrap_up import eda_analysis

df = pd.read_csv("D:\\Users\\1908010137\\Desktop\\code_demo\\chapter3\\data_dumps\\csv\\train.csv")
df = df.drop(["ID", "TARGET"], axis=1)

# 整合工具
# eda_analysis(df.iloc[:, 0:3])

# 计算运行时间/测试优化
start_time = time.time()
eda_analysis(df)
print(f"总 running time : {time.time() - start_time} s.")
