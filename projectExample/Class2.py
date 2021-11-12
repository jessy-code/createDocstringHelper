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
        return (param2, param3)


class Class3:

    def __init__(self, attr1):
        self.param1 = attr1

    def method1(self):
        pass

    def method2(self, param1):
        pass

    def method3(self, param2, param3='foo'):
        return param2, param3


def output_function():
    pass


def other_function(param1, param2):
    return param1, param2
