# Program to find the ASCII value(s) of given character(s)

def find_ascii_values():
    print("Enter characters or strings to find their ASCII values.")
    print("Type 'exit' or 'quit' to stop the program.")
    
    while True:
        user_input = input("\nEnter your input: ")
        
        if user_input.lower() in ('exit', 'quit'):
            print("Exiting the program. Goodbye!")
            break

        if not user_input:
            print("You did not enter anything. Please try again!")
            continue

        print("\nASCII values:")
        for char in user_input:
            print(f"Character: '{char}' -> ASCII Value: {ord(char)}")

if __name__ == "__main__":
    find_ascii_values()
