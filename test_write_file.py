from functions.write_file import write_file

def test_write_file():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f'Result for writing to "lorem.txt": {result}')
    
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f'Result for writing to "pkg/morelorem.txt": {result}')
    
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f'Result for writing to "/tmp/temp.txt": {result}')
    
if __name__ == "__main__":
    test_write_file()