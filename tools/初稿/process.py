#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

'''
 @Author      : Simon Chen
 @Email       : bafelem@gmail.com
 @datetime    : 2019-03-01 22:02:23
 @Description : Description
 @FileName    : process.py
'''

import datetime
import handle_txts
import os
import re
import search_jobs
import subprocess
import sys


CRED = '\033[91m'
CEND = '\033[0m'
CGRN = '\033[0;32m'

HOME = os.path.expanduser('~')
file_save_path = HOME + '/Desktop/' + 'draft_art_work.txt'

def run():
    global job
    while True:
        job = input("Please input job number: ")
        job = job.upper()
        if len(job) > 5 :
            break
        else:
            print("Job number should not be less than 6 digits")
    job_pf_txt_file_path = search_file()
    pf_txt_file = acquire_file(job_pf_txt_file_path)
    if len(pf_txt_file[0]) == 1: #be calful of this block.
        full_pf_path = os.path.join(str(job_pf_txt_file_path[0]), str(pf_txt_file[0][0]))
        pf_artwork_txt = handle_txts.handle_PF(full_pf_path)
    else:
        print("PF Error")
        return
    final_artwork_text = ''
    if pf_txt_file[1]:
        full_txt_paths = handle_txt_files(job_pf_txt_file_path[1],pf_txt_file[1])
        for txt_path in full_txt_paths:
            text_count = handle_txts.handle_txt(txt_path)
            final_artwork_text = final_artwork_text + handle_txts.header_part(text_count[1]) + text_count[0] + pf_artwork_txt
    else:
        fake_txt = search_jobs.search_type('.pdf', job_pf_txt_file_path[1])
        final_artwork_text = handle_txts.header_part(1) + '\n' + fake_txt[0][0:-4] + pf_artwork_txt
    with open(file_save_path, 'a') as f:
        f.write(final_artwork_text)
    subprocess.call(["open", job_pf_txt_file_path[1]])
    print(CGRN + "Good luck, Completed!" + CEND)

def search_file():
    pub_path = search_jobs.folder_search(job, search_jobs.Pub_job_path())
    pf_path = search_jobs.folder_search(job, search_jobs.PF_path())
    if pf_path == None:
        print(CRED + "Can't not find the PF." + CEND)
    if pub_path == None:
        print(CRED + "Can't not find the DF folder." + CEND)
    if pub_path and pf_path:
        print(pf_path)
        print(pub_path)
        return (pf_path, pub_path)
    else:
        sys.exit()


def acquire_file(paths):
    # paths = search_file()
    if paths:
        PF_excel = search_jobs.search_type('.xls',paths[0])
        if not PF_excel:
            PF_excel = search_jobs.search_type('.xlsx',paths[0])
            if not PF_excel:
                print("Check if PF is in the folder.")
                sys.exit()
        DF_txt = search_jobs.search_type('.txt', paths[1])
        if not DF_txt:
            print("txt file is not in the job folder.")
            pdf_files = search_jobs.search_type('.pdf', paths[1])
            if len(pdf_files) > 1:
                print("Multi pdfs and without txt files, end the process.")
                sys.exit()
            # needs work.
        return (PF_excel, DF_txt)
    else:
        print("acquire_file() is null")

def handle_txt_files(path, txts):
    full_path=[]
    for folder in txts:
        full_path.append(os.path.join(path,folder))
    return full_path





if __name__ == "__main__":
    run()
    
