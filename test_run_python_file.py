from functions.run_python_file import run_python_file

def test_run_python_file():
    result = run_python_file("calculator", "main.py")
    print(f'Result of running main.py: {result}')

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(f'Result of running main.py with args: {result}')

    result = run_python_file("calculator", "tests.py")
    print(f'Result of running tests.py: {result}')

    result = run_python_file("calculator", "../main.py")
    print(f'Result of running ../main.py: {result}')

    result = run_python_file("calculator", "nonexistent.py")
    print(f'Result of running nonexistent.py: {result}')

    result = run_python_file("calculator", "lorem.txt")
    print(f'Result of running lorem.txt: {result}')
    
if __name__ == "__main__":
    test_run_python_file()