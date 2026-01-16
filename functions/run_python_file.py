import os
import subprocess
from functions.validate_target_dir import validate_target_dir
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        target_file, valid_target_dir = validate_target_dir(working_directory, file_path)
        
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not target_file.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        
        if args:
            command.extend(args)
            
        completed_process = subprocess.run(command, cwd=working_directory, capture_output=True, text=True, timeout=30)
        output = ""
        
        if completed_process.returncode != 0:
            output += f'Process exited with code {completed_process.returncode}\n'
        
        if not completed_process.stdout or not completed_process.stderr:
            output += 'No output produced.\n'
            
        output += f'STDOUT: {completed_process.stdout}\n'
        output += f'STDERR: {completed_process.stderr}\n'

        return output
        
    except Exception as e:
        return f'Error: execution Python file: {e}'

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file in the working directory and returns its output.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional list of arguments to pass to the Python file.",
                items=types.Schema(
                    type=types.Type.STRING,
                ),
            ),
        },
        required=["file_path"],
    ),
)