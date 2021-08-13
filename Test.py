import unittest
from Project import Project
from Section import Section


class MyTestCase(unittest.TestCase):

    def test_project(self):
        p1 = Project('projectExample')
        self.assertListEqual(['projectExample/Class1.py', 'projectExample/Class2.py'], p1.get_py_file_list())

    def test_section(self):
        s1 = Section('Attributes')
        print(s1.get_section_title())
        self.assertEqual(s1.get_section_title(), 'Attributes\n__________')


if __name__ == '__main__':
    unittest.main()
