import unittest
from pathlib import Path

from co2data.pdf.helpers import get_nr_of_pages_imagemagick, get_nr_of_pages_pypdf2


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.test_file = Path("../../dav_bills/F992687_Alpenverein.pdf")

    def test_number_of_pages_imagemagick(self):
        with self.test_file.open("br") as file_handle:
            nr_pages = get_nr_of_pages_imagemagick(file_handle)
        self.assertEqual(nr_pages, 12)

    def test_number_of_pages_pypdf2(self):
        with self.test_file.open("br") as file_handle:
            nr_pages = get_nr_of_pages_pypdf2(file_handle)
        self.assertEqual(nr_pages, 12)



if __name__ == '__main__':
    unittest.main()
