numbers = [5, 2, 1, 2, 4, 3, 2, 5, 6, 7, 3, 6, 5]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(f"Main List: {numbers}")
print(f"Unique List:{uniques}")


numbers = [5, 2, 1, 2, 4, 3, 2, 5, 6, 7, 3, 6, 5]
uniques = numbers.copy()
for number in numbers:
    count = uniques.count(number)
    if count > 1:
        for no in range(count - 1):
            uniques.remove(number)
print(f"Main List: {numbers}")
print(f"Unique List:{uniques}")
