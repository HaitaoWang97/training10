# -*- coding: utf-8 -*-
"""Tensor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RoCnhXHokH7rP70yvXmAfBHIW11IGU_v
"""

from __future__ import print_function
import torch as t

#构建5*3矩阵，只是分配了空间，未初始化
x = t.Tensor(5, 3)
x

#使用[0,1]均匀分布随机初始化二维数组
x = t.rand(5, 3)
x

print(x.size())#查看x的形状
x.size(0), x.size(1)#查看列的个数

#加法
y = t.rand(5, 3)
x + y

t.add(x, y)

#指定加法输出的结果赋给某个变量
result = t.Tensor(5, 3) #分配空间
t.add(x, y, out=result)
result

print('最初y')
print(y)

print('第一种加法， y的结果')
y.add(x) #函数不加下划线返回一个新的Tensor，不改变y的值
print(y)

print('第二种加法，y的结果')
y.add_(x) #函数加下划线，会修改Tensor原本的值
print(y)

x[:, 1] #Tensor的选取操作

# Tensor与numpy格式的转换
a = t.ones(5)
a

b = a.numpy()
b

import numpy as np
a= np.ones(5)
b= t.from_numpy(a) 
print(a)
print(b)

#Tensor与numpy共享内存，同时发生变化
b.add_(1)
print(b)
print(a)

#Tensor可以通过.cuda转换为GPU的Tensor，可加速计算

x = x.cuda()
y = y.cuda()
x + y