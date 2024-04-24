import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def f(x, y):
    return np.sin(x) + np.cos(y) * np.exp(-(x**2 + y**2))

# 生成 x 和 y 的网格点
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# 计算函数值
Z = f(X, Y)

# 绘图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X, Y)')
ax.set_title('Surface plot of f(x, y)')
plt.show()
