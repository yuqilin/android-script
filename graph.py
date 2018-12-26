#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 yuqilin <yuqilin1228@gmail.com>
#

"""

"""

import os
import matplotlib.pyplot as plt
import csv
from datetime import datetime

csv_file = os.path.join(os.path.dirname(__file__), "mem_2018-12-26-184445.csv")
figure_file = os.path.join(os.path.dirname(__file__), "mem_graph.png")

# mem_info = {
# 	'java_heap' : [],
# 	'native_heap' : [],
# 	'code' : [],
# 	'stack' : [],
# 	'graphics' : [],
# 	'private_other' : [],
# 	'system' : [],
# 	'total' : []
# }

time = []
java_heap = []
native_heap = []
code = []
stack = []
graphics = []
private_other = []
system = []
total = []


with open(csv_file,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(plots, None)
    for row in plots:
        # data = row.split()
        # time.append(datetime.strptime(row[0], '%H:%M:%S'))
        time.append(row[0])
        java_heap.append(float(row[1]))
        native_heap.append(float(row[2]))
        # code.append(row[3])
        # stack.append(float(row[4]))
        graphics.append(float(row[5]))
        # private_other.append(float(row[6]))
        # system.append(float(row[7]))
        total.append(float(row[8]))

# print time
# print java_heap
# print native_heap
# print graphics
# print total

fig = plt.figure(figsize=(16,9), dpi=200)

plt.plot(time, java_heap, label='java_heap')
plt.plot(time, native_heap, label='native_heap')
# plt.plot(time, code, label='code')
# # plt.plot(time, stack, label='stack')
plt.plot(time, graphics, label='graphics')
# # plt.plot(time, private_other, label='private_other')
# # plt.plot(time, system, label='system')
plt.plot(time, total, label='total')
plt.xlabel('Time')
plt.ylabel('Memory (MB)')
plt.title('Trendline')

# fig.autofmt_xdate()
plt.xticks(rotation=90, fontsize=8)
# plt.tick_params(axis='both', which='major', labelsize=16)

# ax = plt.axis('equal')
# print ax

plt.legend(loc=1)
# plt.legend(bbox_to_anchor=(1, 1))

plt.tight_layout()


# plt.show()
plt.savefig(figure_file)
