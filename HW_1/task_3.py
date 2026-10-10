def Palidrome(start, end):
    if start > end:
        for i in range(start, end - 1, - 1):
            if str(i) == str(i)[::-1]:
                yield i
    elif end > start:
        for i in range(start, end + 1):
            if str(i) == str(i)[::-1]:
                yield i