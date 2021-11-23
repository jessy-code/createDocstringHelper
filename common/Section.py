class Section:
    """
    Section of a docstring element

    Parameters
    __________
    section_title : the section title

    object_list=[] : the object which will documented in the section

    offset='' : indentation level of the current python object

    Methods
    _______
    __call__ : build the section string

    get_section_title : return the section title

    get_writable_section : return the section string content

    set_section_title : set the section title
    """
    def __init__(self, section_title, object_list=None, offset=''):
        if object_list is None:
            object_list = []
        self.__section_title = section_title
        self.__object_list = object_list
        self.__writable_section = ''
        self.offset = offset

        self.__call__(section_title, object_list)

    def __call__(self, section_title, object_list):
        """
        Build the section string

        Parameters
        __________
        section_title : the section title

        object_list : the object which will be documented in the current section

        """
        self.__section_title = '\n' + self.offset + section_title + '\n' + self.offset + ''.join(['_' for car in section_title])
        self.__writable_section += self.__section_title
        if len(object_list) > 0:
            self.__writable_section += ''.join(['\n' + self.offset + cur_object + ' : <TO BE COMPLETED>\n'
                                               for cur_object in object_list])

    def get_section_title(self):
        """
        Return the section title
        """
        return self.__section_title

    def get_writable_section(self):
        """
        Return the string which is contained in this section
        """
        return self.__writable_section

    def set_section_title(self, section_title):
        """
        Set the __section_title attribute

        Parameters
        __________
        section_title : the title you want to set in the section title

        """
        self.__section_title = section_title
