import numpy as np
from dymola.dymola_interface import DymolaInterface
from DyMat import DyMatFile
import matplotlib.pyplot as plt
dymola = DymolaInterface()
model_path = 'E:/WeChat Files/WeChat Files/wxid_3pd4xcrh3dr822/FileStorage/File/2023-06/Pendulum.mo'
result_folder = "C:/Users/tqszbd/Documents/Python Scripts/"
dymola.openModel(model_path)
dymola.translateModel('Pendulum')
#设置变量
dymola.ExecuteCommand("g=30")
dymola.ExecuteCommand("L=10")
simulation_time = 10.0

result = dymola.simulateExtendedModel(
    problem='Pendulum',
    stopTime=simulation_time,
    resultFile=result_folder+'result',
)
dymola.close()
 #使用DyMat库读取Dymola仿真结果

dymola_result = DyMatFile(result_folder+"result.mat")

# 在Python中使用仿真结果进行后续处理和分析
# 例如，输出仿真结果变量的值
#读取时间
times = dymola_result.abscissa("omega",True)
omega = dymola_result.data("omega")
theta = dymola_result.data("theta")
plt.figure()
plt.subplot(2, 1, 1)  # 两行一列，当前为第一个子图
plt.plot(times, omega)
plt.xlabel('time (s)')
plt.ylabel('omega')

# 创建第二个子图，显示变量 b 的曲线图
plt.subplot(2, 1, 2)  # 两行一列，当前为第二个子图
plt.plot(times, theta)
plt.xlabel('time (s)')
plt.ylabel('theta')

plt.tight_layout()  # 调整子图布局，避免重叠
plt.show()


