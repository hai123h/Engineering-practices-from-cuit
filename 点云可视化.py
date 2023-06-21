import open3d as o3d
import copy

point = o3d.io.read_point_cloud("rabbit.pcd")
# 曲面重建
# Alpha Shapes算法，滚球法。散点轮廓检测。

tri = o3d.geometry.TriangleMesh
meshes = []
alpha = 0
# 将alpha依次设置为0.3,0.6,0.9,1.2。即更改滚球的半径
for i in range(4):
    alpha += 0.3
    tmpPcd = copy.deepcopy(point).translate((i*20, 0, 0))  # 复制一个，并将其平移20个单位
    mesh = tri.create_from_point_cloud_alpha_shape(tmpPcd, alpha)
    mesh.compute_vertex_normals()
    meshes.append(mesh)

o3d.visualization.draw_geometries(meshes, mesh_show_back_face=True)
