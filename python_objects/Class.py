from python_objects.Function import Function
from common.OverallFunctions import get_object_name_from_regex, add_content_to_string_from_list, get_indentation
from common.Section import Section
from re import compile


class Class:

    def __init__(self, class_name):
        self.__class_name = class_name
        self.__methode_dict = {}
        self.__parm_list = []
        self.__docstring = ''
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

    def get_function_content_from_class_content(self, function_name):
        self.__methode_dict[function_name].content = []
        start_flag = compile('^ *' + 'def ' + function_name + '\(.*: *$')
        stop_flag = compile('^' + get_indentation(self.content) + '[a-zA-Z0-9]' + '.*$')

        self.__methode_dict[function_name].content = add_content_to_string_from_list(self.content,
                                                                                     self.__methode_dict[
                                                                                         function_name].content,
                                                                                     start_flag,
                                                                                     stop_flag)

        self.__methode_dict[function_name].extract_already_docstring_existing()

        return self.__methode_dict[function_name]

    def get_param_list_from_class_content(self):
        self.__parm_list = self.__methode_dict['__init__'].get_param_list()
        return self.__parm_list

    def prepare_docstring_to_all_methods(self):
        self.get_function_in_class()
        [self.get_function_content_from_class_content(function_name) for function_name in
         list(self.__methode_dict.keys())]

        [method.get_param_list_from_content() for method in self.__methode_dict.values()]
        [method.get_return_list_from_content() for method in self.__methode_dict.values()]
        [method.get_raises_from_content() for method in self.__methode_dict.values()]
        [method.write_docstring() for method in self.__methode_dict.values()]

    def write_docstring(self):
        if self.content:
            self.__docstring += get_indentation(self.content) + '"""\n' + get_indentation(self.content) + \
                                '<TO BE COMPLETED>\n'
            self.__docstring += Section('Parameters', self.__parm_list,
                                        offset=get_indentation(self.content)).get_writable_section() + \
                                Section('Methods', self.__methode_dict.keys(),
                                        offset=get_indentation(self.content)).get_writable_section() + \
                                get_indentation(self.content) + '"""'
        else:
            self.__docstring += '"""\n' + '<TO BE COMPLETED>\n'
            self.__docstring += Section('Parameters', self.__parm_list).get_writable_section() + \
                                Section('Methods', self.__methode_dict.keys()).get_writable_section() + \
                                '"""'
