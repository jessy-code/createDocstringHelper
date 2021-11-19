import argparse
import sys

from file.PythonFiles import PythonFiles


def get_user_inputs():
    # Input variable definition
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                     description='Script which initiate the docstring documentation in a given python '
                                                 'file if it is not already existing.')
    parser.add_argument('input_file', help='path of the python file', type=str)
    return parser.parse_args()


def main(argv):
    user_inputs = get_user_inputs()
    p1 = PythonFiles(user_inputs.input_file)

    p1.get_first_level_function_in_file()
    p1.get_class_in_file()

    p1.write_first_level_function_docstring()
    p1.write_class_docstring()


if __name__ == "__main__":
    main(sys.argv[1:])
