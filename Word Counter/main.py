#Gavin Pierce Word Counter

import file_handler
import time_handler
import os

# Function to display the main menu
def show_menu():
    print("\nWelcome to the Word Counter Program!")
    print("1. View the file")
    print("2. Edit the file")
    print("3. Exit")
    
    choice = input("Enter the number of your choice: ")
    return choice

def main():
    # Allow the user to specify the file or use a default
    filename = input("Enter the filename (default: editing_file.txt): ") or "editing_file.txt"
    
    # Check if the file exists, create if not
    if not os.path.exists(filename):
        print(f"The file {filename} does not exist. Creating a new file.")
        with open(filename, 'w') as f:
            f.write("")  # Create an empty file

    while True:
        # Show the menu and get the user's choice
        choice = show_menu()

        if choice == "1":
            # View the file
            try:
                current_content = file_handler.read_file(filename)
                print("\nHere’s the current content of your file:")
                print(current_content)
            except Exception as e:
                print(f"Error reading the file: {e}")

        elif choice == "2":
            # Edit the file
            try:
                current_content = file_handler.read_file(filename)
                print("\nCurrent file content:")
                print(current_content)
                print("\n--- End of Current Content ---\n")

                # Ask the user for new content
                print("Enter new content below (or press Enter to leave the content unchanged):")
                new_content = input()

                if new_content.strip():  # If the user enters new content, update it
                    current_content = new_content

                # Write the new content back to the file
                file_handler.write_file(filename, current_content)

                # Get the word count from the updated file
                word_count = file_handler.get_word_count(filename)

                # Get the current timestamp
                timestamp = time_handler.get_current_timestamp()

                # Update the file with word count and timestamp at the end
                file_handler.update_file(filename, word_count, timestamp)

                # Print confirmation
                print(f"Word count and timestamp have been added to {filename}.")
                print("Here’s the updated file content:")
                print(file_handler.read_file(filename))
            except Exception as e:
                print(f"Error during file editing: {e}")

        elif choice == "3":
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Invalid choice, prompt again
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
