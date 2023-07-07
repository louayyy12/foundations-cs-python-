def factorial(i):
    # Base case: If i is 0 or 1, the factorial is 1
    if i == 0 or i == 1:
        return 1
    else:
        # Recursive case: Multiply i with the factorial of (i-1)
        return i * factorial(i - 1)

# Prompt the user to enter a positive integer
number = int(input("Enter a positive integer: "))

# Call the factorial function to calculate the factorial of the input number
result = factorial(number)

# Print the result
print("The factorial of", number, "is", result)


#############################################################################################


def find_divisors(num):
    # Initialize an empty list to store the divisors
    divisors = []

    # Iterate over the numbers from 1 to num (inclusive)
    for i in range(1, num + 1):
        # Check if num is divisible by the current number
        if num % i == 0:
            # If it is, append the current number to the list of divisors
            divisors.append(i)
    
    # Return the list of divisors
    return divisors

# Prompt the user to enter an integer
num = int(input("Enter an integer: "))

# Call the find_divisors function to calculate the divisors of the input number
divisors = find_divisors(num)

# Print the list of divisors
print(divisors)



#############################################################################################



def reverseString(input_str):
    # Initialize an empty string to store the reversed string
    reversed_str = ""

    # Iterate over the indices of the characters in input_str in reverse order
    for i in range(len(input_str) - 1, -1, -1):
        # Append the character at the current index to reversed_str
        reversed_str += input_str[i]
    
    # Return the reversed string
    return reversed_str

# Prompt the user to enter a string
user_input = input("Enter a string: ")

# Call the reverseString function to reverse the input string
reversed_input = reverseString(user_input)

# Print the reversed string
print("Reversed string:", reversed_input)



#############################################################################################


def get_even_numbers(input_list):
    # Initialize an empty list to store the even numbers
    even_numbers = []

    # Iterate over the numbers in the input_list
    for num in input_list:
        # Check if the current number is even
        if num % 2 == 0:
            # If it is, append it to the even_numbers list
            even_numbers.append(num)
    
    # Return the list of even numbers
    return even_numbers

# Define an input list
input_list = [1, 2, 3, 4, 5, 6]

# Call the get_even_numbers function to get the even numbers from the input list
output_list = get_even_numbers(input_list)

# Print the list of even numbers
print(output_list)


#############################################################################################


def check_password_strength(password):
    # Check if the password length is less than 8
    if len(password) < 8:
        return "Weak password"

    # Initialize variables to track the presence of uppercase, lowercase, digit, and special characters
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False 

    # Iterate over each character in the password
    for char in password:
        # Check if the character is uppercase
        if char.isupper():
            has_uppercase = True
        # Check if the character is lowercase
        elif char.islower():
            has_lowercase = True
        # Check if the character is a digit
        elif char.isdigit():
            has_digit = True
        # Check if the character is a special character
        elif char in ['#', '?', '!', '$']:
            has_special = True

        # If all required character types are present, return "Strong password"
        if has_uppercase and has_lowercase and has_digit and has_special:
            return "Strong password"

    # If the loop completes without finding all required character types, return "Weak password"
    return "Weak password"

#############################################################################################



def is_valid_ipv4_address(address):
    # Split the address into octets based on the dot separator
    octets = address.split('.')

    # Check if there are exactly 4 octets
    if len(octets) != 4:
        return False

    # Iterate over each octet
    for octet in octets:
        # Check if the octet consists only of digits
        if not octet.isdigit():
            return False

        # Convert the octet to an integer value
        value = int(octet)

        # Check if the value is within the valid range of 0 to 255
        if value < 0 or value > 255:
            return False

        # Check if the octet has leading zeros (except for 0 itself)
        if len(octet) > 1 and octet[0] == '0':
            return False

    # If all checks pass, the address is a valid IPv4 address
    return True
