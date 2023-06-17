   # Function by which you will be able to append two PDF files
import os 
from PyPDF2 import PdfMerger

def read_pdf_file_append(directory_path,outputfile):
    """ This function takes  1st argument as directory path where the pdf files to read and 2nd argument as the file path to store your mergend pdf file"""

    directory = directory_path # D:\\London\\BI\\council\\Carer 
    output_file = outputfile # D:\\London\\BI\\council\\Carer\\pdfmerge\\merged.pdf

    # Create a PdfMerger object
    pdf_merger = PdfMerger()

    # Iterate over each .csv file in the directory  
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            file_path = os.path.join(directory, filename)

             # Add the PDF file to the merger
            pdf_merger.append(file_path)

    # Write the merged PDF to the output file
    with open(output_file, "wb") as output:
        pdf_merger.write(output)

    print(f"Data from .pdf files appended to '{output_file}'")  

directory_path = input("Enter the directory filepath to read : ")  # D:\London\BI\council\Carer                   
outputfile = input("Enter the filepath to store the appended pdf file: ") #D:\London\BI\council\Carer\pdfmerge\merged2.pdf

read_pdf_file_append(directory_path,outputfile) 