# While Loop (Infinite Loop)
while True:
    # Start the Block
    try:
        # User Input
        user_input = input("Enter a number: ")
        # Convert to Integer
        number = int(user_input)
        # Print the valid number
        print("You entered:", number)

        break  # Exit the loop if input is valid
        # Hangling Invalid Input
    except ValueError:
        # Error Message
        print("Invalid input! Please enter a valid number.")    