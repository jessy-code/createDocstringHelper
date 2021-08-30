from Section import Section


class Class:

    def __init__(self, class_name):
        self.__class_name = class_name
        self.__attribute_list = []
        self.__methode_list = []
        self.__parm_list = []
        self.__docstring = '"""\n   <TO BE COMPLETED>\n\n\n'

    def __eq__(self, other_class):
        return self.__class_name == other_class.get_class_name()

    def get_class_name(self):
        return self.__class_name

    def append_attribute(self, attribute):
        self.__attribute_list.append(attribute)

    def append_function(self, methode):
        self.__methode_list.append(methode)

    def set_param_list(self, param_list):
        self.__parm_list = param_list

    def set_attribute_list(self, attribute_list):
        self.__attribute_list = attribute_list

    def set_methode_list(self, methode):
        self.__methode_list = methode

    def get_param_list(self):
        return self.__parm_list

    def get_attribute_list(self):
        return self.__attribute_list

    def get_methode_list(self):
        return self.__methode_list

    def get_docstring(self):
        return self.__docstring

    def write_docstring(self):
        self.__docstring += Section('Attributes', self.__attribute_list).get_writable_section() + \
                            Section('Parameters', self.__parm_list).get_writable_section() + \
                            Section('Methods', self.__methode_list).get_writable_section() + '"""'
