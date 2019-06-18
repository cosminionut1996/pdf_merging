import hashlib
import unittest
from PyPDF2 import PdfFileReader

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

class TestMerge(unittest.TestCase):

    def test_result(self):
        merge_result_location = 'merge/merge.pdf'
        with open(merge_result_location,'rb') as handler:
            pdf = PdfFileReader(handler)
            pages = pdf.getNumPages()
            self.assertEqual(pages, 66)

if __name__ == "__main__":
    unittest.main()
 