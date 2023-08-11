# Import the NetworkX library
import networkx as nx 


# Create an empty graph to represent the social media platform
graph = nx.Graph()

def add_user():
    username = input("Enter the username for the new user: ")
    if username in graph: # Check if the username already exists in the graph
        print("User already exists.")
    else:
        graph.add_node(username) # Add the user as a node to the graph
        print("User added successfully.")

def remove_user():
    username = input("Enter the username to remove: ")
    if username in graph: # Check if the username exists in the graph
        graph.remove_node(username) # Remove the user's node from the graph
        print("User removed successfully.")
    else:
        print("User not found.")

def send_friend_request():
    user_from = input("Enter your username: ")
    user_to = input("Enter the username of the user you want to send a friend request to: ")
    if user_from in graph and user_to in graph:
        graph.add_edge(user_from, user_to)
        print("Friend request sent.")
    else:
        print("Invalid usernames.")

def remove_friend():
    user_from = input("Enter your username: ")
    user_to = input("Enter the username of the friend you want to remove: ")
    if graph.has_edge(user_from, user_to):
        graph.remove_edge(user_from, user_to)
        print("Friend removed.")
    else:
        print("Friend not found.")

def view_friends():
    username = input("Enter your username: ")
    if username in graph:
        friends = list(graph.neighbors(username))
        print("Your friends:", ', '.join(friends))
    else:
        print("User not found.")

def view_users():
    users = list(graph.nodes())
    print("Users on the platform:", ', '.join(users))


while True:
    print("1. Add a user\n2. Remove a user\n3. Send a friend request\n4. Remove a friend")
    print("5. View your list of friends\n6. View the list of users \n7. Exit")
    choice = input("- - - - - - -\nEnter a choice: ")
    
    if choice == '1':
        add_user()
    elif choice == '2':
        remove_user()
    elif choice == '3':
        send_friend_request()
    elif choice == '4':
        remove_friend()
    elif choice == '5':
        view_friends()
    elif choice == '6':
        view_users()
    elif choice == '7':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
