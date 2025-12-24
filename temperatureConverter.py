# Temperature Converter
unit = input("is it Celsius or Fahrenheit (C or F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((temp*9)/5 + 32, 1)
    print(f"Temperature is {temp} F")
elif unit == "F":
    temp = round((temp-32)*5/9, 1)
    unit = "Celsius"
    print(f"Temperature is {temp} C")
else:
    print(f"{unit} is not a unit")