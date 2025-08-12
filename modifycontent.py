def modify_content(content):
    # Example modification: convert all text to uppercase
    return content.upper()

def main():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: The file does not exist.")
        return
    except IOError:
        print("Error: The file cannot be read.")
        return

    modified_content = modify_content(content)

    new_filename = "modified_" + filename
    try:
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"Modified content written to {new_filename}")
    except IOError:
        print("Error: Could not write to the new file.")

if __name__ == "__main__":
    main()
