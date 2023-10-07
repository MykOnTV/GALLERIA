def is_leap_year(year):
    if (year % 4 == 0 ):
        return True
    else:
        return False

def leap_year_checker():
    try:
        year = int(input("Enter a year: "))

        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    
    except ValueError:
        print("Invalid input. Please enter a valid year.")

if __name__ == "__main__":
    leap_year_checker()
