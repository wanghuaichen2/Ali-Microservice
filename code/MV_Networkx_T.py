# 根据根据一个踪迹idT_22531765305，
# 按照时间戳保存调用轨迹，将每个时刻的调用情况保存到图中T_22531765305

import pandas as pd
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os

# 创建目录用于保存图片
os.makedirs('call_images', exist_ok=True)

# 读取CSV文件
df = pd.read_csv('../dataset/CallGraph_T_22531765305.csv')

# 创建无向图
G = nx.DiGraph()

# 添加所有节点到图中
all_nodes = set(df['um']).union(set(df['dm']))
G.add_nodes_from(all_nodes)

# 设置根节点为 "UNKNOWN"
root_node = 'UNKNOWN'

# 使用spring布局算法计算节点位置
pos = nx.spring_layout(G, seed=42)

# 绘制初始图，没有连接的情况
nx.draw(G, pos=pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black',
        edge_color='gray', arrows=True,arrowsize=20)
plt.title("Initial Call Graph")
plt.savefig('call_images/call_initial.png')
plt.clf()  # 清除图形

# 按时间戳递增的顺序添加边并保存图像
timestamps = df['timestamp'].unique()
timestamps.sort()

for idx, timestamp in enumerate(timestamps):
    # 创建一个有向图副本
    G_copy = G.copy()

    # 获取历史数据
    historical_df = df[df['timestamp'] <= timestamp]

    # 添加历史数据中的边
    for _, row in historical_df.iterrows():
        um = row['um']
        dm = row['dm']
        G_copy.add_edge(um, dm, color='gray')

    # 获取当前时间戳的数据
    df_timestamp = df[df['timestamp'] == timestamp]

    # 添加当前时刻的边
    for _, row in df_timestamp.iterrows():
        um = row['um']
        dm = row['dm']
        G_copy.add_edge(um, dm, color='red')

    # 绘制有向图，设置边的颜色
    edge_colors = [G_copy[u][v]['color'] for u, v in G_copy.edges()]
    nx.draw(G_copy, pos=pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black',
            edge_color=edge_colors, arrows=True,arrowsize=20)

    # 在右下角显示时间戳
    plt.text(0.9, 0.1, f'T:{timestamp}', ha='center', va='center', transform=plt.gca().transAxes)

    plt.title(f'Call Graph at Timestamp: {timestamp}')

    # 保存图片
    plt.savefig(f'call_images/call_{idx}.png')
    plt.clf()  # 清除图形

print("图片已保存在call_images文件夹中")
