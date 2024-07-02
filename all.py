import json
import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Define global variables
mobiles = []
users = {}
drivers = {}
managers = {}

def save_data(data, file):
    with open(file, 'w') as f:
        json.dump(data, f)

def load_data(file):
    try:
        with open(file, 'r') as f:
            if f.read().strip():  # Check if file is not empty
                f.seek(0)  # Reset file pointer to the beginning
                data = json.load(f)
                return data
            else:
                return {}  # Return empty dict if file is empty
    except FileNotFoundError:
        return {}

def save_drivers_data(mobiles, drivers, file='drivers.txt'):
    data = {
        'mobiles': list(mobiles),
        'drivers': drivers
    }
    save_data(data, file)

def load_drivers_data(file='drivers.txt'):
    data = load_data(file)
    return set(data.get('mobiles', [])), data.get('drivers', {})

def save_users_data(mobiles, users, file='users.txt'):
    data = {
        'mobiles': list(mobiles),
        'users': users
    }
    save_data(data, file)

def load_users_data(file='users.txt'):
    data = load_data(file)
    return set(data.get('mobiles', [])), data.get('users', {})

def load_managers_data(file='managers.txt'):
    data = load_data(file)
    return set(data.get('mobiles', [])), data.get('managers', {})

def save_service(serv, file='services.txt'):
    save_data(serv, file)

def load_service(file='services.txt'):
    return load_data(file)

mobiles, drivers = load_drivers_data()
mobiles, users = load_users_data()
mobiles, managers = load_managers_data()

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
        print(Fore.GREEN + "You have registered as Driver successfully!")

    def wallet(self):
        print(Fore.LIGHTBLUE_EX + f"Your current balance: {self.balance}SR")
        print("1. See Current Balance")
        print("2. Request Money")
        print("3. Show Transactions")
        print("4. Pay Bill")
        choice = int(input("Choose number: "))
        
        if choice == 1:
            print(Fore.LIGHTBLUE_EX + f"Your current balance: {self.balance}SR")
        elif choice == 2:
            self.request_money()
        elif choice == 3:
            self.show_transactions()
        elif choice == 4:
            self.pay_bill()
        else:
            print(Fore.RED + "Invalid choice!")

    def request_money(self):
        amount = float(input("Enter request amount: "))
        description = input("Enter description: ")
        self.requests.append({'amount': amount, 'description': description})
        print(Fore.GREEN + "Request submitted successfully.")

    def show_transactions(self):
        for transaction in self.transactions:
            print(Fore.LIGHTBLUE_EX + f"Date: {transaction['date']}, Amount: {transaction['amount']}, Total Balance: {transaction['balance']}SR")

    def pay_bill(self):
        bill_amount = float(input("Enter bill amount: "))
        if self.balance >= bill_amount:
            self.balance -= bill_amount
            print(Fore.GREEN + f"Bill paid successfully! Your current balance: {self.balance}SR")
        else:
            print(Fore.RED + "Insufficient balance to pay the bill.")

    def status(self):
        for idx, order in enumerate(self.orders, 1):
            print(Fore.LIGHTBLUE_EX + f"{idx}- {order['description']} - {order['status']}")
    
    def orders(self):
        for order in self.orders:
            print(Fore.LIGHTBLUE_EX + f"Order #{order['id']}: {order['description']}")
            response = input("Do you want to accept this order? (Y/N): ")
            if response.lower() == 'y':
                order['status'] = "Accepted"
            else:
                order['status'] = "Rejected"

class Manager:
    def menu(self):
        print("--------------------------------------")
        print("\tCustomer Support")
        print("--------------------------------------")
        print("1. Change Password")
        print("2. Change Mobile Number")
        print("3. Delete Account")
        print("4. File Order Complain")
        print("5. Exit")
        print("--------------------------------------")
    
    @staticmethod
    def add_service():
        serv = input("Enter new service: ")
        services = load_service()
        services.append(serv)
        save_service(services)
        print(Fore.GREEN + "Service added successfully.")
        
    @staticmethod
    def answ_complains():
        pass
    
    def wrong_password(self, mobile, name):
        print(f"Welcome {name}, sorry to hear that you can't access your account")
        new_pass = input("Please enter your new password: ")
        confirm_pass = input("Please re-enter your new password: ")
        if new_pass == confirm_pass:
            print(Fore.GREEN + "Your password has been changed successfully!")
        else:
            print(Fore.RED + "Passwords don't match, try again")
    
    def change_password(self, current_password):
        old_pass = input("Please enter your old password: ")
        if old_pass == current_password:
            new_pass = input("Please enter your new password: ")
            confirm_pass = input("Please re-enter your new password: ")
            if new_pass == confirm_pass:
                print(Fore.GREEN + "Your password has been changed successfully!")
            else:
                print(Fore.RED + "Passwords don't match, try again")
        else:
            print(Fore.RED + "Incorrect password, try again")
    
    def change_mobile(self, mobile):
        new_mobile = input("Please enter your new mobile number: ")
        confirm_new_mobile = input("Please confirm your new mobile number: ")
        if new_mobile == confirm_new_mobile and new_mobile != mobile:
            code = input("Enter the 4-digits code sent to your new mobile: ")
            if code:
                print(Fore.GREEN + "Mobile number changed successfully!")
        else:
            print(Fore.RED + "Mobile numbers don't match or new mobile is the same as the old one.")
    
    def delete_account(self, password):
        password = input("Enter your password: ")
        if password == password:
            confirmation = input("Are you sure you want to delete your account? (Y/N): ")
            if confirmation.lower() == 'y':
                print(Fore.RED + "We are sorry to see you leaving...")
    
    def complain(self):
        order_number = input("Enter your order number: ")
        complain_text = input("Enter your complain: ")
        print(Fore.GREEN + "Our team received your complain successfully, you will be contacted shortly.")

class User:
    def __init__(self, name, mobile, password):
        self.name = name
        self.mobile = mobile
        self.password = password
        self.balance = 0
        self.requests = []
        self.services = []
    
    @staticmethod
    def signup(name, mobile, password):
        global users
        users[mobile] = {'name': name, 'password': password}
        mobiles.add(mobile)
        save_users_data(mobiles, users)
        print(Fore.GREEN + "You have registered as Customer successfully!")
    
    def en_services(self):
        services = load_service()
        print("--------------------------------------")
        print("\tMashawyer Services")
        print("--------------------------------------")
        for idx, service in enumerate(services, 1):
            print(f"{idx}. {service}")
        print("5. Return to Main Menu")
        print("--------------------------------------")
        
        num = int(input("Choose number: "))
        if num == 5:
            users_en_menu()
        elif num <= len(services):
            desc = input("Describe the service: ")
            answ = input("Would you like to upload picture for clarification? (Y, N): ")
            if answ.lower() == 'y':
                print("Uploading...")
            self.services.append(services[num - 1])
            print(Fore.GREEN + f"Order for {services[num - 1]} created successfully.")
        else:
            print(Fore.RED + "Invalid choice!")

def login_as_user():
    mobile = input("Enter your mobile number: ")
    if mobile in users:
        password = input("Enter your password: ")
        if users[mobile]['password'] == password:
            print(Fore.GREEN + f"Welcome back, {users[mobile]['name']}")
            users_en_menu()
        else:
            print(Fore.RED + "Invalid password!")
            user_forgot_password(mobile)
    else:
        print(Fore.RED + "User not found!")

def users_en_menu():
    print("--------------------------------------")
    print("\tMashawyer Services")
    print("--------------------------------------")
    print("1. Order Service")
    print("2. Change Password")
    print("3. Change Mobile Number")
    print("4. Delete Account")
    print("5. File Order Complain")
    print("6. Exit")
    print("--------------------------------------")

def user_forgot_password(mobile):
    print(f"Hello, we see that your phone number is {mobile}")
    choice = input("Do you remember your password? (Y/N): ")
    if choice.lower() == 'n':
        print("Changing password...")
    else:
        login_as_user()

def login_as_driver():
    mobile = input("Enter your mobile number: ")
    if mobile in drivers:
        password = input("Enter your password: ")
        if drivers[mobile]['password'] == password:
            print(Fore.GREEN + f"Welcome back, {drivers[mobile]['name']}")
            driver_en_menu()
        else:
            print(Fore.RED + "Invalid password!")
            driver_forgot_password(mobile)
    else:
        print(Fore.RED + "Driver not found!")

def driver_forgot_password(mobile):
    print(f"Hello, we see that your phone number is {mobile}")
    choice = input("Do you remember your password? (Y/N): ")
    if choice.lower() == 'n':
        print("Changing password...")
    else:
        login_as_driver()

def driver_en_menu():
    print("--------------------------------------")
    print("\tMashawyer Driver")
    print("--------------------------------------")
    print("1. Orders")
    print("2. Wallet")
    print("3. Status")
    print("4. Complain")
    print("5. Exit")
    print("--------------------------------------")

def login_as_manager():
    password = input("Enter manager password: ")
    if password == "admin":
        print(Fore.GREEN + "Welcome, Manager!")
        manager_en_menu()
    else:
        print(Fore.RED + "Invalid password!")

def manager_en_menu():
    print("--------------------------------------")
    print("\tManager Portal")
    print("--------------------------------------")
    print("1. Add Service")
    print("2. Answer Complains")
    print("3. Exit")
    print("--------------------------------------")
    
    
def main():
    print("--------------------------------------")
    print("\tMashawyer Service")
    print("--------------------------------------")
    print("1. Login as User")
    print("2. Login as Driver")
    print("3. Login as Manager")
    print("4. Signup as User")
    print("5. Signup as Driver")
    print("6. Exit")
    print("--------------------------------------")
    
    num = int(input("Choose number: "))
    if num == 1:
        login_as_user()
    elif num == 2:
        login_as_driver()
    elif num == 3:
        login_as_manager()
    elif num == 4:
        name = input("Enter your name: ")
        mobile = input("Enter your mobile number: ")
        password = input("Enter your password: ")
        User.signup(name, mobile, password)
    elif num == 5:
        name = input("Enter your name: ")
        mobile = input("Enter your mobile number: ")
        password = input("Enter your password: ")
        Driver.signup(name, mobile, password)
    elif num == 6:
        exit()
    else:
        print(Fore.RED + "Invalid choice!")


main()

