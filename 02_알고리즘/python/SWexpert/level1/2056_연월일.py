t = int(input())

for test_case in range(1, t+1):
    tc = input()
    y, m, d = tc[:4], tc[4:6], tc[6:]
    if int(m) <= 0 or int(m) > 12:
        print("#{} {}".format(test_case, -1))
    else:
        if int(m) in [1, 3, 5, 7, 8, 10, 12]:
            if 1 <= int(d) <= 31:
                print("#{} {}/{}/{}".format(test_case, y, m, d))
            else:
                print("#{} {}".format(test_case, -1))
        elif int(m) in [9, 11, 4, 6]:
            if 1 <= int(d) <= 30:
                print("#{} {}/{}/{}".format(test_case, y, m, d))
            else:
                print("#{} {}".format(test_case, -1))
        else:
            if 1 <= int(d) <= 28:
                print("#{} {}/{}/{}".format(test_case, y, m, d))
            else:
                print("#{} {}".format(test_case, -1))
