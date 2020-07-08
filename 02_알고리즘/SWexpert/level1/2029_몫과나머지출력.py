for t in range(1, int(input())+1):
    a, b = map(int, input().split())
    print("#{} {} {}".format(t, a//b, a % b))
