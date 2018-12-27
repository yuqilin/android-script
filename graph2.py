#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 yuqilin <yuqilin1228@gmail.com>
#

"""

"""
import pandas as pd

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import os
import getopt
import sys

import datetime
import numpy as np
import matplotlib.ticker as ticker

opts, args = getopt.getopt(sys.argv[1:], "")

input_file = args[0]
output_file = os.path.splitext(input_file)[0] + ".png"

# print input_file, output_file

# csv_file = input_file #os.path.join(os.path.dirname(__file__), input_file)

headers = ['time', 'java_heap', 'native_heap', 'code', 'stack', 'graphics', 'private_other', 'system', 'total']

dateparse = lambda x: pd.datetime.strptime(x, '%H:%M:%S')

data = pd.read_csv(input_file, parse_dates=['time'], date_parser=dateparse)

# data = pd.read_csv(input_file)

# times = []
# for time in data['time']:
    # time.append(datetime.strptime(time, '%H:%M:%S'))

# print "points : " + str(len(data))

# figure size 16:9, dpi 120
fig = plt.figure(figsize=(16,9), dpi=120)

# print data['time']

min = data['time'][0] - datetime.timedelta(seconds=10)
max = data['time'][len(data)-1] + datetime.timedelta(seconds=10)
print min, max

plt.plot(data['time'], data['java_heap'])
plt.plot(data['time'], data['native_heap'])
plt.plot(data['time'], data['graphics'])
plt.plot(data['time'], data['total'])

plt.xlabel('Time')
plt.ylabel('Memory')
plt.title('Memory Trendline')


plt.tick_params(which='both', direction='in')

ax = plt.gca()

ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
ax.xaxis.set_major_locator(mdates.SecondLocator(interval=20))
ax.xaxis.set_minor_locator(mdates.SecondLocator(interval=5))
# datemin = np.datetime64(r.date[0], 'Y')
# datemax = np.datetime64(r.date[-1], 'Y') + np.timedelta64(1, 'Y')

# N = len(data['time'])
# ax.set_xlim(min, max)

# ax.set_xticklabels(data['time'])

# next we'll write a custom formatter
# N = len(data['time'])
# ind = np.arange(N)  # the evenly spaced plot indices

# print N, ind

# def format_date(x, pos):
#     print x, pos
#     thisind = np.clip(int(x + 0.5), 0, N - 1)
#     return data['time'][thisind].strftime('%H:%M:%S')

# ax = plt.gca()
# ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))

# plt.tick_params(
#     which='both',      # both major and minor ticks are affected
#     direction='in')
# ,
#     bottom=True,      # ticks along the bottom edge are off
#     top=False,         # ticks along the top edge are off
#     labelbottom=True) # labels along the bottom edge are off
# plt.xticks(rotation=90)

fig.autofmt_xdate()  # 自动旋转日期标记

# plt.legend(bbox_to_anchor=(1, 1))
plt.legend(loc=1)

# plt.tight_layout()

plt.savefig(output_file)

