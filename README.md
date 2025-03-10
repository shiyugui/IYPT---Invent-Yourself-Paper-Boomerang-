# 前言：

这是一个IYPT2025赛题中的第一题，自制纸飞镖模拟代码，以此来消除不可控的因素，
学校要求以这个题目来做实验，但是实际操作的时候，不可控因素太多，只能通过python模拟来复刻纸飞镖的飞行过程。

这是题目的链接：https://mp.weixin.qq.com/s/5W6-LwPaFwcg9YD_fvn4nQ

# 纸飞镖模拟器

这是一个用于模拟纸飞镖飞行轨迹的程序。通过输入纸飞镖的参数（质量、参考面积、升力系数、阻力系数、初速度和投掷角度），程序将计算并绘制纸飞镖的飞行轨迹，并输出飞行时间、最大高度和最大飞行距离。

# 功能

- 获取用户输入的纸飞镖参数
- 计算纸飞镖在飞行过程中的位置和速度
- 绘制纸飞镖的飞行轨迹
- 输出飞行时间、最大高度和最大飞行距离

# 依赖项

在运行此程序之前，请确保已安装以下 Python 库：

- `numpy`
- `matplotlib`

可以使用以下命令安装这些库：

```bash
pip install numpy matplotlib
```

# 使用方法

- 1.克隆或下载次仓库

- 2.运行代码

- 3.按照提示输入纸飞镖参数:
  - 请输入纸飞镖的质量 (单位: kg)
  - 请输入纸飞镖的参考面积 (单位: m²)
  - 请输入纸飞镖的升力系数
  - 请输入纸飞镖的阻力系数
  - 请输入纸飞镖的初速度 (单位: m/s)
  - 请输入纸飞镖的投掷角度 (单位: 度)

- 4.程序将计算并绘制纸飞镖的飞行轨迹，并输出飞行时间、最大高度和最大飞行距离。

# 示例

### 输入：

 - 请输入纸飞镖的质量 (单位: kg) : 0.01
 - 请输入纸飞镖的参考面积 (单位: m²) : 0.02
 - 请输入纸飞镖的初速度 (单位: m/s) : 10
 - 请输入纸飞镖的投掷角度 (单位: 度) : 30

### 输出：
 - Flight time: 1.28 seconds
 - Maximum height: 2.66 meters
 - Maximum flight distance: 0.86 meters
 ![模拟轨迹](https://github.com/user-attachments/assets/6889a71d-c0b4-4a83-9e88-565dc37c2cb5)

