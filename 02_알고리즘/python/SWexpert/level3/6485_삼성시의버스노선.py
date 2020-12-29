'''
for t in range(1, 1+int(input())):
    busStop = [0] * 5001
    ans = []

    # N
    for _ in range(int(input())):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            busStop[i] += 1
    # P
    for _ in range(int(input())):
        ans.append(busStop[int(input())])

    print("#{} {}".format(t, " ".join(map(str, ans))))
'''

'''
# 1차시도 - 시간초과
# 원인은 extend, count 인것같다.
# 미리 배열크기를 지정하고 필요한 값만 업데이트 해나가는 방식이 훨씬 적은 시간이 걸렸다.ㅠㅠ

for t in range(1, 1+int(input())):
    N = int(input())
    bus = []
    ans = []

    for _ in range(N):
        A, B = map(int, input().split())
        bus.extend([i for i in range(A, B+1)])

    P = int(input())

    for _ in range(P):
        C = int(input())
        ans.append(bus.count(C))

    print("#{} {}".format(t, " ".join(map(str, ans))))
'''
