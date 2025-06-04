import random
import string

def generate_password(length):
    if length < 4:
        return "Password length must be at least 4 for complexity."


    all_chars = string.ascii_letters + string.digits + string.punctuation


    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]


    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

def main():
    print("🔐 Password Generator")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print("\nYour generated password is:\n" + password)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()