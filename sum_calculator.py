#!/usr/bin/env python3

def add_numbers(num1, num2):
    """Calculate the sum of two numbers."""
    return num1 + num2


if __name__ == "__main__":
    try:
        # Get input from user
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        # Calculate sum
        result = add_numbers(first_number, second_number)

        # Display result
        print(f"The sum of {first_number} and {second_number} is {result}")

    except ValueError:
        print("Error: Please enter valid numbers")
