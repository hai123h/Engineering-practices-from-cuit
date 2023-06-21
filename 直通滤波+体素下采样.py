import numpy as np
import open3d as o3d
from open3d import io

# 读取点云数据
pcd = o3d.io.read_point_cloud("rabbit.pcd")
o3d.visualization.draw_geometries([pcd])

# 将点云数据转换为numpy数组
points = np.asarray(pcd.points)

# 计算点云数据的总数
n_points = points.shape[0]
print(n_points)

# 设定需要保留的点云范围
x_min, x_max = -90, 90
y_min, y_max = -90, 90
z_min, z_max = -5, 5

# 将点云数据转化为 numpy 数组
pcd_array = np.asarray(pcd.points)

# 使用 numpy 的逻辑运算符构建掩码
mask = (pcd_array[:, 0] > x_min) & (pcd_array[:, 0] < x_max) \
     & (pcd_array[:, 1] > y_min) & (pcd_array[:, 1] < y_max) \
     & (pcd_array[:, 2] > z_min) & (pcd_array[:, 2] < z_max)
# mask = (pcd_array[:, 2] > z_min) & (pcd_array[:, 2] < z_max)

# 保留符合掩码的点云数据
pcd_filtered = pcd.select_by_index(np.where(mask)[0])

# 可视化直通滤波处理结果
o3d.visualization.draw_geometries([pcd_filtered])
print(pcd_filtered)

# 对点云进行体素下采样
voxel_size = 3
downsampled_pcd = pcd_filtered.voxel_down_sample(voxel_size)

# 可视化体素下采样处理结果
o3d.visualization.draw_geometries([downsampled_pcd])
print(downsampled_pcd)

