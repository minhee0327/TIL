'''
# python 에서 시간초과, PyPy통과...

N = int(input())
sangun = set(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))
ans = [0] * M


for i in range(M):
    if card[i] in sangun:
        ans[i] = 1

print(" ".join(map(str, ans)))

'''


'''
# 프린트를 계속 쓰면 시간이 많이 걸릴거라 생각해서 일부러 이렇게 구현하지 않았는데...
# 이렇게 하니까 통과된다....(시간보다도 )

N = int(input())
sangun = set(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))

for i in range(M):
    if card[i] in sangun:
        print(1, end=" ")
    else:
        print(0, end =" ")
        
'''

'''
# BST구현해서 풀어보기 (의외로 더 느렸다고 한다...)


def BST(num):
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2
        if num == sangun[mid]:
            return 1
        if num < sangun[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return 0


N = int(input())
sangun = sorted(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))

for c in card:
    print(BST(c), end=" ")
'''
