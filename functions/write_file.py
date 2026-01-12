import os
from functions.validate_target_dir import validate_target_dir

def write_file(working_directory, file_path, content):
    try:
        target_file, valid_target_dir = validate_target_dir(working_directory, file_path)
        
        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        
        with open(target_file, 'w') as f:
            f.write(content)
            
            return f'Successfullly wrote to "{file_path}" ({len(content)} characters written)'
            
    except Exception as e:
        return f'Error: {e}'