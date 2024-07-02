from driver import Driver
from manager import Manager
from user import User, users_en_menu
from colorama import init, Fore, Style
from utility import load_drivers_data

init(autoreset=True)

# Global variables to hold the logged-in user or driver
current_user = None
current_driver = None

def user_forgot_password(mobile):
    print(f"Hello, we see that your phone number is {mobile}")
    choice = input(Fore.CYAN+ "Do you remember your password? (Y/N): ")
    if choice.lower() == 'n':
        print(Fore.CYAN+ "Changing password...")
    else:
        login_as_user()

def driver_forgot_password(mobile):
    print(f"Hello, we see that your phone number is {mobile}")
    choice = input(Fore.YELLOW+ "Do you remember your password? (Y/N): ")
    if choice.lower() == 'n':
        print(Fore.YELLOW+ "Changing password...")
    else:
        login_as_driver()

def login_as_manager():
    password = input(Fore.LIGHTBLUE_EX+"Enter manager password: ")
    if password == "admin":
        print(Fore.LIGHTBLUE_EX + "\nWelcome, Manager!")
        manager_en_menu()
    else:
        print(Fore.RED + "Invalid password!")

def manager_en_menu():
    while True:
        print("--------------------------------------")
        print("\tManager Portal")
        print("--------------------------------------")
        print("1. Add Service")
        print("2. Answer Complains")
        print("3. Exit")
        print("--------------------------------------")
        
        choice = int(input("Choose number: "))
        if choice == 1:
            Manager.add_service()
        elif choice == 2:
            Manager.answ_complains()
        elif choice == 3:
            print(Fore.LIGHTBLUE_EX +"Thank you for using Mashawyer, See you soon!")
            break
        else:
            print(Fore.RED + "Invalid choice!")

def login_as_user():
    global current_user
    mobile = input(Fore.CYAN+ "Enter your mobile number: ")
    password = input(Fore.CYAN+ "Enter your password: ")
    
    users = User.load_users_data()[1]  # Load users data

    if mobile in users and users[mobile]['password'] == password:
        current_user = User(users[mobile]['name'], mobile, password)
        while True:
            users_en_menu(current_user)
    else:
        print(Fore.RED + "Invalid login credentials!")

def login_as_driver():
    global current_driver
    mobile = input(Fore.YELLOW+ "Enter your mobile number: ")
    password = input(Fore.YELLOW+ "Enter your password: ")

    mobiles, drivers = load_drivers_data()  # Load drivers data

    if mobile in drivers and drivers[mobile]['password'] == password:
        current_driver = Driver(drivers[mobile]['name'], mobile, password)
        while True:
            current_driver.driver_en_menu()
    else:
        print(Fore.RED + "Invalid login credentials!")

def main():
    while True:
        print("--------------------------------------")
        print("\tMashawyer App")
        print("--------------------------------------")
        print("1. Customer")
        print("2. Driver")
        print("3. Manager")
        print("4. Exit")
        print("--------------------------------------")
        
        num = int(input("Choose number: "))
        if num == 1:
            U()
        elif num == 2:
            D()
        elif num == 3:
            login_as_manager()
        elif num == 4:  # Corrected exit option to 4 to match the prompt
            print("Thank you for using Mashawyer, See you soon!")
            break
        else:
            print(Fore.RED + "Invalid choice!")
        
def D():
    while True:
        print("--------------------------------------")
        print("\tMashawyer | Driver Options")
        print("--------------------------------------")
        print("1. Login as Driver")
        print("2. Signup as Driver")
        print("3. <<")
        print("--------------------------------------")
        
        num = int(input(Fore.YELLOW+ "Choose number: "))
        if num == 1:
            login_as_driver()
        elif num == 2:
            name = input(Fore.YELLOW+ "Enter your name: ")
            mobile = input(Fore.YELLOW+ "Enter your mobile number: ")
            password = input(Fore.YELLOW+ "Enter your password: ")
            Driver.signup(name, mobile, password)
        elif num == 3:
            break
        else:
            print(Fore.RED + "Invalid choice!")

def U():
    while True:
        print("--------------------------------------")
        print("\tMashawyer | Customer Options")
        print("--------------------------------------")
        print("1. Login as Customer")
        print("2. Signup as Customer")
        print("3. <<")
        print("--------------------------------------")
        
        num = int(input(Fore.CYAN+ "Choose number: "))
        if num == 1:
            login_as_user()
        elif num == 2:
            name = input(Fore.CYAN+ "Enter your name: ")
            mobile = input(Fore.CYAN+ "Enter your mobile number: ")
            password = input(Fore.CYAN+ "Enter your password: ")
            User.signup(name, mobile, password)
        elif num == 3:
            break
        else:
            print(Fore.RED + "Invalid choice!")

if __name__ == "__main__":
    main()
