# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from scipy import stats


def fill_tre_top_s(x):
    """为不够5位的数组填充nan"""
    if len(x) <= 5:
        new_array = np.full(5, np.nan)
        new_array[0: len(x)] = x
        return new_array


def eda_analysis(df=None, miss_set=None):
    if miss_set is None:
        miss_set = [np.nan, 9999999999, -999999]
    # 统计数字个数，去重
    count_un = df.apply(lambda x: len(x.unique()))
    count_un = count_un.to_frame("count")

    # 统计数字等于0的个数
    count_zero = df.apply(lambda x: np.sum(x == 0))
    count_zero = count_zero.to_frame("count_zero")

    # 平均值
    df_mean = df.apply(lambda x: np.mean(x[~np.isin(x, miss_set)]))
    df_mean = df_mean.to_frame("df_mean")

    # 中位数
    df_median = df.apply(lambda x: np.median(x[~np.isin(x, miss_set)]))
    df_median = df_median.to_frame("df_median")

    # 众数
    df_mode = df.apply(lambda x: stats.mode(x[~np.isin(x, miss_set)])[0][0])
    df_mode = df_mode.to_frame("df_mode")

    # 众数出现频率
    df_mode_count = df.apply(lambda x: stats.mode(x[~np.isin(x, miss_set)])[1][0])
    df_mode_count = df_mode_count.to_frame("df_mode_count")

    df_mode_percent = df_mode_count / df.shape[0]
    df_mode_percent.columns = ["df_mode_percent"]

    # min
    df_min = df.apply(lambda x: np.min(x[~np.isin(x, miss_set)]))
    df_min = df_min.to_frame("df_min")

    # max
    df_max = df.apply(lambda x: np.max(x[~np.isin(x, miss_set)]))
    df_max = df_max.to_frame("df_max")

    # 分位点
    json_quantile = {}
    for i, name in enumerate(df.columns):
        json_quantile[name] = np.percentile(df[name][~np.isin(df[name], miss_set)], (1, 25, 50, 75, 99))
    df_quantile = pd.DataFrame(json_quantile)[df.columns].T
    df_quantile.columns = ["quan01", "quan25", "quan50", "quan75", "quan99"]

    # 频数
    json_fre_name = {}
    json_fre_count = {}
    for i, name in enumerate(df.columns):
        index_name = df[name][~np.isin(df[name], miss_set)].value_counts().iloc[0:5, ].index.values
        index_name = fill_tre_top_s(index_name)
        json_fre_name[name] = index_name
        # 获取频率前5数字
        values_count = df[name][~np.isin(df[name], miss_set)].value_counts().iloc[0:5, ].values
        values_count = fill_tre_top_s(values_count)
        json_fre_count[name] = values_count

    df_fre_name = pd.DataFrame(json_fre_name)[df.columns].T
    df_fre_count = pd.DataFrame(json_fre_count)[df.columns].T

    df_fre = pd.concat([df_fre_name, df_fre_count], axis=1)
    df_fre.columns = ["value1", "value2", "value3", "value4", "value5",
                      "freq1", "freq2", "freq3", "freq4", "freq5"]

    # miss
    df_miss = df.apply(lambda x: np.sum(x[np.isin(x, miss_set)]))
    df_miss = df_miss.to_frame("df_miss")

    # 拼接，整合
    df_eda_summary = pd.concat(
        [count_un, count_zero, df_mean, df_median,
         df_mode, df_mode_count, df_mode_percent, df_min,
         df_max, df_quantile, df_fre, df_miss],
        axis=1
    )

    df_eda_summary.to_csv("test.csv")

    return df_eda_summary

