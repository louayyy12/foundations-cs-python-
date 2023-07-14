def countDigits(n):
    # if n is less than 10, it has only one digit
    if n < 10:
        return 1
    else:
        # Recursive case: count the current digit and call the function with the remaining digits
        return 1 + countDigits(n // 10)
def findMax(list):
    # if the list is empty, return 0 (no maximum value)
    if len(list) == 0:
        return 0
    # Base case: if the list has only one element, return that element as the maximum
    elif len(list) == 1:
        return list[0]
    else:
        # Recursive case: divide the list into two halves
        mid = len(list) // 2
        # Recursively find the maximum in the left half
        left_max = findMax(list[:mid])
        # Recursively find the maximum in the right half
        right_max = findMax(list[mid:])
        # Return the maximum of the left and right halves
        return max(left_max, right_max)
def countTags(html, tag):
    # Create opening and closing tags based on the given tag name
    opening_tag = "<" + tag + ">"
    closing_tag = "</" + tag + ">"
    count = 0
    # Find the first occurrence of the opening and closing tags in the HTML string
    start = html.find(opening_tag)
    end = html.find(closing_tag)
    # Base case: if either the opening or closing tag is not found, return the count (0)
    if start == -1 or end == -1:
        return count
    else:
        # Increment the count by 1 for the current occurrence
        count += 1
        # Recursively call the function with the remaining portion of the HTML string
        return count + countTags(html[end + len(closing_tag):], tag)
def main():
    while True:
        print("1. Count Digits")
        print("2. Find Max")
        print("3. Count Tags")
        print("4. Exit")
        print("- - - - - - - - - - - - - - -")
        # Prompt the user for a choice
        choice = input("Enter a choice: ")

        if choice == "1":
            # Prompt the user for an integer and count its digits
            num = int(input("Enter an integer: "))
            digit_count = countDigits(num)
            print("Number of digits:", digit_count)

        elif choice == "2":
            # Prompt the user for a list of integers and find the maximum value
            lst = input("Enter a list of integers (space-separated): ").split()
            lst = [int(num) for num in lst]
            max = findMax(lst)
            print("Maximum value:", max)

        elif choice == "3":
            # Use a sample HTML string and prompt the user for a tag to count
            html = '''<html>
<head>
<title>My Website</title>
</head>
<body>
<h1>Welcome to my website!</h1>
<p>Here you'll find information about me and my hobbies.</p>
<h2>Hobbies</h2>
<ul>
<li>Playing guitar</li>
<li>Reading books</li>
<li>Traveling</li>
<li>Writing cool h1 tags</li>
</ul>
</body>
</html>'''
            tag = input("Enter a tag: ")
            tag_count = countTags(html, tag)
            print("Number of occurrences of", tag + ":", tag_count)

        elif choice == "4":
            # Exit the program
            print("Exiting the program...")
            break

        else:
            # Invalid choice
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Start the main program
    main()
