"""
Write your code here

Running this script should write a concatenation
of the pdfs in the <pdfs> folder in the <merge> folder

hint: use mstamy2's PyPDF2
"""

import PyPDF2

from sys import stderr, stdout, exit
import os
import traceback
from collections import defaultdict

from PyPDF2 import PdfFileMerger, parse_filename_page_ranges

DESTINATION_MERGE = "merge/merge.pdf"
PDFS_FOLDER = "pdfs"


if __name__ == "__main__":
	merger = PdfFileMerger()
	filePath = PDFS_FOLDER
	
	filename_page_ranges = parse_filename_page_ranges(os.listdir(PDFS_FOLDER))
	for (filename, page_range) in filename_page_ranges:
		#print(filename, page_range)
		fp = open(filePath + '/' + filename, "rb")
		merger.append(fp, pages=page_range)
		fp.close()

	output = open(DESTINATION_MERGE, 'wb')
	merger.write(output)
	output.close()
		


