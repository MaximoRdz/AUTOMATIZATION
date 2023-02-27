import unittest
import os
from rename_files import rename_txt


class RenameTest(unittest.TestCase):
    def setUp(self):
        # create temporal directory with files to rename
        self.path = os.path.join(os.getcwd(), 'temp_dir')
        os.mkdir(self.path)
        self.file1 = os.path.join(self.path, 'file1.txt')
        self.file2 = os.path.join(self.path, 'file2.txt')
        with open(self.file1, 'w') as f:
            f.write('test')
        with open(self.file2, 'w') as f:
            f.write('test')

    def test(self):
        # test the files exist
        self.assertTrue(os.path.exists(self.file1))
        self.assertTrue(os.path.exists(self.file2))
        rename_txt(self.path, 'new_')
        # check they have been rename
        self.assertTrue(not os.path.exists(self.file1))
        self.assertTrue(not os.path.exists(self.file2))
        # check they have been rename correctly
        self.new_file1 = os.path.join(self.path, 'new_file1.txt')
        self.assertTrue(self.new_file1)
        self.new_file2 = os.path.join(self.path, 'new_file2.txt')
        self.assertTrue(self.new_file2)
        # remove temporary files and dirs
        os.remove(self.new_file1)
        os.remove(self.new_file2)
        os.rmdir(self.path)


if __name__ == '__main__':
    unittest.main()
