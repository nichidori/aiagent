import os
from config import MAX_CHARS
from functions.validate_target_dir import validate_target_dir
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        target_file, valid_target_dir = validate_target_dir(working_directory, file_path)
        
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        content = None
        with open(target_file) as f:
            content = f.read(MAX_CHARS)
            
            if f.read(1):
                content += f'[...File "{file_path}" truncated to {MAX_CHARS} characters]'
        
        return content
            
    except Exception as e:
        return f'Error: {e}'
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads the content of a specified file relative to the working directory, up to a {MAX_CHARS} maximum character limit",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)