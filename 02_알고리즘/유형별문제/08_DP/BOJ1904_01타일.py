N = int(input())

DP = [0] * 1000001
DP[1] = 1
DP[2] = 2

for i in range(3, N+1):
    DP[i] = (DP[i-2] + DP[i-1]) % 15746

print(DP[N])

'''
수정해 나간 과정
- N이 1인경우부터 N이 6일때까지 모든 경우를 하나하나 적어보았다.
- 처음에는 i번째 경우의 수가 i-1, i-2의 경우의 수와 같아서 단순히 더해서 값을 냈다.(기본 피보나치로 생각함)
    - 그게 DP[i] = DP[i-2] + D[i-1]
    - 그런데 i번째에 될 수 있는 경우가 맨 끝에 올 수 있는게 1과 00만 올수 있으니까
        1을 제외한 경우의 수가 i-1번째 경우와 동일할 것이고(자릿수가 동일), 
        00두개를 제외한 경우의 수는는 i-2번째 경우와 동일한 것이었다.(얘도 자릿수 동일함, 배치 같음)
    - 따라서 위의 DP[i] = DP[i-2] + D[i-1] 이게 나온것!
- 거기다가, 문제에서 주어진 15746으로 나누라고 한것을 합산 할때마다 나누어 주었다.
    (처음에는 결과값만 나눴는데 모두 나눠줌)
- 배열의 크기도 문제에서 N의 최대 크기가 1000000이라고 했으므로, 0의 자리를 추가 한걸 생각하여, 1000001로 잡았다.
'''
