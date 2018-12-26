#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 yuqilin <yuqilin1228@gmail.com>
#

"""

"""



class MemInfo(Info):
    TIME = "time"
    JAVA_HEAP = "java-heap"
    NATIVE_HEAP = "native-heap"
    CODE = "code"
    STACK = "stack"
    GRAPHICS = "graphics"
    PRIVATE_OTHER = "private-other"
    SYSTEM = "system"
    TOTAL = "total-pss"

    def __init__(self):
        super().__init__()
        self.count = 1
        self.is_running = True

    def get_start_info(self):
        t = threading.Thread(target=self.get_mem_info)
        t.start()

    def get_end_info(self):
        self.is_running = False

    def get_mem_info(self):
        print("====== get_mem_info =======")
        dirs = self.task.output + "/mem_stats/"
        file_name = "mem_" + self.task.device + "_" + self.task.applicationid + "_" + self.task.version_name + "_" + self.task.name
        field_names = [self.TIME, self.JAVA_HEAP, self.NATIVE_HEAP, self.CODE, self.STACK, self.GRAPHICS, self.PRIVATE_OTHER, self.SYSTEM]
        writer = utils.get_csv_writer(dirs, file_name, field_names)
        while self.is_running:
            java_heap_info = self.task.d.adb_shell("dumpsys meminfo " + self.task.pid + " | grep 'Java Heap:'")
            java_heap_pss = format(int(re.findall(r"\d+", java_heap_info)[0]) / 1000.0, ".2f")
            native_heap_info = self.task.d.adb_shell("dumpsys meminfo " + self.task.pid + " | grep 'Native Heap:'")
            native_heap_pss = format(int(re.findall(r"\d+", native_heap_info)[0]) / 1000.0, ".2f")
            code_info = self.task.d.adb_shell("dumpsys meminfo " + self.task.pid + " | grep 'Code:'")
            code_pss = format(int(re.findall(r"\d+", code_info)[0]) / 1000.0, ".2f")
            stack_info = self.task.d.adb_shell("dumpsys meminfo " + self.task.pid + " | grep 'Stack:'")
            stack_pss = format(int(re.findall(r"\d+", stack_info)[0]) / 1000.0, ".2f")
            graphics_info = self.task.d.adb_shell("dumpsys meminfo " + self.task.pid + " | grep 'Graphics:'")
            graphics_pss = format(int(re.findall(r"\d+", graphics_info)[0]) / 1000.0, ".2f")
            private_other_info = self.task.d.adb_shell("dumpsys meminfo " + self.task.pid + " | grep 'Private Other:'")
            private_other_pss = format(int(re.findall(r"\d+", private_other_info)[0]) / 1000.0, ".2f")
            system_info = self.task.d.adb_shell("dumpsys meminfo " + self.task.pid + " | grep 'System:'")
            system_pss = format(int(re.findall(r"\d+", system_info)[0]) / 1000.0, ".2f")
            # total_info = self.task.d.adb_shell("dumpsys meminfo " + self.task.pid + " | grep 'TOTAL:'")
            # total_pss = format(int(re.findall(r"\d+", total_info)[0]) / 1000.0, ".2f")
            writer.writerow(
                {
                self.TIME: self.get_index(),
                self.JAVA_HEAP: java_heap_pss,
                self.NATIVE_HEAP: native_heap_pss,
                self.CODE: code_pss,
                self.STACK: stack_pss,
                self.GRAPHICS: graphics_pss,
                self.PRIVATE_OTHER: private_other_pss,
                self.SYSTEM: system_pss
                # self.TOTAL: total_pss
                 })
            self.count += 1
            time.sleep(self.task.interval)