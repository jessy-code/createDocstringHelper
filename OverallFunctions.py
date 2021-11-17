from re import match


def test_regex(string, keyword):
    return match('^ *' + keyword + '.*: *$', string)


def extract_name_in_line(line):
    return (line.strip().split(' ')[1]).split('(')[0].replace(':', '')


def get_object_name_by_keyword(file_content, keyword):
    return [(line.strip().split(' ')[1]).split('(')[0].replace(':', '')
            for line in file_content if match('^ *' + keyword + '.*: *$', line)]


def get_object_name_from_regex(list_of_string, regex):
    return [(line.strip().split(' ')[1]).split('(')[0].replace(':', '')
            for line in list_of_string if match(regex, line)]


def add_content_to_string_from_list(list_of_line, content, start_flag, stop_flag):
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
    return string.split('(')[1].split(')')[0]
