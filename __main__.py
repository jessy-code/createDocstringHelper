import argparse
import sys
from os.path import isdir, isfile

from file.PythonFiles import PythonFiles
from project.Project import Project


def get_user_inputs():
    """
    Function to get user inputs
    """
    # Input variable definition
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                     description='Script which initiate the docstring documentation in a given python '
                                                 'file if it is not already existing.')
    parser.add_argument('input_file', help='path of the python file', type=str)
    return parser.parse_args()


def main(argv):
    user_inputs = get_user_inputs()
    if isfile(user_inputs.input_file):
        p1 = PythonFiles(user_inputs.input_file)

        first_level_function = p1.get_first_level_function_in_file()
        class_dict = p1.get_class_in_file()

        try:
            p1.write_first_level_function_docstring()
        except KeyError:
            print('No first level function')
            pass

        try:
            p1.write_class_docstring()
        except KeyError:
            print('No class')
            pass

    elif isdir(user_inputs.input_file):
        p1 = Project(user_inputs.input_file)
        p1.document_project()


if __name__ == "__main__":
    main(sys.argv[1:])
