# string methods

# name = input("Enter your full name: ")
# phone_number = input("Enter your phone #: ")

# result = len(name)
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.find("a")
# result = name.rfind("a")

# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("@")
# phone_number = phone_number.replace(" ","")
# print(phone_number)

#EXERCISE
#Validate user input
# 1. Username is no more than 12 characters
# 2. Username must not contain spaces
# 3. Username must not contain digits

#SOLUTION
user_name = input("Enter a username: ")
if len(user_name) > 12:
    print("Username can't be more than 12 characters")
#user_name.__contains__(" "):
elif not user_name.find(" ") == -1:
    print("No spaces are allowed")
#elif user_name.__contains__("0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9"):
#the above code is better in my opinion
elif not user_name.isalpha():
    print("No digits are allowed")
else:
    print(f"Welcome {user_name}")