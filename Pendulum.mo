model Pendulum
  // 定义模型参数
  parameter Real g = 9.81 "重力加速度";
  parameter Real L = 1 "摆长";

  // 定义模型变量
  Real theta "摆角" ;
  Real omega "角速度" ;
  Real alpha "角加速度" ;

  // 定义初始条件
  initial equation
    theta = 0.1; // 初始摆角为0.1弧度
    omega = 0; // 初始角速度为0

  // 定义运动方程
  equation
    der(omega) = -g/L*sin(theta); // 角加速度
    der(theta) = omega; // 摆角变化率为角速度

  // 定义附加方程
  alpha = -g/L*sin(theta); // 角加速度等于摆角的正弦值乘以重力加速度与摆长的比值


end Pendulum;
