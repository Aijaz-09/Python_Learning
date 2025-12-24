# format specifiers = {value:flags} format a value
#                 based on what flags are inserted

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.64

# no. of decimal place to be displayed = {value:.2f{ for 2 decimal places....
# spaces allocated to display = {value:10} for 10 spaces
# padding = {value:010} for 0 padding(10 total spaces)
# left align = <
# right align(default) = >
# center align = ^
# positive no. preceeded with + sign and negative with - sign = {vlaue:+}
# or maybe use: {value: }, here all + no.s will have a space preceeding them
# thousand's separator = {value:,}
# we can also mix and match flags like {value:,.2f}

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")

