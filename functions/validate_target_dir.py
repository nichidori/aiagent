import os

def validate_target_dir(working_directory, target_path):
    working_dir_abs = os.path.abspath(working_directory)
    target_path_abs = os.path.normpath(os.path.join(working_dir_abs, target_path))

    valid_target_dir = os.path.commonpath([working_dir_abs, target_path_abs]) == working_dir_abs
    
    return target_path_abs, valid_target_dir