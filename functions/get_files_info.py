import os
from functions.validate_target_dir import validate_target_dir
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:            
        target_dir, valid_target_dir = validate_target_dir(working_directory, directory)

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        contents = os.listdir(target_dir)
        files_info = []
        
        for content in contents:
            content_path = os.path.join(target_dir, content)
            file_size = os.path.getsize(content_path)
            is_dir = os.path.isdir(content_path)
            files_info.append(f"- {content}: file_size={file_size}, is_dir={is_dir}")
        
        return "\n".join(files_info)
            
    except Exception as e:
        return f'Error: {e}'
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)