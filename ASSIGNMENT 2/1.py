# MIKE KEVIN MUGAMBI SCT211-0011/2022

from datetime import datetime

def calculate_age():
    try:
        birth_year = int(input("Enter your year of birth: "))
        current_year = datetime.now().year
        age = current_year - birth_year

        # Calculate months and days
        current_month = datetime.now().month
        current_day = datetime.now().day

        birth_month = int(input("Enter your month of birth (1-12): "))
        birth_day = int(input("Enter your day of birth (1-31): "))

        if birth_month <= current_month and birth_day <= current_day:
            months = current_month - birth_month
            days = current_day - birth_day
        else:
            months = (current_month - birth_month - 1 + 12) % 12
            days = (current_day - birth_day - 1 + 30) % 30

        print(f"You are {age} years, {months} months, and {days} days old.")
    except ValueError:
        print("Invalid input. Please enter valid year, month, and day.")

if __name__ == "__main__":
    calculate_age()
