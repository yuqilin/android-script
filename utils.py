#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 yuqilin <yuqilin1228@gmail.com>
#

"""

"""

import os
import platform
import subprocess

# 判断系统类型，windows使用findstr，linux使用grep
system = platform.system()
if system is "Windows":
    find_util = "findstr"
else:
    find_util = "grep"

# 判断是否设置环境变量ANDROID_HOME
if "ANDROID_HOME" in os.environ:
    if system == "Windows":
        command = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb.exe")
    else:
        command = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb")
elif "ANDROID_SDK" in os.environ:
	if system == "Windows":
        command = os.path.join(os.environ["ANDROID_SDK"], "platform-tools", "adb.exe")
    else:
        command = os.path.join(os.environ["ANDROID_SDK"], "platform-tools", "adb")
else:
    raise EnvironmentError("adb not found !!!")

# 设备列表
def get_device_list():
    devices = []
    result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    result.reverse()
    for line in result[1:]:
        if "attached" not in line.strip():
            devices.append(line.split()[0])
        else:
            break
    return devices

# adb命令
def adb(args):
    global serialno_num
    if serialno_num == "":
        devices = get_device_list()
        if len(devices) == 1:
            #global serialno_num
            serialno_num = devices[0]
        else:
            root = tk.Tk()
            window = Window(devices, root)
            window.show_window()
    cmd = "%s -s %s %s" %(command, serialno_num, str(args))
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# adb shell命令
def shell(args):
    global serialno_num
    if serialno_num == "":
        devices = get_device_list()
        if len(devices) == 1:
            serialno_num = devices[0]
        else:
            root = tk.Tk()
            window = Window(devices, root)
            window.show_window()
    cmd = "%s -s %s shell %s" %(command, serialno_num, str(args))

    print(cmd)
    
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


