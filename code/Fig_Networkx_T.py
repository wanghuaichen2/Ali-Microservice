#根据一个踪迹idT_22531765305，
# 打印出调用关系，一张图片记录了所以调用关系，没有基于时间
import pandas as pd
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv('../dataset/CallGraph_T_22531765305.csv')

# 创建一个有向图
G = nx.DiGraph()

# 添加微服务关系到图中
for _, row in df.iterrows():
    um = row['um']
    dm = row['dm']
    G.add_edge(um, dm)

# 绘制微服务调用图
root_node = 'UNKNOWN'
T = nx.bfs_tree(G, root_node)  # 使用广度优先搜索生成树形结构
pos = nx.shell_layout(T)  # 使用shell布局算法布局节点
# pos = nx.spring_layout(G, k=100)  # 使用Spring布局算法布局节点
nx.draw(T, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=8, font_color='black',
        edge_color='gray', linewidths=1, arrowsize=20)
plt.title('Microservices Call Graph')
plt.show()