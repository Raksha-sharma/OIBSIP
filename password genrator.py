import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def main():
    print("Password Generator")
    print("-----------------")
    length = int(input("Enter the password length (at least 8 characters): "))
    password = generate_password(length)
    if password:
        print("Generated Password : ", password)

if __name__ == "__main__":
    main()