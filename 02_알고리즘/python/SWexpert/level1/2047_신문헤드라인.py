for s in input():
    if ord(s) >= 97:
        if s == '_':
            print("_", end="")
        elif s == '.':
            print(".", end="")
        else:
            print(chr(ord(s)-32), end="")
    else:
        print(s, end="")
