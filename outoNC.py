#coding=utf-8
#!/usr/bin/env python3
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import os
import time

#定义读取文件函数

nc_file = os.path.join(os.path.dirname(__file__), "mem_2018-12-26-184445.csv")
figure_file = os.path.join(os.path.dirname(__file__), "mem_graph2.png")
 
headers = ['time', 'java_heap', 'native_heap', 'code', 'stack', 'graphics', 'private_other', 'system', 'total']

data = pd.read_csv(nc_file, names=headers)
# print data
data.time = pd.to_datetime(data.time)
plt.plot(data['time'], data['java_heap'])
# , 'native_heap', 'code', 'stack', 'graphics', 'private_other', 'system', 'total'])
plt.xlabel('Time')
plt.ylabel('Memory')
plt.title('Memory Trendline')
plt.savefig(figure_file)

# def read_data(file_path):
# #columa_names所有列表的名称
#     data = pd.read_csv(nc_file, names=headers)
#     # column_names = colums
#     # data.columns = colums
#     # data.head(3)
#     return data

# #画图线性图
# def huatu(x,y):
#     data = read_data(nc_file)
#     data.plot(x = 'time',y =['java_heap', 'native_heap', 'code', 'stack', 'graphics', 'private_other', 'system', 'total'])
# #def simple_line_plot(x,y,figure_no):
#     # plt.figure(figure_no)
#     plt.plot(x,y)
#     plt.xlabel('Time')
#     plt.ylabel('Memory')
#     plt.title('Memory Trendline')
#     plt.savefig(figure_file)

# #调用函数读取数据
# #os.system('bash /Users/jafferlin/memdump/vivo.sh')
# #time.sleep (1800)
# dataset = read_data(nc_file)
# figure_no=1
# # x=dataset['time']
# # y=dataset['native']
# huatu(x,y)
# #simple_line_plot(x,y,figure_no)
# #plt.show()
# plt.savefig(figure_file)
