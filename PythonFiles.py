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
