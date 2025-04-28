#Gavin Pierce password generator
import random
import string
import re

# Function to get a valid password length
def get_valid_password_length():
    while True:
        try:
            length = int(input("Enter the desired length for your password: "))
            if length < 1:
                print("Password length must be at least 1. Please try again.")
            else:
                return length
        except ValueError:
            print("Please enter a valid integer for password length.")

# Function to get user preferences for password criteria
def get_user_preferences():
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'

    return include_uppercase, include_lowercase, include_numbers, include_special

# Function to get the pool of characters based on user preferences
def get_character_pool(include_uppercase, include_lowercase, include_numbers, include_special):
    char_pool = ""
    if include_uppercase:
        char_pool += string.ascii_uppercase
    if include_lowercase:
        char_pool += string.ascii_lowercase
    if include_numbers:
        char_pool += string.digits
    if include_special:
        char_pool += "@#$%^&*()-_=+[{]}|;:'\",<.>/?"

    if not char_pool:
        print("You must select at least one character type (uppercase, lowercase, numbers, special characters).")
        return None

    return char_pool

# Function to assemble a password
def assemble_password(password_length, char_pool):
    return ''.join(random.choice(char_pool) for _ in range(password_length))

# Function to generate multiple passwords
def generate_multiple_passwords(password_length, char_pool, num_passwords=4):
    passwords = []
    for _ in range(num_passwords):
        password = assemble_password(password_length, char_pool)
        passwords.append(password)
    return passwords

# Function to test password strength
def test_password_strength_criteria(password):
    score = 0

    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1

    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    if score == 6:
        return "Very Strong"
    elif score == 5:
        return "Strong"
    elif score == 4:
        return "Moderate"
    elif score == 3:
        return "Weak"
    else:
        return "Very Weak"

# Function to get a valid password choice from the user
def get_password_choice(generated_passwords):
    print("\nChoose a password to test:")
    for idx, password in enumerate(generated_passwords, 1):
        print(f"{idx}. {password}")
    
    try:
        password_choice = int(input(f"Enter the number (1-{len(generated_passwords)}) of the password to test: "))
        if 1 <= password_choice <= len(generated_passwords):
            return generated_passwords[password_choice - 1]
        else:
            print("Invalid choice. Please select a valid password number.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

# Main menu function
def password_main():
    generated_passwords = []  # To store generated passwords
    while True:
        print("\nWelcome to the Password Generator! Please choose an option:")
        print("1. Generate Passwords")
        print("2. Test a Password's Strength")
        print("3. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            password_length = get_valid_password_length()  # Get password length
            include_uppercase, include_lowercase, include_numbers, include_special = get_user_preferences()  # Get character preferences

            char_pool = get_character_pool(include_uppercase, include_lowercase, include_numbers, include_special)
            if char_pool is None:
                continue

            generated_passwords = generate_multiple_passwords(password_length, char_pool)  # Generate passwords
            print("\nHere are the generated passwords:")
            for idx, password in enumerate(generated_passwords, 1):
                print(f"{idx}. {password}")

        elif choice == "2":
            if not generated_passwords:
                print("\nNo passwords have been generated yet. Please generate some first.")
                continue

            password_to_test = get_password_choice(generated_passwords)
            if password_to_test:
                strength = test_password_strength_criteria(password_to_test)
                print(f"\nThe strength of the selected password '{password_to_test}' is: {strength}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select again.")

# Run the main function
if __name__ == "main":
    password_main()
