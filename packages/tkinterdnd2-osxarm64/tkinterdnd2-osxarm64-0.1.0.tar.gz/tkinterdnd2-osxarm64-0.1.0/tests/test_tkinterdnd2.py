import unittest

import tkinter
import tkinterdnd2

class TestStringMethods(unittest.TestCase):

    def test_version(self):
        root = tkinterdnd2.Tk()
        root.withdraw()
        self.assertEqual(root.TkdndVersion, '2.9.3')

if __name__ == '__main__':
    unittest.main()