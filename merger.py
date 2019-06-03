#!/usr/bin/env python
from PyPDF2 import PdfFileMerger
import tqdm
import os

path = os.getcwd() + "\\"
pdf_files = [file for file in os.listdir(path) if os.path.isfile(file) and file.endswith('.pdf') ]

if pdf_files:
    merger = PdfFileMerger()
    for files in pdf_files:
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
    print(f"No PDFS in the current directory: {os.getcwd()}")
