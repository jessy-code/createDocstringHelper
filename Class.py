class Class:

    def __init__(self, class_name):
        self.__class_name = class_name
        self.__attribute_list = []
        self.__methode_list = []
        self.__parm_list = []

    def __eq__(self, other_class):
        return self.__class_name == other_class.get_class_name()

    def get_class_name(self):
        return self.__class_name

    def append_attribute(self, attribute):
        self.__attribute_list.append(attribute)

    def append_function(self, methode):
        self.__methode_list.append(methode)
