# dictionary = a collection of {key:value} pairs
#             ordered and unchangeable

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("USA"))
# print(capitals.get("Japan"))

# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Detroit"})
# capitals.pop("China")
# capitals.popitem()

# keys = capitals.keys()
# print(keys)

# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# print(values)

# for value in capitals.values():
#     print(value)

# items = capitals.items()
# print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")