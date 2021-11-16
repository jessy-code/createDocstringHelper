class Class1:

    def __init__(self, attr1):
        self.param1 = attr1

    def method1(self):
        pass

    def method2(self, param1):
        pass

    def method3(self, param2, param3='foo'):
        return param2, param3

    def open_file(self, file_path):
        try:
            with open(file_path, 'r') as cur_file:
                cur_file.readline()
        except FileNotFoundError:
            raise

print('hello')