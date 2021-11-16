import Class1


class Class2:

    def __init__(self, attr1):
        self.param1 = attr1

    def method1(self):
        pass

    def method2(self, param1):
        obj1 = Class1()
        obj1.method1()
        pass

    def method3(self, param2, param3='foo'):
        return param2, param3


def other_function(param1, param2='foo'):
    """
    <TO BE COMPLETED>

    Parameters
    __________
    param1 : <TO BE COMPLETED>

    param2='foo' : <TO BE COMPLETED>

    Returns
    _______
    param1 : <TO BE COMPLETED>

    param2 : <TO BE COMPLETED>

    """
    print('toto')
    return(param1, param2)


class Class3:

    def __init__(self, attr1):
        self.param1 = attr1

    def method1(self):
        pass

    def method2(self, param1):
        pass

    def method3(self, param2, param3='foo'):
        return param2, param3


def output_function(file_path):
    """
    <TO BE COMPLETED>

    Parameters
    __________
    file_path : <TO BE COMPLETED>

    Returns
    _______
    file_path : <TO BE COMPLETED>

    Raises
    ______
    FileNotFoundError : <TO BE COMPLETED>

    """
    try:
        with open(file_path, 'r') as cur_file:
            cur_file.readline()
    except FileNotFoundError:
        raise
    return file_path


def output_function2(file_path):
    """
    <TO BE COMPLETED>

    Parameters
    __________
    file_path : <TO BE COMPLETED>

    Returns
    _______
    file_path : <TO BE COMPLETED>

    Raises
    ______
    FileNotFoundError : <TO BE COMPLETED>

    """
    try:
        with open(file_path, 'r') as cur_file:
            cur_file.readline()
    except FileNotFoundError as e:
        raise
    return(file_path)


def output_function3(file_path):
    """
    <TO BE COMPLETED>

    Parameters
    __________
    file_path : <TO BE COMPLETED>

    Returns
    _______
    file_path : <TO BE COMPLETED>

    """
    try:
        with open(file_path, 'r') as cur_file:
            cur_file.readline()
    except:
        raise
    return file_path


def output_function4(file_path):
    """
    <TO BE COMPLETED>

    Parameters
    __________
    file_path : <TO BE COMPLETED>

    Returns
    _______
    file_path : <TO BE COMPLETED>

    Raises
    ______
    FileNotFoundError : <TO BE COMPLETED>

    FileExistsError : <TO BE COMPLETED>

    IndexError : <TO BE COMPLETED>

    """
    try:
        with open(file_path, 'r') as cur_file:
            cur_file.readline()
    except(FileNotFoundError, FileExistsError):
        raise
    try:
        toto = [1, 2, 3]
    except IndexError:
        raise
    return file_path


def another_one():
    """
    <TO BE COMPLETED>

    """
    return


def new_test_function(param1, param2):
    """
    <TO BE COMPLETED>

    Parameters
    __________
    param1 : <TO BE COMPLETED>

    param2 : <TO BE COMPLETED>

    Returns
    _______
    param1 : <TO BE COMPLETED>

    param2 : <TO BE COMPLETED>

    """
    return param1, param2


def empty_function(param):
    """
    <TO BE COMPLETED>

    Parameters
    __________
    param : <TO BE COMPLETED>

    """
    pass


print('hello')
