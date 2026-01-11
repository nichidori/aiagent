from functions.get_files_info import get_files_info

def test_get_files_info():
    info1 = get_files_info("calculator", ".")
    print(f"Result for current directory:\n{info1}\n")
    
    info2 = get_files_info("calculator", "pkg")
    print(f"Result for 'pkg' directory:\n{info2}\n")
    
    info3 = get_files_info("calculator", "/bin")
    print(f"Result for '/bin' directory:\n{info3}\n")
    
    info4 = get_files_info("calculator", "../")
    print(f"Result for '../' directory:\n{info4}\n")

if __name__ == "__main__":
    test_get_files_info()