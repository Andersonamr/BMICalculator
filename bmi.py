#BMI Calculator with Inputs

print("Hello, here you find out where's your body health quality, please provide the numbers in metric format. (Kilograms and Centimeters)")

name = input("What's your name? ")
height = float(input("Whats your height? "))
weight = float(input("What's your weight? "))

height2 = height/100
bmi = weight/height2 ** 2

print("Hey", name, "your BMI is: ",bmi, ".")


# I want to add another part to tell people where they are on the subject of ther body state, like Normal weight, Underweight, Obesity and so on.
# The thing is, i don't how to code that, can someone help me with the IF statements?
