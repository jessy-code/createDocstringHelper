class Section:

    def __init__(self, section_title):
        self.__section_title = section_title

        self.__call__(section_title)

    def __call__(self, section_title):
        self.__section_title = section_title + '\n' + ''.join(['_' for car in section_title])

    def get_section_title(self):
        return self.__section_title

    def set_section_title(self, section_title):
        self.__section_title = section_title
