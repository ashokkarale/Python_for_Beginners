def encode(message):
    ss = set(message)
    sorted(ss)
    outstr = ""
    for item in ss:
        counter = 0
        for ch in message:
            if item == ch:
                counter += 1
        outstr = outstr + str(counter) + item
    return outstr


print(encode("AAAACCCCCCCCBBBB"))