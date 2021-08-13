import unittest
from Project import Project


class MyTestCase(unittest.TestCase):

    def test_project(self):
        p1 = Project('projectExample')
        self.assertListEqual(['projectExample/Class1.py', 'projectExample/Class2.py'], p1.get_py_file_list())


if __name__ == '__main__':
    unittest.main()
