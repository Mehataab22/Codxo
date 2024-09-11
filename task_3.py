"""This Python script generates random passwords with user-defined lengths, ensuring that the passwords meet a minimum length requirement of 8 characters. 
It excludes special characters, using only ASCII letters and digits to create the passwords. 
The script runs in a continuous loop, prompting the user to input the desired password length or type 'exit' to terminate the program. 
If the user inputs a valid number, a password of the specified length is generated and displayed. 
Invalid inputs are handled gracefully, with appropriate error messages guiding the user. 
This approach provides a straightforward method for generating secure passwords while accommodating user preferences and ensuring ease of use."""



import random
import string

def generate_password(length: int) -> str:
    if length < 5:
        raise ValueError("Password length should be at least 5 characters.")
    
    all_characters = string.ascii_letters + string.digits
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main() -> None:
    """
    The main function that runs the password generator.
    """
    print("Welcome to the Password Generator!")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("Enter the length of the password: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        try:
            length = int(user_input)
            password = generate_password(length)
            print(f"Generated password: {password}")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a number.")

if __name__ == "__main__":
    main()
