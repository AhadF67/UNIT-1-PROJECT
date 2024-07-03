from colorama import *
from user import User
from driver import Driver
from manager import Manager

def main():
    print(Fore.WHITE+"--------------------------------------")
    print("\tWelcome to Mashawyer")
    print("--------------------------------------")
    print("1. User")
    print("2. Driver")
    print("3. Manager")
    print("--------------------------------------")

    role_choice = input("Choose your role (1/2/3): ")
    if role_choice not in ['1', '2', '3']:
        print(Fore.RED + "Invalid role choice!")
        return

    if role_choice == '1':
        mobile = input(Fore.LIGHTMAGENTA_EX+"Enter your mobile number: ")
        password = input( "Enter your password: ")
        user = User(name, mobile, password)
        user.user_en_menu()
    elif role_choice == '2': 
        mobile = input(Fore.YELLOW+"Enter your mobile number: ")
        password = input("Enter your password: ")
        driver = Driver(name, mobile, password)
        driver.driver_en_menu()
    elif role_choice == '3':
        password = input(Fore.LIGHTBLUE_EX+"Enter Manager password: ")
        if password == "admin":
            manager = Manager()
            while True:
                print(Fore.WHITE + "1. Add Service")
                print("2. Answer Complaints")
                print("3. Exit")
                choice = input("Choose number: ")
                if choice == '1':
                    manager.add_service()
                elif choice == '2':
                    manager.answ_complains()
                elif choice == '3':
                    print(Fore.WHITE+"Thank you for managing Mashawyer, See you soon!")
                    break
                else:
                    print(Fore.RED + "Invalid choice!")

if __name__ == "__main__":
    main()
