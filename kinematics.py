import numpy as np
import plotly.graph_objects as go
import math

# 定义关节的旋转范围（弧度）
joint_ranges = [
    (-np.pi, np.pi),             # 关节1: ±180°
    (-np.pi * 130 / 180, np.pi * 130 / 180),   # 关节2: ±130°
    (-np.pi * 135 / 180, np.pi * 135 / 180),   # 关节3: ±135°
    (-np.pi, np.pi),             # 关节4: ±180°
    (-np.pi * 128 / 180, np.pi * 128 / 180),   # 关节5: ±128°
    (-np.pi, np.pi)              # 关节6: ±360°
]

# 连杆长度（单位：米）
link_lengths = [0.210, 0.450, 0.660, 0.210, 0.144, 0.0815]  
d = [0.2405, 0.256, 0, 0, 0, 0]  # 连杆偏移（单位：米）
alpha = [0, -np.pi/2, 0, -np.pi/2, np.pi/2, 0]  # 连杆扭转角

# 定义DH矩阵
def dh_matrix(theta, d, a, alpha):
    return np.array([
        [np.cos(theta), -np.sin(theta)*np.cos(alpha),  np.sin(theta)*np.sin(alpha), a*np.cos(theta)],
        [np.sin(theta),  np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), a*np.sin(theta)],
        [0,              np.sin(alpha),               np.cos(alpha),              d],
        [0,              0,                           0,                          1]
    ])

# 计算正向运动学
def forward_kinematics(joint_angles):
    T = np.eye(4)
    for i in range(len(joint_angles)):
        T = T @ dh_matrix(joint_angles[i], d[i], link_lengths[i], alpha[i])
    return T[:3, 3]

# 使用蒙特卡洛方法计算工作空间
num_samples = 2000
workspace = []

for _ in range(num_samples):
    joint_angles = [np.random.uniform(joint_ranges[i][0], joint_ranges[i][1]) for i in range(len(joint_ranges))]
    pos = forward_kinematics(joint_angles)
    workspace.append(pos)

workspace = np.array(workspace)

# 绘制工作空间
# 使用你的数据
x, y, z = workspace[:, 0], workspace[:, 1], workspace[:, 2]

# 计算x, y, z方向的最小值和最大值
x_min, x_max = np.min(x), np.max(x)
y_min, y_max = np.min(y), np.max(y)
z_min, z_max = np.min(z), np.max(z)

# 创建一个3D散点图
scatter = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=4,
        color=z,                # 设置颜色为z轴的值
        colorscale='Viridis',    # 选择一种颜色映射
        opacity=0.8
    )
)

# 创建图表
fig = go.Figure(data=[scatter])

# 设置布局
fig.update_la