#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 yuqilin <yuqilin1228@gmail.com>
#

"""

"""
import pandas as pd

import matplotlib.pyplot as plt
import os
import getopt
import sys

opts, args = getopt.getopt(sys.argv[1:], "")

input_file = args[0]
output_file = os.path.splitext(input_file)[0] + ".png"

# print input_file, output_file

# csv_file = input_file #os.path.join(os.path.dirname(__file__), input_file)

headers = ['time', 'java_heap', 'native_heap', 'code', 'stack', 'graphics', 'private_other', 'system', 'total']

data = pd.read_csv(input_file)

# data = data[1:]

# print data

# figure size 16:9, dpi 120
fig = plt.figure(figsize=(16,9), dpi=120)


plt.plot(data['time'], data['java_heap'])
plt.plot(data['time'], data['native_heap'])
plt.plot(data['time'], data['graphics'])
plt.plot(data['time'], data['total'])

plt.xlabel('Time')
plt.ylabel('Memory')
plt.title('Memory Trendline')
plt.xticks(rotation=90)

# plt.legend(bbox_to_anchor=(1, 1))
plt.legend(loc=1)

plt.tight_layout()

plt.savefig(output_file)

