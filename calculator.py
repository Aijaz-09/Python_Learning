#Calculator

operator = input("What do you wanna do (+, -, *, /, %): ")
a = float(input("Enter first number: "))
b = float(input("Enter 2nd number: "))

if operator == '+':
    print(f"{a} + {b} = {round(a+b, 2)}")
elif operator == '-':
    print(f"{a} - {b} = {round(a-b, 2)}")
elif operator == '*':
    print(f"{a} * {b} = {round(a*b, 2)}")
elif operator == '/':
    print(f"{a} / {b} = {round(a/b, 2)}")
elif operator == '%':
    print(f"{a} % {b} = {round(a%b)}")
else:
    print(f"{operator} is not a valid operator")

