#! /bin/sh
#
# adb-mem.sh
# 
# Created by yuqilin on 12/26/2018
# Copyright (C) 2018 yuqilin <yuqilin1228@gmail.com>
#


PKG_NAME=
CURRENT_ACTIVITY=

# get current app package name
function get_app_id() {
	if [ -z "$PKG_NAME" ]; then
		PKG_NAME=`adb shell dumpsys window w | grep \/ | grep name= | cut -d = -f 3 | cut -d / -f 1`
	fi
}

function get_current_activity() {
	CURRENT_ACTIVITY=`adb shell dumpsys window w | grep \/ | grep name= | cut -d = -f 3 | cut -d \) -f 1`
}

function dumpmem() {
    adb shell dumpsys meminfo $PKG_NAME
}

CSV_NAME=mem_$(date +%F-%H%M%S).csv

echo CSV_NAME=$CSV_NAME

function write_csv_header() {
	echo "time,java_heap,native_heap,code,stack,graphics,private_other,system,total" > $CSV_NAME
}

function write_csv_line() {
	time=$(date +%H:%M:%S)
	echo "$time,$java_heap,$native_heap,$code,$stack,$graphics,$private_other,$system,$total" >> $CSV_NAME
}


JAVA_HEAP_PATTERN="Java Heap:"
NATIVE_HEAP_PATTERN="Native Heap:"
CODE_PATTERN="Code:"
STACK_PATTERN="Stack:"
GRAPHICS_PATTERN="Graphics:"
PRIVATE_OTHER_PATTERN="Private Other:"
SYSTEM_PATTERN="System:"
TOTAL_PATTERN="TOTAL:"


get_app_id

write_csv_header

while [ true ]; do

# dumpmem | grep --color -E 'Java Heap:|Native Heap:|Code:|Stack:|Graphics:|Private Other:|System:|TOTAL:'

MEMINFO="$(adb shell dumpsys meminfo $PKG_NAME)"

java_heap=`echo "$MEMINFO" | grep "$JAVA_HEAP_PATTERN" | awk -F ':' '{print $2}' |sed s/[[:space:]]//g`
native_heap=`echo "$MEMINFO" | grep "$NATIVE_HEAP_PATTERN" | awk -F ':' '{print $2}' |sed s/[[:space:]]//g`
code=`echo "$MEMINFO" | grep "$CODE_PATTERN" | awk -F ':' '{print $2}' |sed s/[[:space:]]//g`
stack=`echo "$MEMINFO" | grep "$STACK_PATTERN" | awk -F ':' '{print $2}' |sed s/[[:space:]]//g`
graphics=`echo "$MEMINFO" | grep "$GRAPHICS_PATTERN" | awk -F ':' '{print $2}' |sed s/[[:space:]]//g`
private_other=`echo "$MEMINFO" | grep "$PRIVATE_OTHER_PATTERN" | awk -F ':' '{print $2}' |sed s/[[:space:]]//g`
system=`echo "$MEMINFO" | grep "$SYSTEM_PATTERN" | awk -F ':' '{print $2}' |sed s/[[:space:]]//g`
total=`echo "$MEMINFO" | grep "$TOTAL_PATTERN" | awk -F ' ' '{print $2}' |sed s/[[:space:]]//g`

java_heap=`awk 'BEGIN{printf "%.2f\n", '$java_heap'/1000}'`
native_heap=`awk 'BEGIN{printf "%.2f\n", '$native_heap'/1000}'`
code=`awk 'BEGIN{printf "%.2f\n", '$code'/1000}'`
stack=`awk 'BEGIN{printf "%.2f\n", '$stack'/1000}'`
graphics=`awk 'BEGIN{printf "%.2f\n", '$graphics'/1000}'`
private_other=`awk 'BEGIN{printf "%.2f\n", '$private_other'/1000}'`
system=`awk 'BEGIN{printf "%.2f\n", '$system'/1000}'`
total=`awk 'BEGIN{printf "%.2f\n", '$total'/1000}'`

printf "java_heap=%6.2fMB, native_heap=%7.2fMB, code=%6.2fMB, stack=%5.2fMB, graphics=%7.2fMB, private_other=%6.2fMB, system=%7.2fMB, total=%7.2fMB\n" $java_heap $native_heap $code $stack $graphics $private_other $system $total
# echo "java_heap=$java_heap, native_heap=$native_heap, code=$code, stack=$stack, graphics=$graphics, private_other=$private_other, system=$system, total=$total"

write_csv_line

sleep 2

done
