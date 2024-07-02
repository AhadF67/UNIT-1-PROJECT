import json

def save_data(data, file):
    with open(file, 'w') as f:
        json.dump(data, f)

def load_data(file):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users_data(mobiles, users, file='users.txt'):
    data = {'mobiles': list(mobiles), 'users': users}
    save_data(data, file)

def load_users_data(file='users.txt'):
    data = load_data(file)
    return set(data.get('mobiles', [])), data.get('users', {})

def save_drivers_data(mobiles, drivers, file='drivers.txt'):
    data = {'mobiles': list(mobiles), 'drivers': drivers}
    save_data(data, file)

def load_drivers_data(file='drivers.txt'):
    data = load_data(file)
    return set(data.get('mobiles', [])), data.get('drivers', {})
