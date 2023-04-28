import random

FIRST_NAMES = ["Hari", "Gita", "Rajan", "Sita", "Suresh", "Sabina", "Roshan", "Sunita", "Binod", "Saraswati"]
LAST_NAMES = ["Shrestha", "Tamang", "Gurung", "Rai", "Karki", "Sharma", "Bhandari", "Thapa", "Bista", "Magar"]
EMAIL_DOMAINS = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com", "icloud.com"]
STREET_NAMES = ["Baghbazar Marg", "Asan Tole", "Durbarmarg", "New Road", "Jawalakhel Road", "Kamaladi Road", "Baluwatar Marg", "Lazimpat Road", "Koteswor Road", "Baneshwor Marg"]
CITIES = ["Kathmandu", "Pokhara", "Biratnagar", "Bharatpur", "Nepalgunj", "Dharan", "Butwal", "Bhaktapur", "Janakpur", "Itahari"]
STATES = ["P1", "P2", "P3", "P4", "P5"]

def generate_first_name():
    return random.choice(FIRST_NAMES)

def generate_last_name():
    return random.choice(LAST_NAMES)

def generate_email(first_name, last_name):
    domain = random.choice(EMAIL_DOMAINS)
    email = f"{first_name.lower()}.{last_name.lower()}{random.randint(0, 99)}@{domain}"
    return email

def generate_street_address():
    street_number = random.randint(1, 1000)
    street_name = random.choice(STREET_NAMES)
    return f"{street_number} {street_name}"

def generate_city():
    return random.choice(CITIES)

def generate_state():
    return random.choice(STATES)

def generate_zip_code():
    zip_code = "".join([str(random.randint(0, 9)) for _ in range(5)])
    return zip_code

def main():
    first_name = generate_first_name()
    last_name = generate_last_name()
    email = generate_email(first_name, last_name)
    street_address = generate_street_address()
    city = generate_city()
    state = generate_state()
    zip_code = generate_zip_code()

    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Email: {email}")
    print(f"Street Address: {street_address}")
    print(f"City: {city}")
    print(f"State: {state}")
    print(f"Zip Code: {zip_code}")

if __name__ == "__main__":
    main()