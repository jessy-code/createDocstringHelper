import unittest
from Project import Project
from Section import Section
from PythonFiles import PythonFiles
from Class import Class
from Function import Function
from shutil import copytree, rmtree
from os.path import isdir
from OverallFunctions import get_object_name_by_keyword, test_regex, extract_name_in_line


def read_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readlines()

    except FileNotFoundError:
        print(file_path + ' not found')
        raise


class MyTestCase(unittest.TestCase):

    def test_project(self):
        p1 = Project('tests/Initial_project_example')
        real_list_file = ['tests/Initial_project_example/OneClassFileExample.py',
                          'tests/Initial_project_example/SeveralClassFileExample.py',
                          'tests/Initial_project_example/OnlyAClassFileExample.py']
        list_file_get_by_function = p1.get_py_file_list()

        real_list_file.sort()
        list_file_get_by_function.sort()

        self.assertListEqual(real_list_file, list_file_get_by_function)

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
        p1 = PythonFiles('tests/Initial_project_example/OneClassFileExample.py')
        with open('tests/Initial_project_example/OneClassFileExample.py', 'r') as file:
            file_content = file.readlines()
        self.assertListEqual(p1.get_python_file_content(), file_content)
        self.assertListEqual(get_object_name_by_keyword(p1.get_python_file_content(), 'class'), ['Class1'])

        with self.assertRaises(FileNotFoundError):
            p2 = PythonFiles('doesnotexist')

        p1.get_class_in_file()
        self.assertDictEqual(p1.get_class_in_file(), {'Class1': Class('Class1')})

        p2 = PythonFiles('tests/Initial_project_example/SeveralClassFileExample.py')
        self.assertDictEqual(p2.get_class_in_file(), {'Class2': Class('Class2'), 'Class3': Class('Class3')})

        p2.get_function_in_file()
        self.assertDictEqual(p2.get_function_in_file(), {'output_function': Function('output_function'),
                                                         'output_function2': Function('output_function2'),
                                                         'output_function3': Function('output_function3'),
                                                         'output_function4': Function('output_function4'),
                                                         'other_function': Function('other_function'),
                                                         'another_one': Function('another_one'),
                                                         'new_test_function': Function('new_test_function'),
                                                         'empty_function': Function('empty_function')
                                                         })

    def test_get_function_content_python_file(self):
        p2 = PythonFiles('tests/Initial_project_example/SeveralClassFileExample.py')
        p2.get_function_in_file()

        p2.get_first_level_function_content('output_function')
        p2.get_first_level_function_content('other_function')
        p2.get_first_level_function_content('another_one')

        self.assertListEqual(p2.get_function_dict()['output_function'].content,
                             read_file_content('tests/object_contents/output_function.py'))

        self.assertListEqual(p2.get_function_dict()['other_function'].content,
                             read_file_content('tests/object_contents/other_function.py'))

        self.assertListEqual(p2.get_function_dict()['another_one'].content,
                             read_file_content('tests/object_contents/another_one.py'))

    def test_get_class_content(self):
        p1 = PythonFiles('tests/Initial_project_example/OneClassFileExample.py')
        p2 = PythonFiles('tests/Initial_project_example/SeveralClassFileExample.py')
        p4 = PythonFiles('tests/Initial_project_example/OnlyAClassFileExample.py')

        test_class1_list = ['Class1']
        test_class2_list = ['Class2', 'Class3']
        test_class4_list = ['Class4']

        p1.get_class_in_file()
        p2.get_class_in_file()
        p4.get_class_in_file()

        python_file_list = [p1, p2, p4]

        [p1.get_class_content(class_name) for class_name in test_class1_list]
        [p2.get_class_content(class_name) for class_name in test_class2_list]
        [p4.get_class_content(class_name) for class_name in test_class4_list]

        for python_file in python_file_list:
            for class_name in python_file.get_class_dict().keys():
                content = []
                try:
                    with open('tests/object_contents/' + class_name + '.py', 'r') as file:
                        content = file.readlines()
                except (FileNotFoundError, FileExistsError):
                    pass
                self.assertListEqual(content, python_file.get_class_dict()[class_name].content)

    def test_function_param_list_from_content(self):
        p2 = PythonFiles('tests/Initial_project_example/SeveralClassFileExample.py')
        test_func_list = ['other_function',
                          'output_function',
                          'output_function2',
                          'output_function3',
                          'output_function4',
                          'another_one',
                          'new_test_function',
                          'empty_function']

        func_dict = p2.get_function_in_file()

        [p2.get_first_level_function_content(func) for func in test_func_list]
        [func.get_param_list_from_content() for func in func_dict.values()
         if func.get_function_name() in test_func_list]

        self.assertListEqual(p2.get_function_dict()['output_function'].get_param_list(), ['file_path'])
        self.assertListEqual(p2.get_function_dict()['output_function2'].get_param_list(), ['file_path'])
        self.assertListEqual(p2.get_function_dict()['output_function3'].get_param_list(), ['file_path'])
        self.assertListEqual(p2.get_function_dict()['output_function4'].get_param_list(), ['file_path'])
        self.assertListEqual(p2.get_function_dict()['other_function'].get_param_list(), ['param1', "param2='foo'"])
        self.assertListEqual(p2.get_function_dict()['another_one'].get_param_list(), [])
        self.assertListEqual(p2.get_function_dict()['new_test_function'].get_param_list(), ['param1', 'param2'])
        self.assertListEqual(p2.get_function_dict()['empty_function'].get_param_list(), ['param'])

    def test_get_return_list_from_content(self):
        p2 = PythonFiles('tests/Initial_project_example/SeveralClassFileExample.py')
        func_dict = p2.get_function_in_file()

        p2.get_first_level_function_content('output_function')
        p2.get_first_level_function_content('other_function')
        p2.get_first_level_function_content('another_one')
        p2.get_first_level_function_content('new_test_function')
        p2.get_first_level_function_content('empty_function')

        [func.get_return_list_from_content() for func in func_dict.values()]

        self.assertListEqual(p2.get_function_dict()['output_function'].get_returns(), ['file_path'])
        self.assertListEqual(p2.get_function_dict()['other_function'].get_returns(), ['param1', 'param2'])
        self.assertListEqual(p2.get_function_dict()['another_one'].get_returns(), [])
        self.assertListEqual(p2.get_function_dict()['new_test_function'].get_returns(), ['param1', 'param2'])
        self.assertListEqual(p2.get_function_dict()['empty_function'].get_returns(), [])

    def test_get_raises_from_content(self):
        p2 = PythonFiles('tests/Initial_project_example/SeveralClassFileExample.py')
        func_dict = p2.get_function_in_file()

        test_function_list = ['output_function',
                              'output_function2',
                              'output_function3',
                              'output_function4',
                              'new_test_function']

        [p2.get_first_level_function_content(func) for func in test_function_list]
        [p2.get_function_dict()[func].get_raises_from_content() for func in test_function_list]

        self.assertListEqual(p2.get_function_dict()['output_function'].get_raises(), ['FileNotFoundError'])
        self.assertListEqual(p2.get_function_dict()['output_function2'].get_raises(), ['FileNotFoundError'])
        self.assertListEqual(p2.get_function_dict()['output_function3'].get_raises(), [])
        self.assertListEqual(p2.get_function_dict()['output_function4'].get_raises(), ['FileNotFoundError',
                                                                                       'FileExistsError',
                                                                                       'IndexError'])
        self.assertListEqual(p2.get_function_dict()['new_test_function'].get_raises(), [])

    def test_write_first_level_function_docstring(self):
        if isdir('tests/modified_project_example'):
            rmtree('tests/modified_project_example')
        copytree('tests/Initial_project_example', 'tests/modified_project_example')

        p2 = PythonFiles('tests/modified_project_example/SeveralClassFileExample.py')
        p2.get_function_in_file()
        p2.write_first_level_function_docstring()

        documented_function_file = PythonFiles('tests/documented_project/SeveralClassFileExample.py')
        documented_function_file.get_function_in_file()

        [documented_function_file.get_first_level_function_content(func)
         for func in documented_function_file.get_function_dict().keys()]
        [self.assertListEqual(p2.get_function_dict()[func].content,
                              documented_function_file.get_function_dict()[func].content)
         for func in p2.get_function_dict().keys()]

        rmtree('tests/modified_project_example')

    def test_class(self):
        param_list_example = ['param1', 'param2', 'param3']

        c1 = Class('ClassTest')
        c1.set_param_list(param_list_example)

        c1.write_docstring()

        [self.assertIn(param, c1.get_docstring()) for param in param_list_example]

    def test_function(self):
        param_list_example = ['param1', 'param2', 'param3']
        return_list_example = ['return1', 'return2']
        raise_list_example = ['AttributeError', 'ValueError']

        f1 = Function('function_test')
        f1.set_param_list(param_list_example)
        f1.set_returns(return_list_example)
        f1.set_raises(raise_list_example)

        f1.content = ['def test():\n', '    print("hello")']

        f1.write_docstring()

        [self.assertIn(param, f1.get_docstring()) for param in param_list_example]
        [self.assertIn(cur_return, f1.get_docstring()) for cur_return in return_list_example]
        [self.assertIn(cur_raise, f1.get_docstring()) for cur_raise in raise_list_example]

    def test_test_regex(self):
        self.assertIsNotNone(test_regex('   class Class1:   ', 'class'))
        self.assertIsNotNone(test_regex("   def method3(self, param2, param3='foo'):    ", 'def'))

        self.assertIsNone(test_regex('   class Class1:   lsdjfq', 'class'))
        self.assertIsNone(test_regex("   def method3(self, param2, param3='foo'):    qsdfjsf", 'def'))

    def test_extract_name_in_line(self):
        self.assertEqual(extract_name_in_line('   class Class1:   lsdjfq'), 'Class1')
        self.assertEqual(extract_name_in_line("   def method3(self, param2, param3='foo'):    qsdfjsf"), 'method3')

    def test_get_class_content(self):
        p1 = PythonFiles('tests/Initial_project_example/OneClassFileExample.py')
        p2 = PythonFiles('tests/Initial_project_example/SeveralClassFileExample.py')
        p4 = PythonFiles('tests/Initial_project_example/OnlyAClassFileExample.py')

        test_class1_list = ['Class1']
        test_class2_list = ['Class2', 'Class3']
        test_class4_list = ['Class4']

        p1.get_class_in_file()
        p2.get_class_in_file()
        p4.get_class_in_file()

        python_file_list = [p1, p2, p4]

        [p1.get_class_content(class_name) for class_name in test_class1_list]
        [p2.get_class_content(class_name) for class_name in test_class2_list]
        [p4.get_class_content(class_name) for class_name in test_class4_list]

        for python_file in python_file_list:
            for class_name in python_file.get_class_dict().keys():
                content = []
                try:
                    with open('tests/object_contents/' + class_name + '.py', 'r') as file:
                        content = file.readlines()
                except (FileNotFoundError, FileExistsError):
                    pass
                self.assertListEqual(content, python_file.get_class_dict()[class_name].content)

    def test_get_function_in_class(self):
        methods_class = ['__init__', 'method1', 'method2', 'method3']

        p1 = PythonFiles('tests/Initial_project_example/SeveralClassFileExample.py')
        p1.get_class_in_file()

        [p1.get_class_content(class_name) for class_name in p1.get_class_dict().keys()]
        [p1.get_class_dict()[class_name].get_function_in_class() for class_name in p1.get_class_dict()]

        [self.assertListEqual(list(class_object.get_methode_dict().keys()), methods_class)
         for class_object in p1.get_class_dict().values()]

    def test_get_function_content_from_class_content(self):
        p1 = PythonFiles('tests/Initial_project_example/SeveralClassFileExample.py')
        p1.get_class_in_file()

        [p1.get_class_content(class_name) for class_name in p1.get_class_dict().keys()]
        [p1.get_class_dict()[class_name].get_function_in_class() for class_name in p1.get_class_dict()]

        for class_object in p1.get_class_dict().values():
            for method in class_object.get_methode_dict().values():
                class_object.get_function_content_from_class_content(method.get_function_name())

        init_content = []
        with open('tests/object_contents/class2_init.py', 'r') as file:
            init_content = file.readlines()

        method2_content = []
        with open('tests/object_contents/class2_method2.py', 'r') as file:
            method2_content = file.readlines()

        self.assertListEqual(p1.get_class_dict()['Class2'].get_methode_dict()['__init__'].content, init_content)
        self.assertListEqual(p1.get_class_dict()['Class2'].get_methode_dict()['method2'].content, method2_content)

    def test_get_param_list_from_class_content(self):
        p1 = PythonFiles('tests/Initial_project_example/SeveralClassFileExample.py')
        p1.get_class_in_file()

        [p1.get_class_content(class_name) for class_name in p1.get_class_dict().keys()]
        [p1.get_class_dict()[class_name].get_function_in_class() for class_name in p1.get_class_dict()]

        for class_object in p1.get_class_dict().values():
            for method in class_object.get_methode_dict().values():
                class_object.get_function_content_from_class_content(method.get_function_name())
                method.get_param_list_from_content()

        self.assertListEqual(p1.get_class_dict()['Class2'].get_param_list_from_class_content(), ['self', 'attr1'])
        self.assertListEqual(p1.get_class_dict()['Class3'].get_param_list_from_class_content(),
                             ['self', 'attr1', 'attr2'])

    def test_write_complete_docstring(self):
        if isdir('tests/modified_project_example'):
            rmtree('tests/modified_project_example')
        copytree('tests/Initial_project_example', 'tests/modified_project_example')

        p1 = PythonFiles('tests/modified_project_example/SeveralClassFileExample.py')

        p1.get_function_in_file()
        p1.get_class_in_file()

        p1.write_first_level_function_docstring()
        p1.write_class_docstring()

        p2 = PythonFiles('tests/modified_project_example/OneClassFileExample.py')

        p2.get_function_in_file()
        p2.get_class_in_file()

        p2.write_first_level_function_docstring()
        p2.write_class_docstring()

        p3 = PythonFiles('tests/modified_project_example/OnlyAClassFileExample.py')

        p3.get_function_in_file()
        p3.get_class_in_file()

        p3.write_first_level_function_docstring()
        p3.write_class_docstring()

        one_class_file_example_documented = []
        with open('tests/documented_project/OneClassFileExample.py', 'r') as file:
            one_class_file_example_documented = file.readlines()

        only_a_class_file_example = []
        with open('tests/documented_project/OnlyAClassFileExample.py', 'r') as file:
            only_a_class_file_example = file.readlines()

        several_class_file_example = []
        with open('tests/documented_project/SeveralClassFileExample.py', 'r') as file:
            several_class_file_example = file.readlines()

        self.assertListEqual(one_class_file_example_documented, p2.get_python_file_content())

        self.assertListEqual(only_a_class_file_example, p3.get_python_file_content())

        self.assertListEqual(several_class_file_example, p1.get_python_file_content())

        rmtree('tests/modified_project_example')


if __name__ == '__main__':
    unittest.main()
