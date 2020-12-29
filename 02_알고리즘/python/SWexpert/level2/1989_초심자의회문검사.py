for t in range(1, int(input())+1):
    s = input()
    if s == s[::-1]:
        print("#{} {}".format(t, 1))
    else:
        print("#{} {}".format(t, 0))
