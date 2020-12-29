for t in range(1, int(input())+1):
    h1, m1, h2, m2 = map(int, input().split())
    h3, m3 = h1+h2, m1+m2
    if h3 > 12:
        h3 -= 12
    if m3 > 60:
        m3 -= 60
        h3 += 1
    print("#{} {} {}".format(t, h3, m3))
