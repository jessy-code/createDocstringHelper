import os


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
            self.__py_file_list = [root_path + '/' + cur_file for cur_file in os.listdir(root_path)
                                   if cur_file.endswith('.py') and os.path.isfile(root_path + '/' + cur_file)]

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
