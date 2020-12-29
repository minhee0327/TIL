for t in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input()))for _ in range(N)]
    ans = 0
    pivot = N//2
    for i in range(N//2):
        ans += sum(arr[i][pivot-i:pivot+i+1])
        ans += sum(arr[N-i-1][pivot-i:pivot+i+1])
    ans += sum(arr[N//2])

    print("#{} {}".format(t, ans))

'''
[Code Review]
- 먼저 마름모에 해당하는 열의 값들을 적어보았다.
- N이 7일경의 열값을 보면 행이 늘어날때마다 중앙(3)을 기준으로 양쪽으로 하나씩 늘어난다.
- 기준(pivot): 3일때 해당하는 열만 정리해보면 아래와 같이 열을 지나간다
   3
  234
 12345
0123456
 12345
  234
   3
그래서 pivot을 기준으로 맨위의 행, 맨 아래행 부터 중앙행까지 ans에 행에서 해당하는 값들을 sum한 값들을 합해갔고
마지막 중앙(0123456)을 마지막에 더해줌으로써 원하는 마름모의 값들을 저장할 수 있었다.
- 생각보다 금방 풀렸던 것 같아서 정리하고 마무리.
- O(N)을 좀 더 줄일수있는 방법이 없나 고민이 됨..
(처음에 방향벡터로 접근했는데.. 이게 더 빨리 풀릴거같아서 이렇게 접근)
'''
