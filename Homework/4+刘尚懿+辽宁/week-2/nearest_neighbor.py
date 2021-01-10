import matplotlib.pyplot as plt
import numpy as np


def nearest_neighbor(input_signal, zoom_multiples):
    '''
	最近邻插值（适用于灰度图）
	:param input_signal: 输入图像
	:param zoom_multiples:  缩放倍数
	:return: 缩放后的图像
	'''
    input_signal_cp = np.copy(input_signal)  # 输入图像的副本

    input_row, input_col = input_signal_cp.shape  # 输入图像的尺寸（行、列）

    # 输出图像的尺寸
    output_row = int(input_row * zoom_multiples[0])
    output_col = int(input_col * zoom_multiples[1])

    output_signal = np.zeros((output_row, output_col))  # 输出图片

    for i in range(output_row):
        for j in range(output_col):
            # 输出图片中坐标 （i，j）对应至输入图片中的（m，n）
            m = round(i / output_row * input_row)
            n = round(j / output_col * input_col)
            # 防止四舍五入后越界
            if m >= input_row:
                m = input_row - 1
            if n >= input_col:
                n = input_col - 1
            # 插值
            output_signal[i, j] = input_signal_cp[m, n]

    return output_signal


a = np.array([[2, 5, 15], [3, 10, 19]], dtype='float')
b = nearest_neighbor(a, (1, 3))
print(a)
plt.imshow(a)
plt.show()
print(b)
plt.imshow(b)
plt.show()
