numbers = [23, 45, 1, 34, 55, 67, 87, 90, 34, 44, 56]
largest = numbers[0]
for number in numbers:
    if largest < number:
        largest = number
print(numbers)
print(f"{largest} is the largest.")
