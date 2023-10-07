def calculate_tip():
    try:
        #User input for total bill amount, tip percentage, and number of people
        totalbill = float(input("Enter the total bill amount: Ksh"))
        tip_percentage = float(input("Enter the tip percentage (10, 12, or 15): "))
        num_people = int(input("Enter the number of people splitting the bill: "))

        # Check if the tip_percentage is valid
        if tip_percentage not in [10, 12, 15]:
            print("Invalid tip percentage. Please enter 10, 12, or 15.")
            return

        # The tip amount
        tip_amount = (tip_percentage / 100) * totalbill

        # The total amount including tip
        total_with_tip = totalbill + tip_amount

        # The amount each person should pay
        amount_per_person = total_with_tip / num_people

        # Display the result rounded to two decimal points
        print(f"Each person should pay: Ksh{amount_per_person:.2f}")

    except ValueError:
        print("Invalid input. Please enter valid values.")

if __name__ == "__main__":
    calculate_tip()
