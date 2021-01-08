N = int(input())

predict = []
score = [i for i in range(1, N+1)]
satisfy = []

for _ in range(N):
    predict.append(int(input()))

predict.sort()

for i in range(N):
    satisfy.append(abs(predict[i] - score[i]))

print(sum(satisfy))

# PyPy3에서는 통과하지만, python에서는 통과하지 못했다
# 시간촤가가 떠서, import sys로 수정하니까 통과하긴 했다.
# 찾아보니 내가 작성한 코드의 2/3의 속도와 공간을 차지하는
# 코드가 있어서 확인해 보았다.
