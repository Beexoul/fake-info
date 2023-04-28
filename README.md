# FakeInfoGenerator

The `FakeInfoGenerator` is a Python script that generates fake personal information such as names, email addresses, street addresses, cities, states, and zip codes. It can be used for testing, generating sample data, or any other purpose that requires fake information.

## Usage

1. Clone or download the `fake_info_generator.py` file.

2. Make sure you have Python installed on your system.

3. Run the script using the following command:

   ```shell

   python fake_info_generator.py

   ```
4. The script will generate random fake information and display it in the console.

# Generated Information
The `fake_info_generator.py` script generates the following fake information:

First Name: Randomly selected from a list of common Nepali first names.
Last Name: Randomly selected from a list of common Nepali last names.
Email: A random email address generated using the first name, last name, and a random number.
Street Address: Randomly generated street number and name from a list of Nepali street names.
City: Randomly selected from a list of Nepali cities.
State: Randomly selected from a list of Nepali states.
Zip Code: A random 5-digit zip code.

# Customization
You can customize the lists of first names, last names, email domains, street names, cities, and states in the script to match your requirements. Simply edit the respective lists in the script.

```shell
FIRST_NAMES = ["Hari", "Gita", "Rajan", "Sita", "Suresh", "Sabina", "Roshan", "Sunita", "Binod", "Saraswati"]
LAST_NAMES = ["Shrestha", "Tamang", "Gurung", "Rai", "Karki", "Sharma", "Bhandari", "Thapa", "Bista", "Magar"]
EMAIL_DOMAINS = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com", "icloud.com"]
STREET_NAMES = ["Baghbazar Marg", "Asan Tole", "Durbarmarg", "New Road", "Jawalakhel Road", "Kamaladi Road", "Baluwatar Marg", "Lazimpat Road", "Koteswor Road", "Baneshwor Marg"]
CITIES = ["Kathmandu", "Pokhara", "Biratnagar", "Bharatpur", "Nepalgunj", "Dharan", "Butwal", "Bhaktapur", "Janakpur", "Itahari"]
STATES = ["P1", "P2", "P3", "P4", "P5"]
```

# Output

```bash
First Name: Sabina
Last Name: Gurung
Email: sabina.gurung70@aol.com     
Street Address: 837 Jawalakhel Road
City: Bhaktapur
State: P4
Zip Code: 55298
```