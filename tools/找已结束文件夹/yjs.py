#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

'''
 @Author      : Simon Chen
 @Email       : bafelem@gmail.com
 @datetime    : 2019-03-25 15:28:30
 @Description : Description
 @FileName    : test.py
'''

import os
import re
import sys
import subprocess

jobs = []
val = [True]
pattern='[BCPTU][\d]{4}[0-9A-Z]{2}[_][A-Z]{3}'
path = "/Volumes/datavolumn_bmkserver_Pub/新做稿/已结束/WMT_Case"
pattern_job = input("Please enter your job:")


def jobsearch(path):
	# pattern_job = input("Please enter your job:")
	files = os.listdir(path)
	for file in files:
		if re.match(pattern, file):
			pass
			jobs.append(file)
			print(path + '/' + file)
			if re.search(pattern_job,file):
				subprocess.call(["open", os.path.join(path,file)])
				val[0] = False
				return
		else:
			if val[0]:
				new_path = os.path.join(path, file)
				if os.path.isdir(new_path):
					jobsearch(new_path)

jobsearch(path)

