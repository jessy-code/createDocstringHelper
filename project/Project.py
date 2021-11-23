from os.path import isfile, isdir
from os import listdir
from file.PythonFiles import PythonFiles


class Project:
    """
    Class design to modelling a complete python project

    Parameters
    __________
    root_path : the root path of the python project

    Methods
    _______
    __call__ : parse python project and initialize needed objects for documentation

    set_root_path : set the project root path

    get_root_path : return the project root path

    set_py_file_list : set the python file list

    get_py_file_list : return the python file list

    document_project : initialize docstring documentation for all project
    """

    def __init__(self, root_path):
        self.__root_path = root_path
        self.__py_file_list = []
        self.__internal_folders = []

        self.__call__(root_path)

    def __call__(self, root_path):
        """
        Parse python project and initialize needed objects for documentation.

        Parameters
        __________
        root_path : the root path of the python project

        Raises
        ______
        FileNotFoundError : raised if the root path cannot be found

        """
        self.__root_path = root_path
        try:
            self.__py_file_list = [root_path + '/' + cur_file for cur_file in listdir(root_path)
                                   if cur_file.endswith('.py') and isfile(root_path + '/' + cur_file)]

            self.__internal_folders = [Project(root_path + '/' + cur_file) for cur_file in listdir(root_path)
                                       if isdir(root_path + '/' + cur_file)]

        except FileNotFoundError:
            raise

    def set_root_path(self, root_path):
        """
        Set the project root path.

        Parameters
        __________
        root_path : the root path of the python project

        """
        self.__root_path = root_path

    def get_root_path(self):
        """
        Return the project root path
        """
        return self.__root_path

    def set_py_file_list(self, py_file_list):
        """
        Set the python file list.

        Parameters
        __________
        py_file_list : the new python file list

        """
        self.__py_file_list = py_file_list

    def get_py_file_list(self):
        """
        Return the python file list.
        """
        return self.__py_file_list

    def document_project(self):
        """
        Initialize docstring documentation for all project.
        """
        for project in self.__internal_folders:
            project.document_project()

        for py_file in self.__py_file_list:
            p1 = PythonFiles(py_file)

            p1.get_first_level_function_in_file()
            p1.get_class_in_file()

            p1.write_first_level_function_docstring()
            p1.write_class_docstring()
