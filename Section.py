class Section:

    def __init__(self, section_title, object_list=[]):
        self.__section_title = section_title
        self.__object_list = object_list
        self.__writable_section = ''

        self.__call__(section_title, object_list)

    def __call__(self, section_title, object_list):
        self.__section_title = '\n' + section_title + '\n' + ''.join(['_' for car in section_title])
        self.__writable_section += self.__section_title
        if len(object_list) > 0:
            self.__writable_section += ''.join(['\n' + cur_object + ' : <TO BE COMPLETED>\n'
                                               for cur_object in object_list])

    def get_section_title(self):
        return self.__section_title

    def get_writable_section(self):
        return self.__writable_section

    def set_section_title(self, section_title):
        self.__section_title = section_title
