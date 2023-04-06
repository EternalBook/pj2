import pandas as pd

'''
一、数据导入
'''
# 1.州缩写表
abbrevs = pd.read_csv(r"./data/state-abbrevs.csv")
# 1.1 查看州的数量
# print(abbrevs.shape)
# 1.2判断数据是否有缺失
# print(abbrevs.isnull().any())  # False表示不存在空值
# 1.3判断是否有重复数据
# print(abbrevs['state'].unique().size)  # 去重 size为51者没重复值
# print(abbrevs)
# 2.人口表
population = pd.read_csv(r"./data/state-population.csv")
# print(population.head())
# 2.1 人口表中查看州的数量
# print(population['state/region'].unique())
# print(population['state/region'].unique().size)

#
# 3.面积表
areas = pd.read_csv(r"./data/state-areas.csv")
# 3.1查看州的个数
# print(areas['state'].unique().size)
# print(areas['state'].unique())
# print(areas)
'''
二、合并表格
'''
# 1.缩写表和人口表合并 外合并
data_csv = pd.merge(population, abbrevs, how="outer", left_on='state/region', right_on='abbreviation')
# print(data_csv.head())
# 合并后abbreviation和state/region内容一致，删除一行
# 1.2 判断population是否有空值
# print(population.isnull().any())
# 1.3 删除abbreviation
data_csv.drop(labels=["abbreviation"], axis=1, inplace=True)
# 1.4 全称state有缺失
# print(data_csv.loc[data_csv['state'].isnull()]['state/region'].unique())   # PR ,USA有缺失  USA是总数据 PR是州数据 (Puerto Rico)
# 1.5 填充空值，PR对应全称填入
# 1.5.1 找出PR的state的值， 赋值
data_csv.loc[data_csv['state/region'] == "PR", "state"] = "Puerto Rico"
data_csv.loc[data_csv['state/region'] == "USA", "state"] = "USA"

# 2.缩写人口表和面积表合并
total = pd.merge(data_csv, areas, how="outer")
# 2.1判断total存在空值
# print(total.isnull().any())
# 2.2 找出area 存在空值的州   不设计人口密度计算， 去除
# print(total.loc[total['area (sq. mi)'].isnull()])
"""
删除 
过滤
"""
# 1.删除 drop
# 2.过滤
not_emtpy_index = total[total['area (sq. mi)'].notnull()].index
total = total.loc[not_emtpy_index]
# print(total)
# ============================数据预处理
# 数据特征提取
# 1.查看2010年全民人口数量  year = 2010  全民 = ages = total
# 两种方法
# 方法一：
# condition = ((total['year'] == 2010) & (total["ages"] == "total"))
# total2010=total[condition]
# print(total2010)
# 方法二：
