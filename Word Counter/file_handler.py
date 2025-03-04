# file_handler.py

def read_file(filename):
    """Reads the content of the file."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty file.")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

def write_file(filename, content):
    """Writes the new content to the file, overwriting any existing content."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to file: {e}")

def get_word_count(filename):
    """Returns the word count of the file content."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        words = content.split()
        return len(words)
    except FileNotFoundError:
        print(f"File {filename} not found. Word count will be 0.")
        return 0
    except Exception as e:
        print(f"Error calculating word count: {e}")
        return 0

def update_file(filename, word_count, timestamp):
    """Appends the word count and timestamp to the end of the file."""
    try:
        with open(filename, 'a') as file:
            file.write(f"\n\nWord Count: {word_count}\nLast Updated: {timestamp}")
    except Exception as e:
        print(f"Error updating file: {e}")
