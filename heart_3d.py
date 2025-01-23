import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建图形对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 生成数据点
t = np.linspace(0, 2*np.pi, 100)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
z = np.zeros_like(t)

# 创建3D心形
for height in np.linspace(0, 10, 20):
    z = np.ones_like(t) * height
    ax.plot(x, y, z, color='red', alpha=0.5)

# 设置视角和标签
ax.view_init(30, 45)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Heart')

# 调整图形比例
ax.set_box_aspect([1,1,1])

# 显示图形
plt.show() 