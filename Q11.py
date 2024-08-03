def collect_values():
    # Initialize an empty list to store user inputs
    values = []

    while True:
        # Prompt the user to enter a value
        user_input = input("Enter a value (press Enter to finish): ")
        
        # Check if the input is empty
        if user_input == "":
            break  # Exit the loop if the input is empty
        
        # Add the user input to the list
        values.append(user_input)
    
    # Print the collected values
    print("Collected values:", values)

# Call the function to execute
collect_values()
