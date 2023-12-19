letters = "abcdefghijklmnopqrstuvwxyz"
numeros = "012345678901234"
parrot = "Norwegian Blue"
print(parrot)

# print(parrot[0:6])  # Norweg
# print(parrot[-14:-8])
# print(parrot[-4:-2])    # Bl
# print(parrot[-4:12])    # Bl
# print(parrot[-3:14])    # Bl
print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

