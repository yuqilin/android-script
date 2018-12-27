#! /bin/sh
#
# graph.sh
# 
# Created by yuqilin on 12/26/2018
# Copyright (C) 2018 yuqilin <yuqilin1228@gmail.com>
#

LATEST_CSV=`ls -lt *.csv | head -n 1 | awk -F ' ' '{print $NF}'`

if [ ! -z "$1" ]; then
	LATEST_CSV="$1"
fi

if [ ! -z "$LATEST_CSV" ]; then

	# python graph.py "$LATEST_CSV"
	python graph2.py "$LATEST_CSV"

fi