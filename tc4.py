import os

def test_file_exists():
    # Path to the file you want to check
    file_path = 'module_2/processor.py'

    # Check if the file exists
    assert os.path.exists(file_path), f"File '{file_path}' does not exist"
