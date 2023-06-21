"""
环境：anaconda:conda 23.3.1,python=Python 3.7.16,open3d=0.11.2
"""


import tkinter as tk
import open3d as o3d


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Open3D 矩形体")
        self.master.geometry("300x200")

        self.width_label = tk.Label(master, text="宽度")
        self.width_label.pack()
        self.width_entry = tk.Entry(master)
        self.width_entry.pack()

        self.height_label = tk.Label(master, text="高度")
        self.height_label.pack()
        self.height_entry = tk.Entry(master)
        self.height_entry.pack()

        self.depth_label = tk.Label(master, text="深度")
        self.depth_label.pack()
        self.depth_entry = tk.Entry(master)
        self.depth_entry.pack()

        self.submit_button = tk.Button(master, text="显示矩形体", command=self.create_box)
        self.submit_button.pack()

    def create_box(self):
        width = float(self.width_entry.get())
        height = float(self.height_entry.get())
        depth = float(self.depth_entry.get())

        mesh_box = o3d.geometry.TriangleMesh.create_box(width=width,
                                                        height=height,
                                                        depth=depth)
        mesh_box.compute_vertex_normals()
        mesh_box.paint_uniform_color([1, 0, 0])  # RGB
        o3d.visualization.draw_geometries([mesh_box])


root = tk.Tk()
main_window = MainWindow(root)
root.mainloop()
