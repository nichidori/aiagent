from functions.get_file_content import get_file_content

def test_get_file_content():
    c1 = get_file_content("calculator", "main.py")
    print(f'Result for "main.py":\n{c1}\n')
    
    c2 = get_file_content("calculator", "pkg/calculator.py")
    print(f'Result for "pkg/calculator.py":\n{c2}\n')

    c3 = get_file_content("calculator", "/bin/cat")
    print(f'Result for "/bin/cat":\n{c3}\n')

    c4 = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f'Result for "pkg/does_not_exist.py":\n{c4}\n')
    
if __name__ == "__main__":
    test_get_file_content()