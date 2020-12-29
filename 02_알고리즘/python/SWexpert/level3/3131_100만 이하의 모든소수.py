import math

for i in range(2,1000000):
    ck = 1
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            ck = 0
            break
    if ck:
        print(i, end=" ")
'''
- 에라토스테네스의채 (예전에 js로 Programmers에서 접했을때 뭔소린지 몰라서 한참 고민한 문제)
'''

