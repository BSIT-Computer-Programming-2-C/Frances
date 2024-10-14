import math  # For factorial calculation

def multiplication_table(number):
    print(f"\nMultiplication table of {number}:")
    for i in range(1, 11):  # Loop for the multiplication table
        print(f"{number} x {i} = {number * i}")

def factorial(number):
    print(f"\nFactorial of {number} is {math.factorial(number)}")

def is_prime(number):
    if number < 2:
        print(f"\n{number} is not a prime number.")
        return
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            print(f"\n{number} is not a prime number.")
            return
    print(f"\n{number} is a prime number.")

# Main program loop
while True:
    # Input validation: ensures the user enters an integer
    try:
        number = int(input("\nEnter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue

    # Checking if the number is even or odd
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

    # Displaying options for further operations
    print("\nChoose an operation:")
    print("1. Display Multiplication Table")
    print("2. Calculate Factorial")
    print("3. Check if Prime")

    choice = input("Enter your choice (1/2/3): ")

    # Performing the chosen operation
    if choice == '1':
        multiplication_table(number)
    elif choice == '2':
        factorial(number)
    elif choice == '3':
        is_prime(number)
    else:
        print("Invalid choice, please select 1, 2, or 3.")

    # Asking if the user wants to perform another operation
    repeat = input("\nDo you want to perform another operation? (yes/no): ").lower()
    if repeat != 'yes':
        print("Exiting the program. Goodbye!")
        break