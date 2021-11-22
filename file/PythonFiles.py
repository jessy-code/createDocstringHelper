from re import match, compile
from python_objects.Class import Class
from python_objects.Function import Function
from shutil import move
from common.OverallFunctions import extract_name_in_line, test_regex, add_content_to_string_from_list, \
    get_object_name_from_regex, check_if_python_class_contains_docstring


class PythonFiles:
    """
    Use to modelling a python file object

    Parameters
    __________
    python_file_path : the python file path

    Methods
    _______
    __call__ : extract the python file content

    get_python_file_content : return the content saved in the current object

    get_function_dict : return the dictionary of first level function founded in the python file

    get_class_dict : return the dictionary of classes founded in the python file

    get_class_in_file : initialize the class dictionary by python file parsing

    get_class_content : extract the class content

    get_function_in_file : initialize the first level function dictionary

    get_first_level_function_content : get the content of first level functions

    init_first_level_function_docstring : build the documentation for a given first level function

    build_string_function_with_docstring : build the string content which will be added to the python file

    write_first_level_function_docstring : write the new built documentation in the python file

    build_string_method_with_docstring : build the documentation object of a given method

    write_method_docstring : write the documentation content in the python file

    init_class_docstring : build the documentation for a given class

    build_string_class_with_docstring : build the string which will be added to the python file

    write_class_docstring : write the class's documentation in the python file
    """

    def __init__(self, python_file_path):
        self.__python_path = python_file_path
        self.__python_file_content = []
        self.__class_dict = {}
        self.__function_dict = {}

        self.__call__()

    def __call__(self):
        """
        Get the python file content

        Raises
        ______
        FileNotFoundError : if the python file is not found

        """
        try:
            with open(self.__python_path, 'r') as python_file:
                self.__python_file_content = python_file.readlines()

        except (FileNotFoundError):
            raise

    def get_python_file_content(self):
        """
        Return the python file content stored in the PythonFile object
        """
        return self.__python_file_content

    def get_function_dict(self):
        """
        Return the function dictionary stored in the PythonFile object
        """
        return self.__function_dict

    def get_class_dict(self):
        """
        Return the class dictionary stored in the PythonFile object
        """
        return self.__class_dict

    def get_class_in_file(self):
        """
        Parse the python file to list all classes and initiate the Class object in a dictionary
        """
        self.__class_dict = {extract_name_in_line(line): Class(extract_name_in_line(line)) for line in
                             self.__python_file_content if test_regex(line, 'class')}
        return self.__class_dict

    def get_class_content(self, class_name):
        """
        Get the content of a given class if it is in the python file at the first level

        Parameters
        __________
        class_name : the name of the class. This class must be in the dictionary class of the PythonFiles

        """
        self.__class_dict[class_name].content = []
        first_class_line = compile('^class ' + class_name + '.*:$')
        last_class_line = compile('^[a-zA-Z0-9]' + '.*$')

        self.__class_dict[class_name].content = add_content_to_string_from_list(self.__python_file_content,
                                                                                self.__class_dict[class_name].content,
                                                                                first_class_line,
                                                                                last_class_line)

        return self.__class_dict[class_name]

    def get_first_level_function_in_file(self):
        """
        Parse the python file to list all first level function and initiate the function object in a dictionary
        """
        self.__function_dict = {function_name: Function(function_name) for function_name in
                                get_object_name_from_regex(self.__python_file_content, compile('^def.*: *$'))}
        return self.__function_dict

    def get_first_level_function_content(self, function_name):
        """
        Get the content of a given function from the python file content

        Parameters
        __________
        function_name : the name of the function which will be extract

        """
        self.__function_dict[function_name].content = []
        start_flag = compile('^def ' + function_name + '\(.*: *$')
        stop_flag = compile('^[a-zA-Z0-9].*$')

        self.__function_dict[function_name].content = add_content_to_string_from_list(self.__python_file_content,
                                                                                      self.__function_dict[
                                                                                          function_name].content,
                                                                                      start_flag,
                                                                                      stop_flag)

        self.__function_dict[function_name].extract_already_docstring_existing()

        return self.__function_dict[function_name]

    def init_first_level_function_docstring(self, function_name):
        """
        Initialize the documentation of a given function from the python file content

        Parameters
        __________
        function_name : the function we want to initiate the documentation. This function must be in the function dictionary
                        of the PythonFiles object

        """
        self.get_first_level_function_content(function_name)
        self.__function_dict[function_name].get_param_list_from_content()
        self.__function_dict[function_name].get_return_list_from_content()
        self.__function_dict[function_name].get_raises_from_content()
        self.__function_dict[function_name].write_docstring()

    def build_string_function_with_docstring(self, function_name):
        """
        Build a string writable in a python file which contains the documentation information of the given function

        Parameters
        __________
        function_name : function which will be parse to build the string

        """
        return self.__function_dict[function_name].content[0] + \
               ''.join(self.__function_dict[function_name].get_docstring()) + \
               ''.join((self.__function_dict[function_name].content[1:]))

    def write_first_level_function_docstring(self):
        """
        Write the documentation in the python file for all first level functions

        Raises
        ______
        FileNotFoundError : if the temporary python file is impossible to write

        FileExistsError : if the temporary python file is impossible to write

        """
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
                        if not self.__function_dict[function_name].docstring_already_exists:
                            file.write(self.build_string_function_with_docstring(function_name))
                        else:
                            flag = False

                    if not flag:
                        file.write(line)

            move(tmp_file, self.__python_path)
            self.__call__()

        except(FileNotFoundError, FileExistsError):
            print('Impossible to create file ' + tmp_file)
            raise

    def build_string_method_with_docstring(self, class_name, function_name):
        """
        Build a string writable in a python file which contains the documentation information of the given method of a
        given class

        Parameters
        __________
        class_name : the class which contains the target method

        function_name : the method name

        """
        return ''.join(self.__class_dict[class_name].get_methode_dict()[function_name].get_docstring())

    def write_method_docstring(self, class_name, method_name, file):
        """
        Write the documentation of a method of a given class in a given file

        Parameters
        __________
        class_name : class which contains the method

        method_name : method which will be documented

        file : File object in which the documentation will be written

        """
        self.__class_dict[class_name].prepare_docstring_to_all_methods()
        [file.write(self.build_string_method_with_docstring(class_name, method_name))
         for line in self.__class_dict[class_name].content
         if match(' .*def ' + method_name + '\(.*:.*$', line)]

    def init_class_docstring(self, class_name):
        """
        Initialize the documentation of a class

        Parameters
        __________
        class_name : the class we want to document

        """
        self.get_class_content(class_name)
        self.__class_dict[class_name].get_function_in_class()
        self.__class_dict[class_name].prepare_docstring_to_all_methods()
        self.__class_dict[class_name].get_param_list_from_class_content()
        self.__class_dict[class_name].write_docstring()

    def build_string_class_with_docstring(self, class_name):
        """
        Build a python writable string which contains the documentation

        Parameters
        __________
        class_name : the class we want to document

        """
        return ''.join(self.__class_dict[class_name].get_docstring()) + '\n'

    def write_class_docstring(self):
        """
        Write the class documentation in the python file

        Raises
        ______
        FileNotFoundError : if the temporary file cannot be created

        FileExistsError : if the temporary file cannot be created

        """
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
                        if not check_if_python_class_contains_docstring(self.__class_dict[class_name].content):
                            file.write(self.build_string_class_with_docstring(class_name))

                    if flag and match('^ .*def .*$', line):
                        method_name = line.split('def ')[1].split('(')[0]
                        if not self.__class_dict[class_name].get_methode_dict()[method_name].docstring_already_exists:
                            self.write_method_docstring(class_name, method_name, file)

            move(tmp_file, self.__python_path)
            self.__call__()

        except(FileNotFoundError, FileExistsError):
            print('Impossible to create file ' + tmp_file)
            raise
