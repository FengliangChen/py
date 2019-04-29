#!/usr/bin/env python3
# -*- coding:utf-8 -*- 



import os
import datetime
import re
import sys
import zipfile

CRED = '\033[91m'
CEND = '\033[0m'
CGRN = '\033[0;32m'

pub_path = "/Volumes/datavolumn_bmkserver_Pub/"
HOME = os.path.expanduser('~')
file_save_path = HOME + '/Desktop/' + 'final_art_work.txt'

def run():
    # global job
    while True:
        job = input("Please input job number: ")
        job = job.upper()
        if len(job) > 5 :
            break
        else:
            print("Job number should not be less than 6 digits")
    job_paths = Pub_job_path()
    if job_paths:
        folder_path = folder_search(job, job_paths)
        if folder_path:
            pdf_files = search_type(".pdf", folder_path)
            if not pdf_files:
                print(CRED+ "no pdf files!!" + CEND)
                sys.exit()
        else:
            print(CRED+ "Can't locate the job!!!" +CEND)
            sys.exit()
    final_text = handle_text(pdf_files)
    with open(file_save_path, 'w') as f:
        f.write(final_text)
    print(CGRN + "texts are ready now!!" + CEND)
    compress_option = input("Please enter y to process compress:")
    if compress_option is 'y' or  compress_option is 'Y':
        compress_file(folder_path)
        print(CGRN + "Completed, enjoy!!" + CEND)
    else:
        print(CGRN + "Pull of compression, completed!" + CEND)

def Pub_job_path():
    today = datetime.date.today()
    today_path = pub_path + today.strftime('%Y%m/%m%d')
    delta_yesterday = today + datetime.timedelta( days = -1 )
    yesterday_path = pub_path + delta_yesterday.strftime('%Y%m/%m%d')
    return (today_path, yesterday_path)

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

def search_type(file_type, path):
    files = os.listdir(path)
    match_files = []
    for file in files:
        m = re.search(file_type, file)
        if m:
            if file[0] != '.':
                match_files.append(file)
    return match_files

def compress_file(compress_path):
    compressed_name = os.path.split(compress_path)[1] + '_' +time_condition()
    fantasy_zip = zipfile.ZipFile(compress_path +'/'+ compressed_name + ".zip", 'w')
    for folder, subfolders, files in os.walk(compress_path):
        for file in files:
            if not file.endswith('.zip'):
                if file[0] != '.':
                    fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), compress_path), compress_type = zipfile.ZIP_DEFLATED)
    fantasy_zip.close()


def time_condition():
    time = datetime.datetime.now()
    today = datetime.date.today()
    time = int(time.hour)
    if time >= 7:
        return today.strftime( '%m%d')
    else:
        delta_time = today + datetime.timedelta( days = -1 )
        return delta_time.strftime( '%m%d')

def handle_text(file_name):
    file_text = ""
    file_name = sorted(file_name)
    for file in file_name:
        file_text = file_text + file[:-4] + '\n' 
    header_single = """
Hi Supplier,

Here is the final artwork for you following item, please confirm receipt.

Link:

"""
    header_plural = """
Hi Supplier,

Here are the final artwork for you following items, please confirm receipt.

Link:

"""
    claim = """
We have provided the files in 2 formats for you (Illustrator files, and PDF files). The artwork is exactly the same in each format, BUT they are for different purposes.
 
Illustrator format (AI files) --- these are for PRINTING ONLY - please send these to your PRINTER.
PDF format --- these are for your visual REFERENCE ONLY. These files are locked, so that no changes can be made. Do not mass print from the PDFs!

If you are looking for WMT approved printers, please feel free to contact us for a printing quote.
 
If you have any questions, or problems with the files, please don't hesitate to let us know, we’ll be happy to help.

IMPORTANT: The above download link will be available for 7 days. We will delete the files from the server at that time. If you do not download the files within 7 days, please contact us and we will re-upload the the server. There will be a 1 hour service fee to do this.

"""
    if len(file_name) == 1:
        return header_single + file_text + claim
    else:
        return header_plural + file_text+ claim



if __name__ == "__main__":
    run()



