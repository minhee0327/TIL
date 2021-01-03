# sol 1: 시간초과 (여기서 develop시켜도 메모리초과나 시간초과 계속나서 sol2로 수정)
# 점화식을 혼자 찾을수는 있었지만, 공간을 미리 할당한다는 생각을 놓쳤던 문제
'''
def makeBABBA(k):
    if k == 0:
        return 'A'
    elif k == 1:
        return 'B'
    else:
        return makeBABBA(k-1) + makeBABBA(k-2)


K = int(input())

screen = makeBABBA(K)
print(screen.count('A'), screen.count('B'))

'''
# sol2: 미리 공간을 할당한 뒤에 점화식을 세워 해결
K = int(input())
a = [0] * 50
b = [0] * 50

a[0] = 1
b[1] = 1

for i in range(2, K+1):
    a[i] = a[i-1] + a[i-2]
    b[i] = b[i-1] + b[i-2]

print(a[K], b[K])
