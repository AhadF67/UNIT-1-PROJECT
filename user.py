import json
from colorama import *
from utility import *
from manager import load_services, save_complaints

mobiles, users = load_users_data()

class User:
    def __init__(self, name, mobile, password):
        self.name = name
        self.mobile = mobile
        self.password = password
        self.balance = 0
        self.transactions = []
        self.requests = []
        self.services = []

    @staticmethod
    def signup(name, mobile, password):
        global users
        users[mobile] = {'name': name, 'password': password}
        mobiles.add(mobile)
        save_users_data(mobiles, users)
        print(Fore.GREEN + "You have registered as " + Fore.CYAN + "Customer" + Fore.GREEN + " successfully!")

    def en_services(self):
        while True:
            services = load_services()
            print("--------------------------------------")
            print("\tMashawyer Services")
            print("--------------------------------------")
            for idx, service in enumerate(services, 1):
                print(f"{idx}. {service}")
            print("5. << ")
            print("--------------------------------------")

            num = int(input(Fore.CYAN + "Choose number: "))
            if num == 5:
                break
            elif num <= len(services):
                desc = input(Fore.CYAN + "Describe the service: ")
                answ = input(Fore.CYAN + "Would you like to upload a picture for clarification? (Y/N): ")
                if answ.lower() == 'y':
                    print(Fore.CYAN + "Uploading...")
                self.services.append({'description': desc, 'status': 'Pending'})
                print(Fore.GREEN + f"Order for {services[num - 1]} created successfully.")
            else:
                print(Fore.RED + "Invalid choice!")

    @staticmethod
    def load_users_data(file='users.txt'):
        data = load_data(file)
        return set(data.get('mobiles', [])), data.get('users', {})

    def users_account(self):
        while True:
            print("--------------------------------------")
            print("\tAccount")
            print("--------------------------------------")
            print("1. Change Password")
            print("2. Change Mobile Number")
            print("3. Delete Account")
            print("4. << ")
            print("--------------------------------------")

            choice = int(input(Fore.CYAN + "Choose number: "))
            if choice == 1:
                self.change_password()
            elif choice == 2:
                self.change_mobile()
            elif choice == 3:
                self.delete_account()
            elif choice == 4:
                break
            else:
                print(Fore.RED + "Invalid choice!")

    def users_wallet(self):
        while True:
            print("--------------------------------------")
            print("\tWallet")
            print("--------------------------------------")
            print("1. Current Balance")
            print("2. Top-Up Money")
            print("3. Show Transactions")
            print("4. Money Requests")
            print("5. << ")
            print("--------------------------------------")

            choice = int(input(Fore.CYAN + "Choose number: "))
            if choice == 1:
                print(Fore.CYAN + f"Your current balance: {self.balance}SR")
            elif choice == 2:
                self.topup()
            elif choice == 3:
                self.show_transactions()
            elif choice == 4:
                self.money_requests()
            elif choice == 5:
                break
            else:
                print(Fore.RED + "Invalid choice!")

    def complain(self):
        complaint = input(Fore.CYAN + "Enter your complaint: ")
        save_complaints(complaint)
        print(Fore.GREEN + "Complaint registered successfully.")

    def status(self):
        for idx, order in enumerate(self.services, 1):
            print(Fore.CYAN + f"{idx}- {order['description']} - {order['status']}")

    def change_password(self):
        old_password = input(Fore.CYAN + "Enter your old password: ")
        if old_password == self.password:
            new_password = input(Fore.CYAN + "Enter your new password: ")
            self.password = new_password
            users[self.mobile]['password'] = new_password
            save_users_data(mobiles, users)
            print(Fore.GREEN + "Password changed successfully!")
        else:
            print(Fore.RED + "Incorrect old password!")

    def change_mobile(self):
        old_mobile = input(Fore.CYAN + "Enter your old mobile number: ")
        if old_mobile == self.mobile:
            new_mobile = input(Fore.CYAN + "Enter your new mobile number: ")
            if new_mobile not in mobiles:
                self.mobile = new_mobile
                users[new_mobile] = users.pop(old_mobile)
                mobiles.remove(old_mobile)
                mobiles.add(new_mobile)
                save_users_data(mobiles, users)
                print(Fore.GREEN + "Mobile number changed successfully!")
            else:
                print(Fore.RED + "New mobile number already exists!")
        else:
            print(Fore.RED + "Incorrect old mobile number!")

    def delete_account(self):
        confirm = input(Fore.CYAN + "Are you sure you want to delete your account? (Y/N): ")
        if confirm.lower() == 'y':
            mobiles.remove(self.mobile)
            del users[self.mobile]
            save_users_data(mobiles, users)
            print(Fore.GREEN + "Account deleted successfully.")
        else:
            print(Fore.CYAN + "Account deletion cancelled.")

    def topup(self):
        amount = float(input(Fore.CYAN + "Enter the amount to top-up: "))
        self.balance += amount
        self.transactions.append({'type': 'top-up', 'amount': amount})
        print(Fore.GREEN + f"Account topped up successfully! New balance: {self.balance}SR")

    def show_transactions(self):
        if self.transactions:
            for idx, transaction in enumerate(self.transactions, 1):
                print(Fore.CYAN + f"{idx}. Type: {transaction['type']}, Amount: {transaction['amount']}SR")
        else:
            print(Fore.CYAN + "No transactions available.")

    def money_requests(self):
        if self.requests:
            for idx, request in enumerate(self.requests, 1):
                print(Fore.CYAN + f"{idx}. Description: {request['description']}, Amount: {request['amount']}SR")
        else:
            print(Fore.CYAN + "No money requests available.")

def users_en_menu(current_user):
    while True:
        print("--------------------------------------")
        print("\tMashawyer Services")
        print("--------------------------------------")
        print("1. Order Service")
        print("2. Account")
        print("3. Wallet")
        print("4. Order Status")
        print("5. File Order Complain")
        print("6. Exit")
        print("--------------------------------------")

        choice = int(input(Fore.CYAN + "Choose number: "))
        if choice == 1:
            current_user.en_services()
        elif choice == 2:
            current_user.users_account()
        elif choice == 3:
            current_user.users_wallet()
        elif choice == 4:
            current_user.status()
        elif choice == 5:
            current_user.complain()
        elif choice == 6:
            print(Fore.CYAN + "Thank you for using Mashawyer, See you soon!")
            break
        else:
            print(Fore.RED + "Invalid choice!")
