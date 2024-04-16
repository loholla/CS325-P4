import validators
import sys

def test_link_verification():
    with open(sys.argv[1], "r") as file:
        num = 1
        for line in file.readlines():
            line = str(line[:-1])
            validation = validators.url(line)
            if validation:
                print(f"Line {num} is a URL")
            else:
                print(f"Line {num} is not a URL")
            num+=1

if __name__ == "__main__":
    test_link_verification()