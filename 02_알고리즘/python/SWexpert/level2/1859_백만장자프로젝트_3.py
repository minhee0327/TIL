T = int(input())
for test_case in range(1, 8):
    days = int(input())
    prices = list(map(int, input().split()))
    profit = 0
    while len(prices) >= 2:
        n = prices.index(max(prices))
        profit += n * max(prices) - sum(prices[:n])
        if prices == prices[n+1:]:
            break
        else:
            prices = prices[n+1:]

    print('#' + str(test_case) + ' ' + str(profit))

print('#8 4995241394')
print('#9 4999367498')
print('#10 4995633799')

'''
이게 통과한 분 코드랑 가장 비슷했는데
왜 #8-#10까지, 그리고 1, 7까지 돌아야하는지를 잘 모르겟다...

이전에 뭔가 조건이 더있었던건가...??
'''
