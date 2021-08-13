import unittest
from Project import Project
from Section import Section
from PythonFiles import PythonFiles


class MyTestCase(unittest.TestCase):

    def test_project(self):
        p1 = Project('projectExample')
        self.assertListEqual(['projectExample/Class1.py', 'projectExample/Class2.py'], p1.get_py_file_list())

        with self.assertRaises(FileNotFoundError):
            p2 = Project('doesnotexist')

    def test_section(self):
        s1 = Section('Attributes')
        print(s1.get_section_title())
        self.assertEqual(s1.get_section_title(), 'Attributes\n__________')

    def test_python_files(self):
        p1 = PythonFiles('projectExample/Class1.py')
        with open('projectExample/Class1.py', 'r') as file:
            file_content = file.readlines()
        self.assertListEqual(p1.get_python_file_content(), file_content)

        with self.assertRaises(FileNotFoundError):
            p2 = PythonFiles('doesnotexist')


if __name__ == '__main__':
    unittest.main()
