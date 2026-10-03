import random
import string

def gen_password(length):
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    simbols = string.punctuation
    
    password = ""
    for _ in range(length):
        password += random.choice(lowercase + uppercase + digits + simbols)
    return password

def analyze_password(password):
    Length = len(password)
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    punctuation = 0
    for caracter in password:
        if caracter.isupper():
            has_upper = True
        if caracter.islower():
            has_lower = True
        if caracter.isdigit():
            has_digit = True
        if not caracter.isalnum():
            has_symbol = True
    if Length >= 8:
        punctuation += 1
    if Length >= 12:
        punctuation += 1
    if has_upper:
        punctuation += 1
    if has_lower:
        punctuation += 1
    if has_digit:
        punctuation += 1
    if has_symbol:
        punctuation += 1
        
        
    if punctuation <= 2:
        return f"your punctuaction is:{punctuation}, Password is weak:{password}, Hacking time stimated in seconds: 1.5"
    if punctuation <= 4:
        return f"your punctuaction is:{punctuation}, Password is medium:{password}, Hacking time stimated in seconds: 3 days"
    if punctuation >= 5:
        return f"your punctuaction is:{punctuation}, Password is strong:{password}, Hacking time stimated in seconds: centuries"
    

while True:
    print("1. Generate password")
    print("2. Analyze password")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        length = int(input("Enter the length of the password: "))
        password = gen_password(length)
        print(f"Generated password: {password}")
    
    elif choice == "2":
        password = input("Enter the password to analyze: ")
        result = analyze_password(password)
        print(result)
    
    elif choice == "3":
        break
    
    else:
        print("Invalid choice. Please try again.")
        continue