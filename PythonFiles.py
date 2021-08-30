import re
from Class import Class
from Function import Function


class PythonFiles:

    def __init__(self, python_file_path):
        self.__python_path = python_file_path
        self.__python_file_content = []
        self.__class_list = []
        self.__function_list = []

        self.__call__()

    def __call__(self):
        try:
            with open(self.__python_path, 'r') as python_file:
                self.__python_file_content = python_file.readlines()

        except FileNotFoundError:
            raise

    def get_python_file_content(self):
        return self.__python_file_content

    def get_class_in_file(self):
        self.__class_list = [Class(class_name) for class_name in get_object_name_by_keyword(self.__python_file_content,
                                                                                            'class')]
        return self.__class_list

    def get_function_in_file(self):
        self.__function_list = [Function(function_name) for function_name in get_object_name_by_keyword(
            self.__python_file_content, 'def')]
        return self.__function_list


def get_object_name_by_keyword(file_content, keyword):
    return [(line.strip().split(' ')[1]).split('(')[0].replace(':', '')
            for line in file_content if re.match('^ *' + keyword + '.*: *$', line)]
