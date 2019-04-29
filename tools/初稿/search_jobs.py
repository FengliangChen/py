#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

'''
 @Author      : Simon Chen
 @Email       : bafelem@gmail.com
 @datetime    : 2019-03-01 16:15:53
 @Description : Description
 @FileName    : search.py
'''

import os
import re
import datetime

pub_path = "/Volumes/datavolumn_bmkserver_Pub/"
wks_path = pub_path + "新做稿/未开始"
jxz_path = pub_path + "新做稿/进行中"


def folder_search(pattern, paths):
    for folder in paths:
        if os.path.exists(folder):
            for file in os.listdir(folder):
                m=re.search(pattern, file)
                # m=re.search('[\w]' + pattern, file)
                if m:
                    if file[0] != '.': 
                        return os.path.join(folder,file)
        else:
            continue
            # print("{} doesn't existed".format(folder))
            # return

def PF_path():
    return (wks_path, jxz_path)

def Pub_job_path():
    today = datetime.date.today()
    today_path = pub_path + today.strftime('%Y%m/%m%d')
    delta_yesterday = today + datetime.timedelta( days = -1 )
    yesterday_path = pub_path + delta_yesterday.strftime('%Y%m/%m%d')
    return (today_path, yesterday_path)

def search_type(file_type, path):
    files = os.listdir(path)
    match_files = []
    for file in files:
        m = re.search(file_type, file)
        if m:
            if file[0] != '.':
                match_files.append(file)
    return match_files


if __name__ == "__main__":
    k = folder_search("180277",Pub_job_path())
    CRED = '\033[91m'
    CEND = '\033[0m'
    print(CRED + "Error, does not compute!" + CEND)




