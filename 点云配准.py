import open3d as o3d
import numpy as np

source = o3d.io.read_point_cloud("dragonStandRight_24.ply")
target = o3d.io.read_point_cloud("dragonStandRight_0.ply")

# 调整点云颜色    rgb
source.paint_uniform_color([1, 0, 0])
target.paint_uniform_color([0, 1, 0])

# 对点云进行下采样滤波
voxel_size = 0.005  # 点云体素化尺寸
downsource = source.voxel_down_sample(voxel_size)
downtarget = target.voxel_down_sample(voxel_size)

threshold = 1.0  # 移动范围的阀值
trans_init = np.asarray([[1, 0, 0, 0],  # 4x4 identity matrix，这是一个转换矩阵，
                         [0, 1, 0, 0],  # 象征着没有任何位移，没有任何旋转，我们输入
                         [0, 0, 1, 0],  # 这个矩阵为初始变换
                         [0, 0, 0, 1]])

# 运行icp
reg_p2p = o3d.registration.registration_icp(
    downsource, downtarget, threshold, trans_init,
    o3d.registration.TransformationEstimationPointToPoint())

# 将我们的矩阵依照输出的变换矩阵进行变换
print(reg_p2p)
downsource.transform(reg_p2p.transformation)

# 在点云上加上法向量以进行后续处理
downsource.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
downtarget.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

# 进行点云配准
print("Registering...")
threshold = 0.02
trans_init = np.asarray([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
reg_p2p = o3d.pipelines.registration.registration_icp(downsource, downtarget, threshold, trans_init,
                                                      o3d.pipelines.registration.TransformationEstimationPointToPoint())
print(reg_p2p)

# 将所有点云数据合并成一个列表
pcd_list = [downsource, downtarget]

# 可视化所有点云数据
o3d.visualization.draw_geometries(pcd_list)
