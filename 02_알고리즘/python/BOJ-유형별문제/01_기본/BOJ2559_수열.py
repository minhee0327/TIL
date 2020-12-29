N, K = map(int, input().split())
C = list(map(int, input().split()))
ans = -100 * K

if N == K:
    ans = sum(C)
else:
    temp = sum(C[:K])
    ans = temp
    for i in range(K, N):
        temp -= C[i-K]
        temp += C[i]
        if ans < temp:
            ans = temp


print(ans)

'''
시간초과 원인
1. N과 K가 같을 경우를 생각 못해냈음
2. 위 코드처럼 처음에 K만큼 수를 합한다음 맨 오른쪽끝은 더해주고, 맨 왼쪽끝은 빼가는 식으로 구현하지 않았었고
3. temp = sum(C[i: i+K]) # i는 N-K만큼 회전 하면서 계속 sum함수를 호출했었다.
4. 문제는 그래서 시간이 많이 걸렸던 것...! 
'''
