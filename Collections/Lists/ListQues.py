dlist = [1, 1, 5, 100, -20, -20, 6, 0, 0]
clist = [10, 20, 30, 40, 30, 20]
alist = [1, 2, 2, 3, 4, 4, 4, 10]

counter = 0
for i in range(len(alist)):
    if alist[i] == alist[i - 1]:
        counter += 1

print(counter)