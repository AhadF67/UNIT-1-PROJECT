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
        if mobile in users:
            raise ValueError("Mobile number already registered.")
        users[mobile] = {'name': name, 'password': password}
        mobiles.add(mobile)
        save_users_data(mobiles, users)
        print(Fore.GREEN + "You have registered as User successfully!")

    def wallet(self):
        while True:
            print(f"Your current balance: {self.balance}SR")
            print("1. See Current Balance")
            print("2. Add Money")
            print("3. Show Transactions")
            print("4. << ")
            choice = input("Choose number: ")

            if not choice.isdigit():
                print(Fore.RED + "Invalid choice!")
                continue

            choice = int(choice)
            if choice == 1:
                print(f"Your current balance: {self.balance}SR")
            elif choice == 2:
                self.add_money()
            elif choice == 3:
                self.show_transactions()
            elif choice == 4:
                break
            else:
                print(Fore.RED + "Invalid choice!")

    def add_money(self):
        try:
            amount = float(input(Fore.YELLOW + "Enter amount to add: "))
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            self.balance += amount
            self.transactions.append({'type': 'add', 'amount': amount})
            print(Fore.GREEN + f"Amount {amount}SR added to your balance successfully!")
        except ValueError as e:
            print(Fore.RED + str(e))

    def show_transactions(self):
        if not self.transactions:
            print(Fore.RED + "No transactions available.")
            return

        for idx, transaction in enumerate(self.transactions, 1):
            print(Fore.YELLOW + f"{idx}. Type: {transaction['type']}, Amount: {transaction['amount']}SR")

    def view_services(self):
        services = load_services()
        if not services:
            print(Fore.RED + "No services available.")
            return

        for idx, service in enumerate(services, 1):
            print(f"{idx}. {service}")

        try:
            num = int(input( "Choose service number to request: "))
            if 1 <= num <= len(services):
                description = input("Enter service description: ")
                order_data = {'service': services[num - 1], 'description': description, 'status': 'pending'}
                save_order(order_data)
                print(Fore.GREEN + "Service requested successfully.")
            else:
                print(Fore.RED + "Invalid service number!")
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a number.")

    def complain(self):
        complaint = input( "Enter your complaint: ")
        save_complaints(complaint)
        print(Fore.GREEN + "Complaint registered successfully.")

    def user_en_menu(self):
        while True:
            print("--------------------------------------")
            print("\tMashawyer User")
            print("--------------------------------------")
            print("1. Services")
            print("2. Wallet")
            print("3. Complain")
            print("4. Exit")
            print("--------------------------------------")

            choice = input("Choose number: ")
            if not choice.isdigit():
                print(Fore.RED + "Invalid choice!")
                continue

            choice = int(choice)
            if choice == 1:
                self.view_services()
            elif choice == 2:
                self.wallet()
            elif choice == 3:
                self.complain()
            elif choice == 4:
                print("Thank you for using Mashawyer, See you soon!")
                exit()
            else:
                print(Fore.RED + "Invalid choice!")
