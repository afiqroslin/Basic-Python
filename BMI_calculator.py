

print("Weight in KG: ")
weight = float(input())
print("Height in CM:")
cm = float(input())
height = cm/100

bmi = (weight/(height**2))
print("Your BMI is: ")

if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<25:
    print("Normal")
elif bmi>=25 and bmi<30:
    print("Overweight")
else:
    print("Obesity")
    
    
    
    
    
    
    
