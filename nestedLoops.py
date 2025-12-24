# nested loop = a loop within another loop
#         outer loop:
#             inner loop:

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol you wanna use: ")

for y in range(rows):
    for x in range(columns):
        print(symbol, end=" ")
    print()