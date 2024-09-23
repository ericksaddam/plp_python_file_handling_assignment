def create_and_write_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is file handling assignment.\n")
            file.write("The answer is plp.\n")
            file.write("plp Python learning is awesome!\n")
        print("File created and written successfully.")
    except PermissionError:
        print("Error: Permission denied. Unable to create or write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred while creating/writing the file: {e}")

def read_and_display_file():
    try:
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("\nFile contents:")
            print(content)
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("This line was appended later.\n")
            file.write("The current year is 2024.\n")
            file.write("File handling in Python is fun!\n")
        print("Additional content appended successfully.")
    except PermissionError:
        print("Error: Permission denied. Unable to append to the file.")
    except Exception as e:
        print(f"An unexpected error occurred while appending to the file: {e}")

def main():
    create_and_write_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()

if __name__ == "__main__":
    main()