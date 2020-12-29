for t in range( 1, 1+int(input())):
    A, B = map(int, input().split())
    print("#{} {}".format(t, (A//B)**2))