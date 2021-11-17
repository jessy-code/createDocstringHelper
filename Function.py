from re import match, compile

from OverallFunctions import get_indentation
from Section import Section


class Function:

    def __init__(self, function_name):
        self.__function_name = function_name
        self.__param_list = []
        self.__returns = []
        self.__raises = []
        self.__docstring = ''
        self.content = []

    def __eq__(self, other_function):
        return self.__function_name == other_function.get_function_name() and self.content == other_function.content

    def get_function_name(self):
        return self.__function_name

    def set_param_list(self, param_list):
        self.__param_list = param_list

    def get_param_list(self):
        return self.__param_list

    def set_returns(self, returns):
        self.__returns = returns

    def get_returns(self):
        return self.__returns

    def set_raises(self, raises):
        self.__raises = raises

    def get_raises(self):
        return self.__raises

    def get_docstring(self):
        return self.__docstring

    def get_param_list_from_content(self):
        self.__param_list = []
        several_param_format = compile('^.*def .*\(.*,.*$')
        no_param_format = compile('^.*def .*\(\)')

        if match(several_param_format, self.content[0]):
            self.__param_list.extend(self.content[0].split('(')[1].split(')')[0].split(','))
        elif match(no_param_format, self.content[0]):
            self.__param_list = []
        else:
            self.__param_list.append(self.content[0].split('(')[1].split(')')[0])

        self.__param_list = [elt.strip() for elt in self.__param_list]

    def get_return_list_from_content(self):
        self.__returns = []
        return_format = compile('^ *return.*$')
        simple_return = compile('^ *return [a-zA-Z0-9_-]*$')
        bracket_return = compile('^ *return\([a-zA-Z0-9_-]*\).*$')
        several_value_return = compile('^ *return [a-zA-Z0-9_-]*,.*$')
        several_value_with_bracket_return = compile('^ *return\([a-zA-Z0-9_-]*,.*$')
        return_lines = [line.strip() for line in self.content if match(return_format, line)]

        [self.__returns.append(elt.split('(')[1].split(')')[0]) for elt in return_lines if match(bracket_return, elt)]

        [self.__returns.extend(elt.split('return ')[1].split(','))
         for elt in return_lines if match(several_value_return, elt)]

        [self.__returns.extend(elt.split('(')[1].split(')')[0].split(','))
         for elt in return_lines if match(several_value_with_bracket_return, elt)]

        [self.__returns.append(elt.split('return ')[1]) for elt in return_lines if match(simple_return, elt)]

        self.__returns = [elt.strip() for elt in self.__returns]

        return self.__returns

    def get_raises_from_content(self):
        self.__raises = []

        exception_format = compile('^ *except[( ].*$')
        several_exception_format = compile('^ *except[( ].*,.*$')
        except_lines = [line.strip() for line in self.content if match(exception_format, line)]

        [self.__raises.extend(
            elt.split('as')[0].split('except')[1].strip().split(':')[0].split(')')[0].split('(')[1].split(','))
         if match(several_exception_format, elt)
         else self.__raises.append(elt.split('as')[0].split('except')[1].strip().split(':')[0].split(')')[0])
         for elt in except_lines]

        self.__raises = [elt.strip() for elt in self.__raises]
        return self.__raises

    def extract_already_docstring_existing(self):
        content_tmp = []
        self.__docstring = []
        flag = False
        for line in self.content:
            if match('.*""".*$', line):
                flag = not flag
            if flag or match('.*""".*$', line):
                self.__docstring.append(line)
            if not flag and not match('.*""".*$', line):
                content_tmp.append(line)
        self.content = content_tmp

    def write_docstring(self):
        self.__docstring += get_indentation(self.content) + '"""\n' + get_indentation(self.content) + '<TO BE COMPLETED>\n'

        if self.__param_list:
            self.__docstring += Section('Parameters', self.__param_list,
                                        offset=get_indentation(self.content)).get_writable_section()

        if self.__returns:
            self.__docstring += Section('Returns', self.__returns, offset=get_indentation(self.content)).get_writable_section()

        if self.__raises:
            self.__docstring += Section('Raises', self.__raises, offset=get_indentation(self.content)).get_writable_section()

        self.__docstring += '\n' + get_indentation(self.content) + '"""\n'
