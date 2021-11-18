import os


class Project:

    def __init__(self, root_path):
        self.__root_path = root_path
        self.__py_file_list = []

        self.__call__(root_path)

    def __call__(self, root_path):
        self.__root_path = root_path
        try:
            self.__py_file_list = [root_path + '/' + cur_file for cur_file in os.listdir(root_path)
                                   if cur_file.endswith('.py') and os.path.isfile(root_path + '/' + cur_file)]

        except FileNotFoundError:
            raise

    def set_root_path(self, root_path):
        self.__root_path = root_path

    def get_root_path(self):
        return self.__root_path

    def set_py_file_list(self, py_file_list):
        self.__py_file_list = py_file_list

    def get_py_file_list(self):
        return self.__py_file_list
