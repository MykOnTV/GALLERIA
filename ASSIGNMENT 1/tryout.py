# MIKE KEVIN MUGAMBI SCT211-0011/2022
# Simple Python calculator for addition (sum)

def add_numbers():
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        result = number1 + number2
        print(f"The sum of {number1} and {number2} is: {result}")
    except ValueError:
        print("Invalid. Please enter valid numbers.")

if __name__ == "__main__":
    add_numbers()
