def DivideByFive(start, end):
    if start > end:
        for i in range(start, end - 1, - 1):
            if i % 5 == 0:
                yield i
    elif end > start:
        for i in range(start, end + 1):
            if i % 5 == 0:
                yield i

    else:
        print("Numbers are equal")