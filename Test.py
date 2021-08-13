import unittest
from Project import Project
from Section import Section
from PythonFiles import PythonFiles, get_object_name_by_keyword
from Class import Class


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
        self.assertListEqual(get_object_name_by_keyword(p1.get_python_file_content(),'class'), ['Class1'])

        with self.assertRaises(FileNotFoundError):
            p2 = PythonFiles('doesnotexist')

        p1.get_class_in_file()
        self.assertListEqual(p1.get_class_in_file(), [Class('Class1')])

        p2 = PythonFiles('projectExample/Class2.py')
        self.assertListEqual(p2.get_class_in_file(), [Class('Class2'), Class('Class3')])


if __name__ == '__main__':
    unittest.main()
