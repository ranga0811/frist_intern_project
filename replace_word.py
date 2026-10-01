# Basic File Handling

try:
    # Read data from the file
    with open("data.txt", "r") as file:
        data = file.read()

    print("Original Data:")
    print(data)

    # Find and replace a word
    old_word = input("Enter the word to find: ")
    new_word = input("Enter the replacement word: ")

    modified_data = data.replace(old_word, new_word)

    # Save modified data back to the file
    with open("data.txt", "w") as file:
        file.write(modified_data)

    print("\nModified Data:")
    print(modified_data)

    print("\nFile updated successfully!")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Error:", e)