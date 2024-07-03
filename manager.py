from colorama import *
from utility import *

services_file = 'services.txt'
complaints_file = 'complaints.txt'

class Manager:
    @staticmethod
    def add_service():
        services = load_services()
        service_name = input(Fore.LIGHTBLUE_EX + "Enter service name: ")
        services.append(service_name)
        save_services(services)
        print(Fore.GREEN + "Service added successfully!")

    @staticmethod
    def answ_complains():
        complaints = load_complaints()
        if not complaints:
            print(Fore.RED + "No complaints to answer.")
            return

        for idx, complaint in enumerate(complaints, 1):
            print(Fore.LIGHTBLUE_EX + f"{idx}. {complaint}")

        try:
            num = int(input(Fore.LIGHTBLUE_EX + "Choose complaint number to answer: "))
            if 1 <= num <= len(complaints):
                response = input(Fore.LIGHTBLUE_EX + "Enter your response: ")
                print(Fore.GREEN + f"Response to complaint {num}: {response}")
                complaints.pop(num - 1)
                save_complaints(complaints)
            else:
                print(Fore.RED + "Invalid complaint number!")
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a number.")

def load_services():
    return load_data(services_file).get('services', [])

def save_services(services):
    save_data({'services': services}, services_file)

def load_complaints():
    return load_data(complaints_file).get('complaints', [])

def save_complaints(complaints):
    save_data({'complaints': complaints}, complaints_file)
