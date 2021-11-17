from Function import Function
from OverallFunctions import get_object_name_from_regex
from Section import Section
from re import compile


class Class:

    def __init__(self, class_name):
        self.__class_name = class_name
        self.__methode_dict = {}
        self.__parm_list = []
        self.__docstring = '"""\n   <TO BE COMPLETED>\n\n\n'
        self.content = []

    def __eq__(self, other_class):
        return self.__class_name == other_class.get_class_name()

    def get_class_name(self):
        return self.__class_name

    def set_param_list(self, param_list):
        self.__parm_list = param_list

    def get_param_list(self):
        return self.__parm_list

    def get_methode_dict(self):
        return self.__methode_dict

    def get_docstring(self):
        return self.__docstring

    def get_function_in_class(self):
        self.__methode_dict = {function_name: Function(function_name) for function_name in
                               get_object_name_from_regex(self.content, compile('^ *def.*: *$'))}
        return self.__methode_dict

    def write_docstring(self):
        self.__docstring += Section('Parameters', self.__parm_list).get_writable_section() + \
                            Section('Methods', self.__methode_dict).get_writable_section() + '"""'
