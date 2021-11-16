from re import match
from Class import Class
from Function import Function
from shutil import move


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

    def get_class_content_in_file(self):
        self.__class_dict = {extract_name_in_line(line): Class(extract_name_in_line(line)) for line in
                             self.__python_file_content if test_regex(line, 'class')}
        return self.__class_dict

    def get_function_in_file(self):
        self.__function_dict = {function_name: Function(function_name) for function_name in
                                get_first_level_object_name_by_keyword(self.__python_file_content, 'def')}
        return self.__function_dict

    def get_first_level_function_content(self, function_name):
        self.__function_dict[function_name].content = []
        flag = False

        for line in self.__python_file_content:
            if match('^[a-zA-Z0-9]' + '.*$', line):
                flag = False
            if match('^' + 'def ' + function_name + '\(.*: *$', line):
                flag = True
            if flag:
                self.__function_dict[function_name].content.append(line)

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


        except(FileNotFoundError, FileExistsError):
            print('Impossible to create file ' + tmp_file)
            raise


def test_regex(string, keyword):
    return match('^ *' + keyword + '.*: *$', string)


def extract_name_in_line(line):
    return (line.strip().split(' ')[1]).split('(')[0].replace(':', '')


def get_object_name_by_keyword(file_content, keyword):
    return [(line.strip().split(' ')[1]).split('(')[0].replace(':', '')
            for line in file_content if match('^ *' + keyword + '.*: *$', line)]


def get_first_level_object_name_by_keyword(file_content, keyword):
    return [(line.strip().split(' ')[1]).split('(')[0].replace(':', '')
            for line in file_content if match('^' + keyword + '.*: *$', line)]
