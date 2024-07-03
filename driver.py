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
        if mobile in drivers:
            raise ValueError("Mobile number already registered.")
        drivers[mobile] = {'name': name, 'password': password}
        mobiles.add(mobile)
        save_drivers_data(mobiles, drivers)
        print(Fore.GREEN + "You have registered as Driver successfully!")

    def wallet(self):
        while True:
            print(Fore.WHITE+"1. See Current Balance")
            print("2. Request Money")
            #print("3. Show Transactions")
            #print("4. Pay Bill")
            print("3. << ")
            choice = input(Fore.YELLOW+"Choose number: ")

            if not choice.isdigit():
                print(Fore.RED + "Invalid choice!")
                continue

            choice = int(choice)
            if choice == 1:
                print(f"Your current balance: {self.balance}SR")
            elif choice == 2:
                self.request_money()
            #elif choice == 3:
                #self.check_transactions()
            #elif choice == 4:
                #self.pay_bill()
            elif choice == 3:
                break
            else:
                print(Fore.RED + "Invalid choice!")

    def request_money(self):
        try:
            amount = float(input( Fore.YELLOW+"Enter request amount: "))
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            description = input("Enter description: ")
            request_data = {'amount': amount, 'description': description, 'status': 'pending'}
            save_request(request_data)
            print(Fore.GREEN + "Request submitted successfully.")
        except ValueError as e:
            print(Fore.RED + str(e))

    def check_transactions(self):
        requests = load_requests()
        for request in requests:
            if request['status'] == 'accepted':
                self.balance += request['amount']
                print(Fore.GREEN + f"Amount {request['amount']}SR added to your balance from customer.")
        update_requests([r for r in requests if r['status'] != 'accepted'])

    def pay_bill(self):
        try:
            bill_amount = float(input("Enter bill amount: "))
            if bill_amount <= 0:
                raise ValueError("Bill amount must be positive.")
            if self.balance >= bill_amount:
                self.balance -= bill_amount
                print(Fore.GREEN + f"Bill paid successfully! Your current balance: {self.balance}SR")
            else:
                print(Fore.RED + "Insufficient balance to pay the bill.")
        except ValueError as e:
            print(Fore.RED + str(e))

    def view_orders(self):
        orders = load_orders()
        if not orders:
            print(Fore.RED + "No orders available.")
            return

        for idx, order in enumerate(orders, 1):
            try:
                service = order['service']
                description = order['description']
                status = order['status']
                print(Fore.WHITE + f"{idx}. Service: {service}, Description: {description}, Status: {status}")
            except KeyError as e:
                print(Fore.RED + f"Order {idx} is missing key: {e}")

        try:
            num = int(input(Fore.YELLOW+"Choose order number to update: "))
            if 1 <= num <= len(orders):
                print(Fore.WHITE+"1. Accepted")
                print("2. In Progress")
                print("3. Finished")
                status_choice = int(input(Fore.YELLOW+"Choose status number: "))
                if status_choice == 1:
                    new_status = 'accepted'
                elif status_choice == 2:
                    new_status = 'in progress'
                elif status_choice == 3:
                    new_status = 'finished'
                else:
                    print(Fore.RED + "Invalid status choice!")
                    return
                orders[num - 1]['status'] = new_status
                update_orders(orders)
                print(Fore.GREEN + f"Order #{num} status updated to {new_status}.")
            else:
                print(Fore.RED + "Invalid order number!")
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a number.")


    def complain(self):
        complaint = input(Fore.YELLOW+"Enter your complaint: ")
        save_complaints(complaint)
        print(Fore.GREEN + "Complaint registered successfully.")

    def driver_en_menu(self):
        while True:
            print(Fore.WHITE+"--------------------------------------")
            print("\tMashawyer Driver")
            print("--------------------------------------")
            print("1. Orders")
            print("2. Wallet")
            print("3. Complain")
            print("4. Exit")
            print("--------------------------------------")

            choice = input( Fore.YELLOW+"Choose number: ")
            if not choice.isdigit():
                print(Fore.RED + "Invalid choice!")
                continue

            choice = int(choice)
            if choice == 1:
                self.view_orders()
            elif choice == 2:
                self.wallet()
            elif choice == 3:
                self.complain()
            elif choice == 4:
                print(Fore.WHITE+"Thank you for using Mashawyer, See you soon!")
                exit()
            else:
                print(Fore.RED + "Invalid choice!")
