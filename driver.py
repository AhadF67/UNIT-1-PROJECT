import json
from colorama import *
from utility import *  
from manager import save_complaints

mobiles, drivers = load_drivers_data()

class Driver:
    def __init__(self, name, mobile, password):
        self.name = name
        self.mobile = mobile
        self.password = password
        self.balance = 0
        self.requests = []
        self.orders = []

    @staticmethod
    def signup(name, mobile, password):
        global drivers
        drivers[mobile] = {'name': name, 'password': password}
        mobiles.add(mobile)
        save_drivers_data(mobiles, drivers)
        print(Fore.GREEN + "You have registered as "+ Fore.YELLOW +"Driver" +Fore.GREEN +" successfully!")

    def wallet(self):
        while True:
            print(Fore.YELLOW + f"Your current balance: {self.balance}SR")
            print("1. See Current Balance")
            print("2. Request Money")
            print("3. Show Transactions")
            print("4. Pay Bill")
            print("5. << ")
            choice = int(input(Fore.YELLOW +"Choose number: "))
            
            if choice == 1:
                print(Fore.YELLOW + f"Your current balance: {self.balance}SR")
            elif choice == 2:
                self.request_money()
            elif choice == 3:
                self.show_transactions()
            elif choice == 4:
                self.pay_bill()
            elif choice == 5:
                break
            else:
                print(Fore.RED + "Invalid choice!")

    def request_money(self):
        amount = float(input(Fore.YELLOW +"Enter request amount: "))
        description = input(Fore.YELLOW +"Enter description: ")
        self.requests.append({'amount': amount, 'description': description})
        print(Fore.GREEN + "Request submitted successfully.")

    def show_transactions(self):
        for transaction in self.transactions:
            print(Fore.YELLOW + f"Date: {transaction['date']}, Amount: {transaction['amount']}, Total Balance: {transaction['balance']}SR")

    def pay_bill(self):
        bill_amount = float(input(Fore.YELLOW +"Enter bill amount: "))
        if self.balance >= bill_amount:
            self.balance -= bill_amount
            print(Fore.GREEN + f"Bill paid successfully!"+ Fore.YELLOW +"Your current balance: {self.balance}SR")
        else:
            print(Fore.RED + "Insufficient balance to pay the bill.")

    def status(self):
        for idx, order in enumerate(self.orders, 1):
            print(Fore.YELLOW + f"{idx}- {order['description']} - {order['status']}")
    
    def view_orders(self):
        for order in self.orders:
            print(Fore.YELLOW + f"Order #{order['id']}: {order['description']}")
            response = input(Fore.YELLOW +"Do you want to accept this order? (Y/N): ")
            if response.lower() == 'y':
                order['status'] = "Accepted"
                self.balance += order['amount']
                print(Fore.GREEN + f"Order #{order['id']} accepted. "+Fore.YELLOW +"Your balance is now {self.balance}SR")
            else:
                order['status'] = "Rejected"
                print(Fore.RED + f"Order #{order['id']} rejected.")
    
    def complain(self):
        complaint = input(Fore.YELLOW +"Enter your complaint: ")
        save_complaints(complaint)
        print(Fore.GREEN + "Complaint registered successfully.")
        
    def driver_en_menu(self):
        while True:
            print("--------------------------------------")
            print("\tMashawyer Driver")
            print("--------------------------------------")
            print("1. Orders")
            print("2. Wallet")
            print("3. Status")
            print("4. Complain")
            print("5. Exit")
            print("--------------------------------------")

            choice = int(input(Fore.YELLOW +"Choose number: "))
            if choice == 1:
                self.view_orders()
            elif choice == 2:
                self.wallet()
            elif choice == 3:
                self.status()
            elif choice == 4:
                self.complain()
            elif choice == 5:
                print(Fore.YELLOW +"Thank you for using Mashawyer, See you soon!")
                break
            else:
                print(Fore.RED + "Invalid choice!")
