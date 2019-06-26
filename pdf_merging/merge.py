"""
Write your code here

Running this script should write a concatenation
of the pdfs in the <pdfs> folder in the <merge> folder

hint: use mstamy2's PyPDF2
"""

from PyPDF2 import PdfFileMerger
import os.path 


DESTINATION_MERGE = "merge/merge.pdf"
PDFS_FOLDER = "pdfs"
list_test = ['1.pdf','2.pdf','3.pdf','4.pdf']


def merge_pdf():
    mergePdf = PdfFileMerger()
    for i in range(4):
        
        s = os.path.join(PDFS_FOLDER,list_test[i])
    
        with open(os.path.join(PDFS_FOLDER,list_test[i]),'rb') as f:
            mergePdf.append(f)
    return mergePdf


merge_pdf_writer = merge_pdf()
output = open(DESTINATION_MERGE,"wb")
merge_pdf_writer.write(output)
