input_weight = float(input("Please enter in your weight in Kilograms:"))
#asks the user to input their weight
input_height = float(input("Please enter in your Height in Meters:"))
#asks the user to input their height
bmi = round(input_weight / input_height**2 , 2)
print(f"Your Current BMI is {bmi}")

if bmi < 18.50:
   print("You are currently: Underweight")
elif bmi < 25.00:
    print("You are currently: A Healthy Weight")
elif bmi < 30.00:
    print("You are currently: Overweight.")
elif bmi > 29.99:
    print("You are currently: Obese")
