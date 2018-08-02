#!/usr/bin/env python3

# encoding: utf-8
# BY Simon Chen, bafelem@gmail.com
# Prepare the draft work texts, will need one txt for input and  one txt for output, the path on 
# Last released on 07/26/2018


import xlrd
import sys

path1 = sys.argv[1] + "/a.txt"
path2 = sys.argv[1] + "/draft_art_work.txt" # txt path for output.

def path3():
	if sys.argv[2] == "xls":
		return sys.argv[1] + "/a.xls"
	if sys.argv[2] == "xlsx":
		return sys.argv[1] + "/a.xlsx"

data = xlrd.open_workbook(path3())
table=data.sheet_by_index(0)

cell_A1=table.cell(4,7).value
cell_A2=table.cell(5,7).value
cell_A3=table.cell(6,7).value
cell_A4=table.cell(7,7).value
cell_A5=table.cell(8,7).value
cell_A6=table.cell(9,7).value
cell_A7=table.cell(10,7).value
cell_A8=table.cell(11,7).value

####################

with open(path1, 'r') as raw:
	raw_txt = raw.read()

t=raw_txt.splitlines()

def first_count():
	j = 0
	k = 0
	l =[]
	for line in t:
		if line != "":
			j += 1
			k =0
		elif line == "":
			k += 1
			if k == 1:
				l.extend([j])
			j = 0
	return l

l = first_count()

l = iter(l)	



def header_part(count):
	header = 'Hi supplier,'
	if count == 1:
		first_line = "The following " + str(count) + " DRAFT ARTWORK FILE is for your first approval:"
	else:
		first_line = "The following " + str(count) + " DRAFT ARTWORK FILES are for your first approval:"
	with open(path2, 'a') as f:
		f.write('\n'+header+'\n'+'\n'+first_line+'\n')

def print_line(text):
	text = text.strip('.pdf')
	with open(path2, 'a') as f:
		f.write('\n'+text)

def print_tail():
	with open(path2, 'a') as f:
		f.write('\n'+'\n'+cell_A1+'\n'+cell_A2+'\n'+cell_A3+'\n'+cell_A4+'\n'+cell_A5+'\n'+cell_A6+'\n'+cell_A7+'\n'+cell_A8+'\n'+'\n'+'\n')

j = 0
k = 0

for line in t:
	if line != "":
		j += 1
		k =0
		if j == 1:
			try:
				lines_count = 0
				lines_count = next(l)
			except StopIteration:
				pass
			header_part(lines_count)
		print_line(line)
	elif line == "": # So there must be break lines at the end of the a.txt file then it can proceed the condition.
		k += 1
		if k == 1:
			print_tail()
		j = 0


print("Completed! Enjoy!")

exit()