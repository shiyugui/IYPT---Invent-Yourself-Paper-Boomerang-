'''
_______________#########_______________________ 
______________############_____________________ 
______________#############____________________ 
_____________##__###########___________________ 
____________###__######_#####__________________ 
____________###_#######___####_________________ 
___________###__##########_####________________ 
__________####__###########_####_______________ 
________#####___###########__#####_____________ 
_______######___###_########___#####___________ 
_______#####___###___########___######_________ 
______######___###__###########___######_______ 
_____######___####_##############__######______ 
____#######__#####################_#######_____ 
____#######__##############################____ 
___#######__######_#################_#######___ 
___#######__######_######_#########___######___ 
___#######____##__######___######_____######___ 
___#######________######____#####_____#####____ 
____######________#####_____#####_____####_____ 
_____#####________####______#####_____###______ 
______#####______;###________###______#________ 
________##_______####________####______________ 
'''
import numpy as np
import matplotlib.pyplot as plt

def get_input(prompt, cast_func=float):
    """
    获取用户输入并转换为指定类型。
    
    参数:
    prompt (str): 提示用户输入的字符串。
    cast_func (function): 用于转换输入的函数，默认为 float。
    
    返回:
    转换后的用户输入。
    """
    while True:
        try:
            return cast_func(input(prompt))
        except ValueError:
            print("输入无效，请重新输入。")

def initialize_parameters():
    """
    初始化纸飞镖的参数，包括质量、参考面积、升力系数、阻力系数、初速度和投掷角度。
    
    返回:
    tuple: 包含质量、参考面积、升力系数、阻力系数、初速度和投掷角度的元组。
    """
    mass = get_input("请输入纸飞镖的质量 (单位: kg) :")
    area = get_input("请输入纸飞镖的参考面积 (单位: m^2) :")
    lift_coefficient = get_input("请输入纸飞镖的升力系数 :")
    drag_coefficient = get_input("请输入纸飞镖的阻力系数 :")
    initial_velocity = get_input("请输入纸飞镖的初速度 (单位: m/s) :")
    angle_degrees = get_input("请输入纸飞镖的投掷角度 (单位: 度) :")
    return mass, area, lift_coefficient, drag_coefficient, initial_velocity, angle_degrees

def update(position, velocity, mass, area, lift_coefficient, drag_coefficient, time_step, density_air, G):
    """
    更新纸飞镖的位置和速度。
    
    参数:
    position (np.array): 当前的位置。
    velocity (np.array): 当前的速度。
    mass (float): 纸飞镖的质量。
    area (float): 纸飞镖的参考面积。
    lift_coefficient (float): 纸飞镖的升力系数。
    drag_coefficient (float): 纸飞镖的阻力系数。
    time_step (float): 时间步长。
    density_air (float): 空气密度。
    G (float): 重力加速度。
    
    返回:
    tuple: 更新后的位置和速度。
    """
    acceleration = np.array([0.0, -G])  # 初始加速度，仅考虑重力
    speed = np.linalg.norm(velocity)  # 计算速度的大小
    if speed > 0:
        # 计算升力和阻力
        lift_force = 0.5 * density_air * speed**2 * area * lift_coefficient * np.array([-velocity[1], velocity[0]]) / speed
        drag_force = -0.5 * density_air * speed**2 * area * drag_coefficient * velocity / speed
    else:
        lift_force = drag_force = np.array([0.0, 0.0])  # 如果速度为零，则升力和阻力为零
    acceleration += (lift_force + drag_force) / mass  # 更新加速度
    velocity += acceleration * time_step  # 更新速度
    position += velocity * time_step  # 更新位置
    return position, velocity

def main():
    """
    主函数，执行纸飞镖的模拟。
    """
    # 初始化参数
    mass, area, lift_coefficient, drag_coefficient, initial_velocity, angle_degrees = initialize_parameters()
    G = 9.81  # 重力加速度
    density_air = 1.225  # 空气密度
    angle_radians = np.radians(angle_degrees)  # 将角度转换为弧度
    time_step = 0.01  # 时间步长
    total_time = 10.0  # 总模拟时间
    position = np.array([0.0, 0.0])  # 初始位置
    velocity = np.array([initial_velocity * np.cos(angle_radians), initial_velocity * np.sin(angle_radians)])  # 初始速度
    trajectory_x = [position[0]]  # 记录轨迹的X坐标
    trajectory_y = [position[1]]  # 记录轨迹的Y坐标
    times = [0.0]  # 记录时间
    t = 0.0  # 初始化时间
    while t < total_time:
        position, velocity = update(position, velocity, mass, area, lift_coefficient, drag_coefficient, time_step, density_air, G)
        trajectory_x.append(position[0])
        trajectory_y.append(position[1])
        times.append(t + time_step)
        t += time_step
        if position[1] <= 0.0 and abs(position[0]) < 1.0:
            break
    # 绘制轨迹图
    plt.figure()
    plt.plot(trajectory_x, trajectory_y, label='Trajectory')
    plt.xlabel('X Position (m)')
    plt.ylabel('Y Position (m)')
    plt.title('Boomerang Flight Simulation')
    plt.legend()
    plt.grid(True)
    plt.show()
    # 输出飞行时间、最大高度和最大飞行距离
    flight_time = times[-1]
    print(f"Flight time: {flight_time:.2f} seconds")
    max_height = max(trajectory_y)
    print(f"Maximum height: {max_height:.2f} meters")
    flight_distance = max(trajectory_x)
    print(f"Maximum flight distance: {flight_distance:.2f} meters")

if __name__ == "__main__":
    main()