import queue
import datetime

class Ticket:
    def __init__(self, ticket_id, event_id, user_name, date, status, priority):
        self.ticket_id = ticket_id
        self.event_id = event_id
        self.user_name = user_name
        self.date = date
        self.status = status
        self.priority = priority

    def __str__(self):
        return f"Ticket ID: {self.ticket_id}, Event ID: {self.event_id}, User Name: {self.user_name}, Date: {self.date}, Status: {self.status}, Priority: {self.priority}"

####### import data from txt file : https://stackoverflow.com/questions/7485458/python-reading-text-file

def import_tickets_from_file():
    ticket_queue = queue.Queue()
    try:
        with open("Tickets.txt", "r") as file:
            for line in file:
                ticket_info = line.strip().split(', ')
                if len(ticket_info) == 6:
                    ticket = Ticket(*ticket_info)
                    ticket_queue.put(ticket)
    except FileNotFoundError:
        print("Tickets file not found.")
    return ticket_queue

#######################################

def book_ticket_user(ticket_queue):
    print("\n-- User Ticket Booking --")
    event_id = input("Enter Event ID: ")

    # Get the current system date and format it as YYYYMMDD
    current_date = datetime.datetime.now().strftime("%Y%m%d")

    # Auto-generate the ticket ID based on the queue size
    ticket_id = f"tick{ticket_queue.qsize() + 1:03}"

    # Prompt for the user name
    user_name = input("Enter Your Name: ")

    # Priority is set to 3 (low) for users
    priority = 3

    # Create a new Ticket object with the provided details and the current date
    new_ticket = Ticket(ticket_id, event_id, user_name, current_date, 0, priority)  # Assuming status is set to 0 for incomplete

    # Enqueue the new ticket into the ticket_queue
    ticket_queue.put(new_ticket)

    # Store the new ticket in the "Tickets.txt" file
    with open("Tickets.txt", "a") as file:
        file.write(f"{new_ticket.ticket_id}, {new_ticket.event_id}, {new_ticket.user_name}, {new_ticket.date}, {new_ticket.status}, {new_ticket.priority}\n")

    print("Ticket booked successfully!")

def user_menu(ticket_queue):
    while True:
        print("\n-- User Menu --")
        print("1. Book a Ticket")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_ticket_user(ticket_queue)
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1 or 2).")


######################################

### Display queue : https://stackoverflow.com/questions/71769815/how-to-dequeue-and-display-queue
def display_statistics(ticket_queue):
    event_tickets_count = {}
    for ticket in ticket_queue.queue:
        event_id = ticket.event_id
        if event_id in event_tickets_count:
            event_tickets_count[event_id] += 1
        else:
            event_tickets_count[event_id] = 1

    if event_tickets_count:
        max_tickets_event = max(event_tickets_count, key=event_tickets_count.get)
        print(f"Event ID with the highest number of tickets: {max_tickets_event}")
    else:
        print("No tickets found.")

######################

def book_ticket_admin(ticket_queue):
    print("\n-- Admin Ticket Booking --")
    event_id = input("Enter Event ID: ")

    # Get the current system date and format it as YYYYMMDD
    current_date = datetime.datetime.now().strftime("%Y%m%d")

    # Auto-generate the ticket ID based on the queue size
    ticket_id = f"tick{ticket_queue.qsize() + 1:03}"

    # Prompt for the user name
    user_name = input("Enter User Name: ")

    # Prompt for the priority (1 for high, 2 for medium, 3 for low)
    while True:
        try:
            priority = int(input("Enter the priority (1 for high, 2 for medium, 3 for low): "))
            if priority not in (1, 2, 3):
                raise ValueError
            break
        except ValueError:
            print("Invalid priority. Please enter 1 (high), 2 (medium), or 3 (low).")

    # Create a new Ticket object with the provided details and the current date
    new_ticket = Ticket(ticket_id, event_id, user_name, current_date, 0, priority)  # Assuming status is set to 0 for incomplete

    # Enqueue the new ticket into the ticket_queue
    ticket_queue.put(new_ticket)

    # Store the new ticket in the "Tickets.txt" file
    with open("Tickets.txt", "a") as file:
        file.write(f"{new_ticket.ticket_id}, {new_ticket.event_id}, {new_ticket.user_name}, {new_ticket.date}, {new_ticket.status}, {new_ticket.priority}\n")

    print("Ticket booked successfully on behalf of the user!")


######################

### Display queue : https://stackoverflow.com/questions/71769815/how-to-dequeue-and-display-queue

def display_all_tickets(ticket_queue):
    print("\n-- All Tickets --")
    if ticket_queue.empty():
        print("No tickets found.")
    else:
        for ticket in ticket_queue.queue:
            print(ticket)

######################

def change_ticket_priority(ticket_queue):
    print("\n-- Change Ticket Priority --")
    ticket_id = input("Enter Ticket ID to change its priority: ")
    found_ticket = None

    for ticket in ticket_queue.queue:
        if ticket.ticket_id == ticket_id:
            while True:
                try:
                    priority = int(input("Enter the new priority (1 for high, 2 for medium, 3 for low): "))
                    if priority not in (1, 2, 3):
                        raise ValueError
                    ticket.priority = priority
                    found_ticket = ticket
                    break
                except ValueError:
                    print("Invalid priority. Please enter 1 (high), 2 (medium), or 3 (low).")
            print("Ticket priority changed successfully.")
            break

    if found_ticket is None:
        print(f"Ticket with ID '{ticket_id}' not found.")
    else:
        # Update the ticket in the Tickets.txt file
        with open("Tickets.txt", "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            ticket_data = line.strip().split(", ")
            if ticket_data[0] == found_ticket.ticket_id:
                ticket_data[-1] = str(found_ticket.priority)
                lines[i] = ", ".join(ticket_data) + "\n"
                break

        with open("Tickets.txt", "w") as file:
            file.writelines(lines)

######################
#### Remove ticket from queu : https://stackoverflow.com/questions/64365042/remove-or-edit-item-from-python-queue

def disable_ticket(ticket_queue):
    print("\n-- Disable Ticket --")
    ticket_id = input("Enter Ticket ID to disable: ")

    found_ticket = None
    for ticket in ticket_queue.queue:
        if ticket.ticket_id == ticket_id:
            found_ticket = ticket
            break

    if found_ticket:
        ticket_queue.queue.remove(found_ticket)
        print(f"Ticket with ID '{ticket_id}' has been disabled and removed from the system.")
        # Update the Tickets.txt file to remove the ticket with the specified ID
        with open("Tickets.txt", "r") as file:
            lines = file.readlines()

        with open("Tickets.txt", "w") as file:
            for line in lines:
                if line.startswith(ticket_id):
                    continue
                file.write(line)
    else:
        print(f"Ticket with ID '{ticket_id}' not found. Please enter a valid Ticket ID.")



######################

def run_events(ticket_queue):
    print("\n-- Today's Events --")
    today_date = datetime.datetime.now().strftime("%Y%m%d")
    today_tickets = [ticket for ticket in ticket_queue.queue if ticket.date == today_date]

    if not today_tickets:
        print("No events found for today.")
    else:
        today_tickets.sort(key=lambda x: int(x.priority))  # Convert priority to integer for correct sorting
        for ticket in today_tickets:
            print(ticket)
            ticket_queue.queue.remove(ticket)

######################
###### Menu source code : https://stackoverflow.com/questions/19964603/creating-a-menu-in-python

def admin_menu(ticket_queue):
    while True:
        print("\n-- Admin Menu --")
        print("1. Display Statistics")
        print("2. Book a Ticket")
        print("3. Display all Tickets")
        print("4. Change Ticket's Priority")
        print("5. Disable Ticket")
        print("6. Run Events")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_statistics(ticket_queue)
        elif choice == '2':
            book_ticket_admin(ticket_queue)
        elif choice == '3':
            display_all_tickets(ticket_queue)
        elif choice == '4':
            change_ticket_priority(ticket_queue)
        elif choice == '5':
            disable_ticket(ticket_queue)
        elif choice == '6':
            run_events(ticket_queue)
        elif choice == '7':
            print("Exiting the program without saving.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-7).")
            

def login_form():
    print("Welcome to the Ticket Management System!")
    username = input("Enter your username: ")

    if username.lower() == "admin":
        password = input("Enter your password: ")
        admin_password = "admin123123"  # Replace with the actual admin password

        # Admin login
        attempts = 1
        while password != admin_password and attempts < 5:
            print("Incorrect Username and/or Password. Please try again.")
            password = input("Enter your password: ")
            attempts += 1

        if password == admin_password:
            print("Admin login successful. Welcome!")
            ticket_queue = import_tickets_from_file()
            admin_menu(ticket_queue)  # Call the admin_menu() function with the ticket_queue parameter
        else:
            print("Max login attempts reached. Exiting.")
    else:
        # User login
        print(" login successful. Welcome!")
        ticket_queue = import_tickets_from_file()
        user_menu(ticket_queue)  # Call the function to display the user menu here

if __name__ == "__main__":
    login_form()
