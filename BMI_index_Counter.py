
weight = float(input())
height  = float(input())
BMI = weight/(height*height)
print("BMI is: ", BMI)
if BMI < 18.5:
    print("Underweight")

if (BMI >= 18.5) and (BMI < 25):
    print("Normal")

if (BMI >= 25) and (BMI < 30):
    print("Overweight ")

if BMI > 30:
    print("Obesity ")
