"""
Write your code here

Running this script should write a concatenation
of the pdfs in the <pdfs> folder in the <merge> folder

hint: use mstamy2's PyPDF2
"""


DESTINATION_MERGE = "merge/merge.pdf"

import os
import sys

from PyPDF2 import PdfFileMerger


folder = "pdfs"

documente = os.listdir(folder)

merger = PdfFileMerger()

for doc in documente:
    if not doc.endswith(".pdf"):
        continue

    input1 = open(os.path.join(folder, doc), 'rb')
    print(os.path.join(folder, doc))
    merger.append(input1)

output = open(DESTINATION_MERGE, "wb")
merger.write(output)
