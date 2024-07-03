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
    except json.JSONDecodeError:
        raise ValueError(f"File {file} contains invalid JSON.")

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

def save_request(data, file='requests.txt'):
    requests = load_data(file).get('requests', [])
    requests.append(data)
    save_data({'requests': requests}, file)

def load_requests(file='requests.txt'):
    return load_data(file).get('requests', [])

def update_requests(requests, file='requests.txt'):
    save_data({'requests': requests}, file)

def save_order(data, file='orders.txt'):
    orders = load_data(file).get('orders', [])
    orders.append(data)
    save_data({'orders': orders}, file)

def load_orders(file='orders.txt'):
    return load_data(file).get('orders', [])

def update_orders(orders, file='orders.txt'):
    save_data({'orders': orders}, file)
