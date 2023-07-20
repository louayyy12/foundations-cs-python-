# JSON is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. It is often used for data serialization and communication between different systems
# The json module in Python allows you here to Work with files, The json.dump() function is used to write JSON data directly to a file, while json.load() function reads JSON data from a file



# Import the json module to work with JSON data.
import json

# Function to sum two tuples element-wise and return the result as a new tuple.
def sum_tuples(tup1, tup2):
    return tuple(a + b for a, b in zip(tup1, tup2))

# Function to export a dictionary to a JSON file.
def export_json(dictionary, filename):
    with open(filename, 'w') as file:
        json.dump(dictionary, file)

# Function to import data from a JSON file and return it as a list of dictionaries.
def import_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Function to display the menu options.
def display_menu():
    print("1. Sum Tuples")
    print("2. Export JSON")
    print("3. Import JSON")
    print("4. Exit")

# Function to get a valid choice from the user.
def get_user_choice():
    while True:
        choice = input("Enter a choice: ")
        if choice in ['1', '2', '3', '4']:
            return int(choice)
        print("Invalid choice. Please try again.")

# Function to handle the "Sum Tuples" menu option.
def sum_tuples_menu():
    tup1 = eval(input("Enter the first tuple: "))  # Note: Use with caution as eval can be unsafe.
    tup2 = eval(input("Enter the second tuple: "))  # Note: Use with caution as eval can be unsafe.
    result = sum_tuples(tup1, tup2)
    print("Result:", result)

# Function to handle the "Export JSON" menu option.
def export_json_menu():
    dictionary = eval(input("Enter the dictionary: "))  # Note: Use with caution as eval can be unsafe.
    filename = input("Enter the filename: ")
    export_json(dictionary, filename)
    print("JSON exported successfully.")

# Function to handle the "Import JSON" menu option.
def import_json_menu():
    filename = input("Enter the filename: ")
    data = import_json(filename)
    print("List of dictionaries:", data)

# Main program loop
while True:
    display_menu()
    choice = get_user_choice()

    if choice == 1:
        sum_tuples_menu()
    elif choice == 2:
        export_json_menu()
    elif choice == 3:
        import_json_menu()
    elif choice == 4:
        break 
