def proper_divisior(n) -> list:
    div_list = []
    for i in range(1, n):
        if n % i == 0:
            div_list.append(i)
    return div_list


divs = proper_divisior(220)
for item in divs:
    print(item)
