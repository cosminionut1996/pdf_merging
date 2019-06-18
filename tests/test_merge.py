import hashlib
import unittest

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

class TestMerge(unittest.TestCase):

    def test_result(self):
        merge_result_location = 'merge/merge.pdf'
        self.assertEqual(
            "e661d4ff8a10c1c2efacaae3bd217837",
            md5(merge_result_location)
        )

if __name__ == "__main__":
    unittest.main()
 