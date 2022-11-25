print("Welcome to the BMI Calculator")
height = int(input("What is your height (inches)? "))
weight = int(input("What is your weight (lbs.)? "))
bmi = round((weight * 703) / (height * height), 1)

if bmi < 16:
    print(f"Your BMI is {bmi} and is considered severely underweight.")
elif bmi < 18.5:
    print(f"Your BMI is {bmi} and is considered underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi} and is considered normal.")
elif bmi < 30:
    print(f"Your BMI is {bmi} and is considered overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi} and is considered moderately obese.")
elif bmi < 40:
    print(f"Your BMI is {bmi} and is considered severely obese.")
else:
    print(f"Your BMI is {bmi} and is considered morbidly obese.")