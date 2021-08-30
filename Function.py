from Section import Section


class Function:

    def __init__(self, function_name):
        self.__function_name = function_name
        self.__param_list = []
        self.__returns = []
        self.__raises = []
        self.__docstring = '"""\n   <TO BE COMPLETED>\n\n\n'

    def set_param_list(self, param_list):
        self.__param_list = param_list

    def get_param_list(self):
        return self.__param_list

    def set_returns(self, returns):
        self.__returns = returns

    def set_raises(self, raises):
        self.__raises = raises

    def get_raises(self):
        return self.__raises

    def get_docstring(self):
        return self.__docstring

    def write_docstring(self):
        self.__docstring += Section('Parameters', self.__param_list).get_writable_section() + \
                            Section('Returns', self.__returns).get_writable_section() + \
                            Section('Raises', self.__raises).get_writable_section() + '"""'
