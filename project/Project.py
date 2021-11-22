from os.path import isfile, isdir
from os import listdir
from file.PythonFiles import PythonFiles


class Project:
    """
    <TO BE COMPLETED>

    Parameters
    __________
    self : <TO BE COMPLETED>

    root_path : <TO BE COMPLETED>

    Methods
    _______
    __init__ : <TO BE COMPLETED>

    __call__ : <TO BE COMPLETED>

    set_root_path : <TO BE COMPLETED>

    get_root_path : <TO BE COMPLETED>

    set_py_file_list : <TO BE COMPLETED>

    get_py_file_list : <TO BE COMPLETED>
    """

    def __init__(self, root_path):
        """
        <TO BE COMPLETED>

        Parameters
        __________
        self : <TO BE COMPLETED>

        root_path : <TO BE COMPLETED>

        """
        self.__root_path = root_path
        self.__py_file_list = []
        self.__internal_folders = []

        self.__call__(root_path)

    def __call__(self, root_path):
        """
        <TO BE COMPLETED>

        Parameters
        __________
        self : <TO BE COMPLETED>

        root_path : <TO BE COMPLETED>

        Raises
        ______
        FileNotFoundError : <TO BE COMPLETED>

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
        <TO BE COMPLETED>

        Parameters
        __________
        self : <TO BE COMPLETED>

        root_path : <TO BE COMPLETED>

        """
        self.__root_path = root_path

    def get_root_path(self):
        """
        <TO BE COMPLETED>

        Parameters
        __________
        self : <TO BE COMPLETED>

        """
        return self.__root_path

    def set_py_file_list(self, py_file_list):
        """
        <TO BE COMPLETED>

        Parameters
        __________
        self : <TO BE COMPLETED>

        py_file_list : <TO BE COMPLETED>

        """
        self.__py_file_list = py_file_list

    def get_py_file_list(self):
        """
        <TO BE COMPLETED>

        Parameters
        __________
        self : <TO BE COMPLETED>

        """
        return self.__py_file_list

    def document_project(self):
        for project in self.__internal_folders:
            project.document_project()

        for py_file in self.__py_file_list:
            p1 = PythonFiles(py_file)

            p1.get_first_level_function_in_file()
            p1.get_class_in_file()

            p1.write_first_level_function_docstring()
            p1.write_class_docstring()
