# conditional expression = a one-line shortcut for the if-else statement (ternary operator)
#   print or assign one of two values based on a condition
#   X if condition else Y

num = 6
a = 6
b = 7
age = 20
temperature = 18
user_role = "admin"


# result = "even" if x % 2 == 0 else "odd"
# print(result)

# max_num = a if     a>b else b
# min_num = a if a<b else b
# print(max_num)
# print(min_num)

# status = "adult" if age >= 18 else "child"
# print(status)

# weather = "hot" if temperature > 20 else "cold"
# print(weather)

access_level = "full_access" if user_role == "admin" else "limited_access"
print(access_level)