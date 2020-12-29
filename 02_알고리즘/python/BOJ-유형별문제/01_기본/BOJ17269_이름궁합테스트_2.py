N, M = map(int, input().split())
A, B = input().split()

alpha = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1,
         3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

voca = ''
min_len = min(N, M)
for i in range(min_len):
    voca += A[i] + B[i]

# min_len의 길이 이후의 길이니까, 짧은 문자는 빈문자열이기 때문에 아래와 같이 표현
voca += A[min_len:] + B[min_len:]

score = []

# ord로 알파벳의 ASCII 값을 가져와, A크기만큼 차를 구하면, 해당 알파벳의 idx값을 구할 수 있음.
# 그 idx값으로 저장해둔 '획수'를 lst에 저장
lst = [alpha[ord(i)-ord('A')] for i in voca]

for i in range(N+M-2):
    for j in range(N+M-1-i):
        lst[j] += lst[j+1]

print("{}%".format(lst[0] % 10*10 + lst[1] % 10))
