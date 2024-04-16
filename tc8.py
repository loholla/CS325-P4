import sys
from module_1 import raw_data_collector

def test_articles_processed():
    with open(sys.argv[1], "r") as file:
        li = file.readlines()
    total_line = len(li)
    print(f"Total Articles: {total_line}")

    num = raw_data_collector.rdc(sys.argv)
    print(f"Number of articles processed: {num - 1}")

    if total_line == num-1:
        print("Accurate number of articles processed")

if __name__ == "__main__":
    test_articles_processed()