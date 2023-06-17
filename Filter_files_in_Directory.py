
import os
from docx import Document

# write a function which can help you to filter only word or pdf file fom a directory

def filter_only_filename_exe(filepath,filetype):
    
    """ Argument filepath takes the directory path and argument filetype takes 
    the file extension like pdf or docx to read and disply all filenames present in the directory"""
    
    
    directory = filepath  # argument to pass the directory path
    # Iterate over each .docx file in the directory  
    for filename in os.listdir(directory):
        if filename.endswith("."+filetype):#argument to pass the type of file to filter
            print(filename)

filepath=input("Enter the file directory: ") #D:\Ranjith\BI\Harrow\Carer
filetype=input("Enter the file extension you want to filter[eg:pdf,docx]: ")# pdf


filter_only_filename_exe(filepath,filetype)