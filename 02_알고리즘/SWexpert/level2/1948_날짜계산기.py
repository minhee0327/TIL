date = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

for t in range(1, 1+int(input())):
    m1, d1, m2, d2 = map(int, input().split())
    m1, m2 = date[m1-1], date[m2-1]
    print("#{} {}".format(t, (m2+d2)-(m1+d1)+1))
