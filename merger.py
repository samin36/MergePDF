#!/usr/bin/env python
from PyPDF2 import PdfFileMerger
import tqdm
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, help="complete path of the folder with pdf files")
args = parser.parse_args()

path = args.path if args.path else os.getcwd()

path += "\\"

pdf_files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)) and file.endswith('.pdf') ]

if pdf_files:
    merger = PdfFileMerger()
    for files in pdf_files:
        print(f"Adding {files}...")
        merger.append(path + files)

    while True:
        file_name = input("Name of the merged file (or q to quit)-> ")
        if file_name == 'q':
            break
        elif ".pdf" not in file_name:
            file_name += ".pdf"

        if not os.path.exists(path + file_name):
            merger.write(path + file_name)
            print("PDFS merged successfully")
            break
        else:
            print("File with this name already exists")

    merger.close()
else:
    print(f"No PDFS in the directory: {path}")
