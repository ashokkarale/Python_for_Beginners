mass = int(input("Input mass to convert: "))
convert_to = input("(L)bs or (K)g: ")

if convert_to == "l" or convert_to == "L":
    print(f"Your weight is {mass * 0.45} KG")
elif convert_to == "k" or convert_to == "K":
    print(f"Your weight is {mass / 0.45} LB")
else:
    print("Invalid unit!")
