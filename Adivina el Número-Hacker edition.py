import random
import time


def show_banner():
    print("██╗  ██╗ █████╗  ██████╗██╗  ██╗")
    time.sleep(0.5)
    print("██║  ██║██╔══██╗██╔════╝██║ ██╔╝")
    time.sleep(0.5)
    print("███████║███████║██║     █████╔╝ ")
    time.sleep(0.5)
    print("██╔══██║██╔══██║██║     ██╔═██╗ ")
    time.sleep(0.5)
    print("██║  ██║██║  ██║╚██████╗██║  ██╗")
    time.sleep(0.5)
    print("╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝")
    
    
    print("========================================")
    print("   [+] SISTEMA DE SEGURIDAD v1.0        ")
    print("   [+] INICIANDO PROTOCOLO DE ACCESO    ")
    print("========================================")
    
def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = False
    
    while not guess:
        user = input("guess a number between 1 and 100:  ")
        try:
            user = int(user)
            attempts += 1
            if user == number_to_guess:
                print(f"ACCESS GRANTED:{number_to_guess} in {attempts} attempts.")
                guess = True
            
            elif user < number_to_guess:
                print("ACCESS DENIED: The number is higher.")
                attempts += 1
            elif user > number_to_guess:
                print("ACCESS DENIED: The number is lower.")
                attempts += 1
            if attempts == 10:
                print(f"ACCESS DENIED too many attempts: {attempts}. The number was {number_to_guess}.")
                guess = True
                break
        except ValueError:
            print("ACCESS DENIED: Please enter valid characters.")
            

while True:
    show_banner()
    print("1. Guess the number")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        guess_number()
    
    elif choice == "2":
        print("Finishing the program...")
        break
    else:
        print("ACCESS DENIED: Please enter valid characters.")
    