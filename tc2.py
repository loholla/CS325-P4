import sys
import requests

def test_link_usable():
    with open(sys.argv[1], "r") as file:
        num = 1
        for URL in file.readlines():
            URL = str(URL[:-1])
            response = requests.get(URL)
            print(f"Article {num}: {int(response.status_code)}")
            num+=1

if __name__ == "__main__":
    test_link_usable()