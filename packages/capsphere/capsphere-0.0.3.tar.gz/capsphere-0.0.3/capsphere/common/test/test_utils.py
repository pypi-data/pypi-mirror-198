import unittest
from capsphere.common.utils import get_file_format
from capsphere.common.test.resources.data import FILE_NAME_1, FILE_NAME_2, FILE_NAME_3


class TestUtils(unittest.TestCase):
    def test_valid_file_split(self):
        pdf_file = get_file_format(FILE_NAME_1)
        img_file = get_file_format(FILE_NAME_2)
        self.assertEqual(pdf_file, 'pdf')
        self.assertEqual(img_file, 'img')

    def test_invalid_file_split(self):
        with self.assertRaises(ValueError) as cm:
            get_file_format(FILE_NAME_3)
        self.assertEqual("Unrecognised filename format 'invalid.file.extension': "
                         "Unable to split strings",
                         str(cm.exception))



