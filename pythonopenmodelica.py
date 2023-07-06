from OMPython import OMCSessionZMQ
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# 创建与OpenModelica的连接
omc = OMCSessionZMQ()

# 加载模型文件

model_file = 'E:/WeChat Files/WeChat Files/wxid_3pd4xcrh3dr822/FileStorage/File/2023-06/Pendulum.mo'
omc.sendExpression('loadModel(Modelica)')
omc.sendExpression('loadFile("' + model_file + '")')

load_errors = omc.sendExpression('getErrorString()')
if load_errors:
    print("模型加载错误:")
    print(load_errors)
    exit()

# 编译模型
omc.sendExpression('translateModel("Pendulum")')
omc.sendExpression('buildModel(Pendulum)')
# 检查模型编译是否成功
build_errors = omc.sendExpression('getErrorString()')
if build_errors:
    print("模型编译错误:")
    print(build_errors)
    exit()

# 设置仿真参数
stopTime=3000
omc.sendExpression('setCommandLineOptions("--noWindow")')
# 开始仿真
omc.sendExpression('simulate(Pendulum, stopTime='+str(stopTime)+')')
# 检查模型编译是否成功
build_errors = omc.sendExpression('getErrorString()')
if build_errors:
    print("仿真错误:")
    print(build_errors)
    exit()

# 获取仿真结果
# 提取omega、theta、alpha和时间的值
#omega =omc.sendExpression('val(omega,[1 3000])')
# 打印omega、theta、alpha和时间的值


times = []
omega = []
theta=[]

# 循环获取每个时间点的值，并存储在列表中
for time in np.arange(0,stopTime,1):
    value1 = omc.sendExpression('val(omega,'+str(time)+')')
    value2 = omc.sendExpression('val(theta,'+str(time)+')')
    times.append(time)
    omega.append(value1)
    theta.append(value2)



#data = [times,omega,theta]
#columns=['time', 'omega','theta']

#df = pd.DataFrame({col: values for col, values in zip(columns, data)})

#df.to_excel('output.xlsx', index=False)
# 绘制曲线图
# 创建第一个子图，显示变量 a 的曲线图
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
