def output_function(file_path):
    try:
        with open(file_path, 'r') as cur_file:
            cur_file.readline()
    except FileNotFoundError:
        raise


