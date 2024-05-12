#---- Question 1:-

# 1.Decimal to Hexa, Hexa to Decimal Conversion

def decimal_to_hex(decimal):
    hex_digits = "0123456789ABCDEF"
    hex_value = ""

    # Validate input
    try:
        decimal = int(decimal)
    except ValueError:
        return "Invalid input. Please enter a valid decimal number."

    # Conversion process
    while decimal > 0:
        remainder = decimal % 16
        hex_value = hex_digits[remainder] + hex_value
        decimal = decimal // 16
    
    return hex_value

def hex_to_decimal(hexadecimal):
    decimal = 0
    hex_digits = "0123456789ABCDEF"

    # Validate input
    if not all(char.upper() in hex_digits for char in hexadecimal):
        return "Invalid input. Please enter a valid hexadecimal number."

    # Conversion process
    for digit in hexadecimal:
        decimal = decimal * 16 + hex_digits.index(digit.upper())
    return decimal


# ------------------------------------------------------------------------------------------------------------------------
# Question 2:-
 
 # 2.Maskify user mobile number

def maskify(number):
    if len(number) <= 3:
        return number
    else:
        return "#" * (len(number) - 3) + number[-3:]

# Example usage:
mobile_number = input("Enter your mobile number: ")
print("Masked mobile number:", maskify(mobile_number))


#-----------------------------------------------------------------------------------------------------------------------------------
# Question 3:- 

# 3. OOPS

class Person:
    def __init__(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.mobile = input("Enter mobile number: ")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_mobile(self):
        return self.mobile

# Example usage:
person = Person()
print("Name:", person.get_name())
print("Age:", person.get_age())
print("Mobile:", person.get_mobile())


#--------------------------------------------------------------------------------------------------------------------------
# Question 4:- 

# 4. Validate the Password

def is_safe_password(password):
    # Check length
    if len(password) < 8:
        return "Password is not safe. It should be at least 8 characters long."

    # Check for lowercase letters
    if not any(char.islower() for char in password):
        return "Password is not safe. It should contain at least one lowercase letter."

    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        return "Password is not safe. It should contain at least one uppercase letter."

    # Check for digits
    if not any(char.isdigit() for char in password):
        return "Password is not safe. It should contain at least one digit."

    # Check for special symbols
    if not any(char in '_@$' for char in password):
        return "Password is not safe. It should contain at least one of the symbols '_', '@', or '$'."

    # All checks passed
    return "Password is safe."

# Example usage:
password = input("Enter a password: ")
print(is_safe_password(password))
