import pandas as pd

file_path = '../dataset/CallGraph_480.csv'
# 读取CallGraph_480.csv文件
df = pd.read_csv(file_path, sep=",", on_bad_lines="skip")

# 打印列名
print("列名：", df.columns)

# 统计数据条数
data_count = len(df)
print("数据条数：", data_count)
# 获取列数
num_columns = df.shape[1]
# 打印列数
print("列数:", num_columns)

# 打印前五行数据
print("前五行数据：")
print(df.head())

# 将列名为traceid，值为T_22531765305的每一行记录保存到CallGraph.csv中
traceid_T_18351226599 = df[df['traceid'] == 'T_22531765305']
traceid_T_18351226599.to_csv('CallGraph_T_22531765305.csv', index=False)
