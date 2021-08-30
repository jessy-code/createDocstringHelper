import unittest
from Project import Project
from Section import Section
from PythonFiles import PythonFiles, get_object_name_by_keyword
from Class import Class
from Function import Function


class MyTestCase(unittest.TestCase):

    def test_project(self):
        p1 = Project('projectExample')
        self.assertListEqual(['projectExample/Class1.py', 'projectExample/Class2.py'], p1.get_py_file_list())

        with self.assertRaises(FileNotFoundError):
            p2 = Project('doesnotexist')

    def test_section(self):
        param_list_example = ['param1', 'param2', 'param3']
        method_list_example = ['foo1', 'foo2']

        s1 = Section('Attributes')
        self.assertEqual(s1.get_section_title(), '\nAttributes\n__________')

        s2 = Section('Attributes', param_list_example)
        self.assertEqual(s2.get_writable_section(), '\nAttributes\n__________\nparam1 : <TO BE COMPLETED>\n\nparam2 : '
                                                    '<TO BE COMPLETED>\n\nparam3 : <TO BE COMPLETED>\n')

        s3 = Section('Parameters', param_list_example)
        self.assertEqual(s3.get_writable_section(), '\nParameters\n__________\nparam1 : <TO BE COMPLETED>\n\nparam2 : '
                                                    '<TO BE COMPLETED>\n\nparam3 : <TO BE COMPLETED>\n')

        s4 = Section('Methods', method_list_example)
        self.assertEqual(s4.get_writable_section(), '\nMethods\n_______\nfoo1 : <TO BE COMPLETED>\n\nfoo2 : '
                                                    '<TO BE COMPLETED>\n')

    def test_python_files(self):
        p1 = PythonFiles('projectExample/Class1.py')
        with open('projectExample/Class1.py', 'r') as file:
            file_content = file.readlines()
        self.assertListEqual(p1.get_python_file_content(), file_content)
        self.assertListEqual(get_object_name_by_keyword(p1.get_python_file_content(), 'class'), ['Class1'])

        with self.assertRaises(FileNotFoundError):
            p2 = PythonFiles('doesnotexist')

        p1.get_class_in_file()
        self.assertListEqual(p1.get_class_in_file(), [Class('Class1')])

        p2 = PythonFiles('projectExample/Class2.py')
        self.assertListEqual(p2.get_class_in_file(), [Class('Class2'), Class('Class3')])
        p2.get_function_in_file()
        self.assertListEqual(p2.get_function_in_file(), [Function('__init__'), Function('method1'), Function('method2'),
                                                         Function('method3'), Function('__init__'), Function('method1'),
                                                         Function('method2'), Function('method3'),
                                                         Function('output_function')])

    def test_class(self):
        param_list_example = ['param1', 'param2', 'param3']
        method_list_example = ['foo1', 'foo2']

        c1 = Class('ClassTest')
        c1.set_param_list(param_list_example)
        c1.set_attribute_list(param_list_example)
        c1.set_methode_list(method_list_example)

        c1.write_docstring()

        [self.assertIn(param, c1.get_docstring()) for param in param_list_example]
        [self.assertIn(methode, c1.get_docstring()) for methode in method_list_example]

    def test_function(self):
        param_list_example = ['param1', 'param2', 'param3']
        return_list_example = ['return1', 'return2']
        raise_list_example = ['AttributeError', 'ValueError']

        f1 = Function('function_test')
        f1.set_param_list(param_list_example)
        f1.set_returns(return_list_example)
        f1.set_raises(raise_list_example)

        f1.write_docstring()

        [self.assertIn(param, f1.get_docstring()) for param in param_list_example]
        [self.assertIn(cur_return, f1.get_docstring()) for cur_return in return_list_example]
        [self.assertIn(cur_raise, f1.get_docstring()) for cur_raise in raise_list_example]


if __name__ == '__main__':
    unittest.main()
