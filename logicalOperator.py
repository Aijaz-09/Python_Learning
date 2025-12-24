# logical operators = evaluate multiple conditions (and, or, not)
#                                  and = both conditions must be true
#                                  or = at least one condition must be true
#                                  not = inverts the condition (not false, not true)

temp = 26
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is hot outside🥵")
    print("It is sunny☀️")
elif temp <= 0 and is_sunny:
    print("It is cold outside🥶")
    print("It is sunny☀️")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside😊")
    print("It is sunny☀️")
elif temp >= 28 and not is_sunny:
    print("It is hot outside🥵")
    print("It is cloudy☁️")
elif temp <= 0 and not is_sunny:
    print("It is cold outside🥶")
    print("It is cloudy☁️")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside😊")
    print("It is cloudy☁️️")