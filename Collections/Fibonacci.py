def generate_fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(b)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)


generate_fibonacci(10)
