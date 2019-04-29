#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

'''
 @Author      : Simon Chen
 @Email       : bafelem@gmail.com
 @datetime    : 2019-03-01 19:11:11
 @Description : Description
 @FileName    : read_xls.py
'''


import xlrd
import sys


def handle_txt(path):
    with open(path, 'r') as raw:
        raw_txt = raw.read()
    t=raw_txt.splitlines()
    count = 0
    new_texts = ''
    for line in t:
        if line != "":
            line = line.strip('.pdf')
            new_texts = new_texts + '\n' + line
            count = count + 1
    return (new_texts, count)

def header_part(count):
    header = 'Hi supplier,'
    if count == 1:
        first_line = "The following " + str(count) + " DRAFT ARTWORK FILE is for your first approval:"
    else:
        first_line = "The following " + str(count) + " DRAFT ARTWORK FILES are for your first approval:"
    return '\n' + header + '\n' + '\n' + first_line + '\n'

def handle_PF(path):
    data = xlrd.open_workbook(path)
    table=data.sheet_by_index(0)
    cell_A1=table.cell(4,7).value
    cell_A2=table.cell(5,7).value
    cell_A3=table.cell(6,7).value
    cell_A4=table.cell(7,7).value
    cell_A5=table.cell(8,7).value
    cell_A6=table.cell(9,7).value
    cell_A7=table.cell(10,7).value
    cell_A8=table.cell(11,7).value
    return '\n'+'\n'+cell_A1+'\n'+cell_A2+'\n'+cell_A3+'\n'+cell_A4+'\n'+cell_A5+'\n'+cell_A6+'\n'+cell_A7+'\n'+cell_A8+'\n'+'\n'+'\n'

def draft_artwork(txt_path, PF_path):
    texts = handle_txt(txt_path)
    return header_part(texts[1]) + texts[0] + handle_PF(PF_path)


if __name__ == "__main__":
    path_e = "/Users/imac-6/Desktop/U190311_DSL_DetailList_W.xls"
    path1 = "/Users/imac-6/Desktop/U181241_SES.txt"
    print(draft_artwork(path1, path_e))






