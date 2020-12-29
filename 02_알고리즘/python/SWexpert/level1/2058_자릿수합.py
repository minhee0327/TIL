n = int(input())
ret = 0
while n:
    ret += n % 10
    n //= 10

print(ret)
