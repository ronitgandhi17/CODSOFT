import string
import secrets

def generate_password(length=12):
    # Define characters to use for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a secure random password
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length < 1:
            print("Password length must be at least 1.")
        else:
            password = generate_password(password_length)
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    main()