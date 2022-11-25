print("Welcome to the BMI Calculator")
height = int(input("What is your height (inches)? "))
weight = int(input("What is your weight (lbs.)? "))
bmi = round((weight * 703) / (height * height), 1)

if bmi < 16:
    print(f"Your BMI is {bmi} and is considered severely underweight.")
elif bmi >= 16 and bmi <= 18.4:
    print(f"Your BMI is {bmi} and is considered underweight.")
elif bmi >= 18.5 and bmi <= 24.9:
    print(f"Your BMI is {bmi} and is considered normal.")
elif bmi >= 25 and bmi <= 29.9:
    print(f"Your BMI is {bmi} and is considered overweight.")
elif bmi >= 30 and bmi < 34.9:
    print(f"Your BMI is {bmi} and is considered moderately obese.")
elif bmi >= 35 and bmi < 39.9:
    print(f"Your BMI is {bmi} and is considered severely obese.")
else:
    print(f"Your BMI is {bmi} and is considered morbidly obese.")