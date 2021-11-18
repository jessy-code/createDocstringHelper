class Class1:
    """
    <TO BE COMPLETED>

    Parameters
    __________
    self : <TO BE COMPLETED>

    attr1 : <TO BE COMPLETED>

    Methods
    _______
    __init__ : <TO BE COMPLETED>

    method1 : <TO BE COMPLETED>

    method2 : <TO BE COMPLETED>

    method3 : <TO BE COMPLETED>

    open_file : <TO BE COMPLETED>
    """
    def __init__(self, attr1):
        """
        <TO BE COMPLETED>

        Parameters
        __________
        self : <TO BE COMPLETED>

        attr1 : <TO BE COMPLETED>

        """
        self.param1 = attr1

    def method1(self):
        """
        <TO BE COMPLETED>

        Parameters
        __________
        self : <TO BE COMPLETED>

        """
        pass

    def method2(self, param1):
        """
        <TO BE COMPLETED>

        Parameters
        __________
        self : <TO BE COMPLETED>

        param1 : <TO BE COMPLETED>

        """
        pass

    def method3(self, param2, param3='foo'):
        """
        <TO BE COMPLETED>

        Parameters
        __________
        self : <TO BE COMPLETED>

        param2 : <TO BE COMPLETED>

        param3='foo' : <TO BE COMPLETED>

        Returns
        _______
        param2 : <TO BE COMPLETED>

        param3 : <TO BE COMPLETED>

        """
        return param2, param3

    def open_file(self, file_path):
        """
        <TO BE COMPLETED>

        Parameters
        __________
        self : <TO BE COMPLETED>

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

print('hello')