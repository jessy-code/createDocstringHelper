from re import match, IGNORECASE
from re import split as resplit


def test_regex(string, keyword):
    """
    Check if a given string is contained in another one

    Parameters
    __________
    string : string in which you want to check

    keyword : string you want to find

    """
    return match('^ *' + keyword + '.*: *$', string)


def extract_name_in_line(line):
    """
    Get the name of an object in a python line

    Parameters
    __________
    line : the line in which we want to find an object name

    """
    return (line.strip().split(' ')[1]).split('(')[0].replace(':', '')


def get_object_name_by_keyword(file_content, keyword):
    """
    Get the list of name for a specific type of object

    Parameters
    __________
    file_content : a list of string where we search the objects

    keyword : identifier of the objects

    """
    return [(line.strip().split(' ')[1]).split('(')[0].replace(':', '')
            for line in file_content if match('^ *' + keyword + '.*: *$', line)]


def get_object_name_from_regex(list_of_string, regex):
    """
    Get the objects found from a given regular expression

    Parameters
    __________
    list_of_string : list in which we search objects

    regex : regular expression used to find objects

    """
    return [(line.strip().split(' ')[1]).split('(')[0].replace(':', '')
            for line in list_of_string if match(regex, line)]


def add_content_to_string_from_list(list_of_line, content, start_flag, stop_flag):
    """
    Add strings to an already existing string. The added element are found in the list_of_line input. We add all lines
    between the input start_flag and the input stop_flag.

    Parameters
    __________
    list_of_line : a list of string where we want to extract elements between start and stop flags

    content : the string list in which the elements will be added

    start_flag : the flag were the extraction will start on list_of_line input

    stop_flag : the flag were the extraction will stop

    Returns
    _______
    content : the content with the wanted added elements

    """
    flag = False
    for line in list_of_line:
        if match(stop_flag, line):
            flag = False
        if match(start_flag, line):
            flag = True
        if flag:
            content.append(line)
    return content


def remove_brackets_to_string(string):
    """
    Remove brackets to a given string

    Parameters
    __________
    string : the string in which we want to remove brackets

    """
    return string.replace('(', '').replace(')','')


def get_indentation(string_list):
    """
    Get the indentation level of a python object.

    Parameters
    __________
    string_list : the content lines of a python object

    """
    indented_lines = [line for line in string_list if
                      match(r'^ .*[a-zA-Z0-9]*$', line) and string_list.index(line) > 0]
    try:

        return resplit(r'[a-z0-9]', indented_lines[0], flags=IGNORECASE)[0]
    except IndexError:
        raise
