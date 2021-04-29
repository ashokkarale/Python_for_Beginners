list_of_airlines = ["AL1", "AL2", "AL3", "AL4", "AL5"]

for airline in list_of_airlines:
    print(airline)

if "AL5" in list_of_airlines:
    print("Airline present")
else:
    print("Airline not found")

subList = list_of_airlines[0:3]
for airline in subList:
    print(airline)

print("Last 3 Airlines")

for airline in range(len(list_of_airlines) - 2, len(list_of_airlines)):
    print(list_of_airlines[airline])
