from re import match, compile
from Class import Class
from Function import Function
from shutil import move
from OverallFunctions import extract_name_in_line, test_regex, add_content_to_string_from_list, \
    get_object_name_from_regex


class PythonFiles:

    def __init__(self, python_file_path):
        self.__python_path = python_file_path
        self.__python_file_content = []
        self.__class_dict = {}
        self.__function_dict = {}

        self.__call__()

    def __call__(self):
        try:
            with open(self.__python_path, 'r') as python_file:
                self.__python_file_content = python_file.readlines()

        except FileNotFoundError:
            raise

    def get_python_file_content(self):
        return self.__python_file_content

    def get_function_dict(self):
        return self.__function_dict

    def get_class_dict(self):
        return self.__class_dict

    def get_class_in_file(self):
        self.__class_dict = {extract_name_in_line(line): Class(extract_name_in_line(line)) for line in
                             self.__python_file_content if test_regex(line, 'class')}
        return self.__class_dict

    def get_class_content(self, class_name):
        self.__class_dict[class_name].content = []
        first_class_line = compile('^class ' + class_name + '.*:$')
        last_class_line = compile('^[a-zA-Z0-9]' + '.*$')

        self.__class_dict[class_name].content = add_content_to_string_from_list(self.__python_file_content,
                                                                                self.__class_dict[class_name].content,
                                                                                first_class_line,
                                                                                last_class_line)

        return self.__class_dict[class_name]

    def get_function_in_file(self):
        self.__function_dict = {function_name: Function(function_name) for function_name in
                                get_object_name_from_regex(self.__python_file_content, compile('^def.*: *$'))}
        return self.__function_dict

    def get_first_level_function_content(self, function_name):
        self.__function_dict[function_name].content = []
        start_flag = compile('^' + 'def ' + function_name + '\(.*: *$')
        stop_flag = compile('^[a-zA-Z0-9]' + '.*$')

        self.__function_dict[function_name].content = add_content_to_string_from_list(self.__python_file_content,
                                                                                      self.__function_dict[
                                                                                          function_name].content,
                                                                                      start_flag,
                                                                                      stop_flag)

        self.__function_dict[function_name].extract_already_docstring_existing()

        return self.__function_dict[function_name]

    def init_first_level_function_docstring(self, function_name):
        self.get_first_level_function_content(function_name)
        self.__function_dict[function_name].get_param_list_from_content()
        self.__function_dict[function_name].get_return_list_from_content()
        self.__function_dict[function_name].get_raises_from_content()
        self.__function_dict[function_name].write_docstring()

    def build_string_function_with_docstring(self, function_name):
        return self.__function_dict[function_name].content[0] + \
               ''.join(self.__function_dict[function_name].get_docstring()) + \
               ''.join((self.__function_dict[function_name].content[1:]))

    def write_first_level_function_docstring(self):
        self.__call__()
        try:
            tmp_file = self.__python_path.split('.py')[0] + '_tmp' + '.py'
            with open(tmp_file, 'w') as file:

                flag = False
                for line in self.__python_file_content:
                    if match('^[a-zA-Z0-9].*$', line):
                        flag = False

                    if match('^def .*\(.*:.*$', line):
                        flag = True
                        function_name = line.split('def ')[1].split('(')[0]
                        self.init_first_level_function_docstring(function_name)
                        file.write(self.build_string_function_with_docstring(function_name))

                    if not flag:
                        file.write(line)

            move(tmp_file, self.__python_path)
            self.__call__()

        except(FileNotFoundError, FileExistsError):
            print('Impossible to create file ' + tmp_file)
            raise

    def build_string_method_with_docstring(self, class_name, function_name):
        return ''.join(self.__class_dict[class_name].get_methode_dict()[function_name].get_docstring())

    def write_method_docstring(self, class_name, method_name, file):
        self.__class_dict[class_name].prepare_docstring_to_all_methods()
        for line in self.__class_dict[class_name].content:
            if match(' .*def ' + method_name + '\(.*:.*$', line):
                file.write(self.build_string_method_with_docstring(class_name, method_name))

    def init_class_docstring(self, class_name):
        self.get_class_content(class_name)
        self.__class_dict[class_name].get_function_in_class()
        self.__class_dict[class_name].prepare_docstring_to_all_methods()
        self.__class_dict[class_name].get_param_list_from_class_content()
        self.__class_dict[class_name].write_docstring()

    def build_string_class_with_docstring(self, class_name):
        return ''.join(self.__class_dict[class_name].get_docstring()) \


    def write_class_docstring(self):
        self.__call__()
        try:
            tmp_file = self.__python_path.split('.py')[0] + '_tmp' + '.py'
            with open(tmp_file, 'w') as file:
                flag = False

                for line in self.__python_file_content:
                    file.write(line)
                    if match('^[a-zA-Z0-9].*$', line):
                        flag = False

                    if match('^class .*:.*$', line):
                        flag = True

                        try:
                            class_name = line.split('class ')[1].split(':')[0]
                        except:
                            class_name = line.split('class ')[1].split('(')[0]
                        self.init_class_docstring(class_name)

                        file.write(self.build_string_class_with_docstring(class_name))

                    if flag and match('^ .*def .*$', line):
                        method_name = line.split('def ')[1].split('(')[0]
                        self.write_method_docstring(class_name, method_name, file)

            move(tmp_file, self.__python_path)
            self.__call__()

        except(FileNotFoundError, FileExistsError):
            print('Impossible to create file ' + tmp_file)
            raise
