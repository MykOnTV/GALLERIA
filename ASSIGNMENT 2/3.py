def calculate_bmi(weight_kg, height_m):
    # Calculation of BMI
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    else:
        return "Overweight"

def bmi_calculator():
    try:
        # Get user input for weight and height
        weight_kg = float(input("Enter your weight in kilograms: "))
        height_m = float(input("Enter your height in meters: "))

    
        bmi = calculate_bmi(weight_kg, height_m)

        # Interpretation of BMI 
        interpretation = interpret_bmi(bmi)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are categorized as: {interpretation}")

    except ValueError:
        print("Invalid input. Please enter valid values.")

if __name__ == "__main__":
    bmi_calculator()
