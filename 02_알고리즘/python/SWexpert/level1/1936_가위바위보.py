a, b = map(int, input().split())

if (a+1) % 3 == b % 3:
    print('B')
elif (a+2) % 3 == b % 3:
    print('A')
